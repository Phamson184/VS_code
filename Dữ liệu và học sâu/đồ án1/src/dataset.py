import pandas as pd
import re
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def load_and_parse_data(log_file, label_file):
    print("⏳ [1/4] Đang đọc và bóc tách dữ liệu log...")
    pattern = re.compile(r'(blk_-?\d+)')
    records = []
    
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            blocks = pattern.findall(line)
            for blk in set(blocks):
                records.append({'BlockId': blk, 'Content': line.strip()})
                
    df = pd.DataFrame(records)
    print(f"✅ Đã quét xong {len(df)} dòng log chứa BlockId.")
    
    print("⏳ [2/4] Đang gom nhóm (Group by) các sự kiện theo từng phiên (Session)...")
    sessions = df.groupby('BlockId')['Content'].apply(list).reset_index()
    
    print("⏳ [3/4] Đang gán nhãn Normal/Anomaly cho từng phiên...")
    labels = pd.read_csv(label_file)
    sessions = sessions.merge(labels, on='BlockId', how='inner')
    return sessions

def preprocess_and_split(sessions_df, output_dir="data"):
    print("⏳ [4/4] Đang tiền xử lý văn bản và chia tập dữ liệu (Stratified Split)...")
    sessions_df['text'] = sessions_df['Content'].apply(lambda x: ' '.join(x))
    sessions_df['label_int'] = (sessions_df['Label'] == 'Anomaly').astype(int)

    X = sessions_df['text'].values
    y = sessions_df['label_int'].values

    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp)

    print("⏳ Đang chuyển đổi Text thành Vector số (TF-IDF)...")
    vectorizer = TfidfVectorizer(max_features=500)
    
    X_train_vec = vectorizer.fit_transform(X_train).toarray()
    X_val_vec = vectorizer.transform(X_val).toarray()
    X_test_vec = vectorizer.transform(X_test).toarray()

    with open(os.path.join(output_dir, 'tfidf_vectorizer.pkl'), 'wb') as f:
        pickle.dump(vectorizer, f)

    print("\n🚀 HOÀN TẤT GIAI ĐOẠN 1 & 2!")
    return X_train_vec, X_val_vec, X_test_vec, y_train, y_val, y_test

if __name__ == "__main__":
    LOG_PATH = 'data/HDFS.log'
    LABEL_PATH = 'data/anomaly_label.csv'
    
    if not os.path.exists(LOG_PATH) or not os.path.exists(LABEL_PATH):
        print("❌ Lỗi: Không tìm thấy file dữ liệu.")
    else:
        sessions_data = load_and_parse_data(LOG_PATH, LABEL_PATH)
        X_tr, X_v, X_te, y_tr, y_v, y_te = preprocess_and_split(sessions_data)