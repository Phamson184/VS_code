import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import os

# Import các module tự viết trong thư mục src
from dataset import load_and_parse_data, preprocess_and_split
from model import AnomalyMLP

def run_training_pipeline():
    print("--- KHỞI ĐỘNG LUỒNG HUẤN LUYỆN ---")
    
    # 1. Gọi luồng xử lý dữ liệu từ dataset.py
    log_path = 'data/HDFS.log'
    label_path = 'data/anomaly_label.csv'
    sessions_data = load_and_parse_data(log_path, label_path)
    X_train, X_val, X_test, y_train, y_val, y_test = preprocess_and_split(sessions_data)
    
    # 2. Đóng gói dữ liệu vào DataLoader của PyTorch
    print("\n⏳ Đang nạp dữ liệu vào Tensor...")
    train_loader = DataLoader(TensorDataset(torch.tensor(X_train, dtype=torch.float32), 
                                            torch.tensor(y_train, dtype=torch.float32)), 
                              batch_size=256, shuffle=True)
    val_loader = DataLoader(TensorDataset(torch.tensor(X_val, dtype=torch.float32), 
                                          torch.tensor(y_val, dtype=torch.float32)), 
                            batch_size=256)

    # 3. Khởi tạo Mô hình và Cơ chế Phạt trọng số (Class Imbalance)
    model = AnomalyMLP(input_dim=500)
    pos_weight = torch.tensor([(y_train == 0).sum() / (y_train == 1).sum()], dtype=torch.float32)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    # 4. Vòng lặp Huấn luyện (Training Loop)
    epochs = 50
    patience = 8
    best_val_loss = float('inf')
    epochs_no_improve = 0

    print(f"\n🚀 Bắt đầu huấn luyện với pos_weight = {pos_weight.item():.2f}")
    for epoch in range(epochs):
        model.train()
        for X_batch, y_batch in train_loader:
            optimizer.zero_grad()
            loss = criterion(model(X_batch), y_batch)
            loss.backward()
            optimizer.step()
            
        # Tính Loss trên tập Validation
        model.eval()
        val_loss = 0
        with torch.no_grad():
            for xb, yb in val_loader:
                val_loss += criterion(model(xb), yb).item()
        val_loss /= len(val_loader)
        
        print(f"Epoch {epoch+1:02d} | Val Loss: {val_loss:.4f}")
        
        # Cơ chế Early Stopping & Lưu Model
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            epochs_no_improve = 0
            os.makedirs('models', exist_ok=True)
            torch.save(model.state_dict(), 'models/best_model.pth')
        else:
            epochs_no_improve += 1
            if epochs_no_improve >= patience:
                print(f"⚠️ Dừng sớm tại Epoch {epoch+1} (Val loss không giảm).")
                break

    print("\n✅ Hoàn tất! File mô hình đã được lưu tại: models/best_model.pth")

if __name__ == "__main__":
    run_training_pipeline()