import sys
import os

# Thêm thư mục src vào path để import model.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Đường dẫn gốc của project (lên 1 cấp so với src/)
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

import numpy as np
import torch
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve,
    auc,
    precision_recall_curve,
)
from model import AnomalyMLP

# ── 1. Load dữ liệu test ────────────────────────────────────────────────────────
print("⏳ Đang nạp dữ liệu test...")
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')

X_test_vec = np.load(os.path.join(PROCESSED_DIR, 'X_test_vec.npy'))
y_test     = np.load(os.path.join(PROCESSED_DIR, 'y_test.npy'))

print(f"✅ X_test: {X_test_vec.shape} | Anomaly: {y_test.sum()} / {len(y_test)}")

# ── 2. Load model ───────────────────────────────────────────────────────────────
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'best_model.pth')
print(f"\n⏳ Đang nạp model từ {MODEL_PATH}...")

model = AnomalyMLP(input_dim=500)
model.load_state_dict(torch.load(MODEL_PATH, map_location='cpu'))
model.eval()
print("✅ Nạp model thành công!")

# ── 3. Inference ────────────────────────────────────────────────────────────────
print("\n⏳ Đang chạy inference trên tập Test...")
X_test_t = torch.tensor(X_test_vec, dtype=torch.float32)

with torch.no_grad():
    logits = model(X_test_t)
    probs  = torch.sigmoid(logits).numpy()
    preds  = (probs >= 0.5).astype(int)

# ── 4. In báo cáo ───────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  KẾT QUẢ ĐÁNH GIÁ CUỐI CÙNG")
print("=" * 55)
print(classification_report(
    y_test, preds,
    target_names=["Normal", "Anomaly"],
    digits=4
))

# ── 5. Vẽ 3 biểu đồ ────────────────────────────────────────────────────────────
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

fig = plt.figure(figsize=(16, 5))
fig.suptitle("Đánh giá mô hình — Log Anomaly Detection (HDFS)",
             fontsize=14, fontweight="bold")
gs = gridspec.GridSpec(1, 3, figure=fig, wspace=0.35)

# --- Confusion Matrix ---
ax1 = fig.add_subplot(gs[0])
cm   = confusion_matrix(y_test, preds)
disp = ConfusionMatrixDisplay(cm, display_labels=["Normal", "Anomaly"])
disp.plot(ax=ax1, colorbar=False, cmap="Blues")
ax1.set_title("Confusion Matrix")
for name, row, col in [("TN",0,0),("FP",0,1),("FN",1,0),("TP",1,1)]:
    ax1.text(col, row - 0.32, name, ha="center", va="center",
             fontsize=9, color="grey", style="italic")

# --- ROC Curve ---
ax2  = fig.add_subplot(gs[1])
fpr, tpr, _ = roc_curve(y_test, probs)
roc_auc = auc(fpr, tpr)
ax2.plot(fpr, tpr, color="#1f77b4", lw=2, label=f"AUC = {roc_auc:.4f}")
ax2.plot([0,1],[0,1], "k--", lw=1, label="Random baseline")
ax2.fill_between(fpr, tpr, alpha=0.08, color="#1f77b4")
ax2.set_xlabel("False Positive Rate")
ax2.set_ylabel("True Positive Rate")
ax2.set_title("ROC Curve")
ax2.legend(loc="lower right")
ax2.grid(True, alpha=0.3)

# --- Precision-Recall Curve ---
ax3 = fig.add_subplot(gs[2])
precision, recall, _ = precision_recall_curve(y_test, probs)
pr_auc        = auc(recall, precision)
anomaly_ratio = y_test.mean()
ax3.plot(recall, precision, color="#d62728", lw=2, label=f"PR-AUC = {pr_auc:.4f}")
ax3.axhline(y=anomaly_ratio, color="k", linestyle="--", lw=1,
            label=f"Baseline ({anomaly_ratio:.3f})")
ax3.fill_between(recall, precision, alpha=0.08, color="#d62728")
ax3.set_xlabel("Recall")
ax3.set_ylabel("Precision")
ax3.set_title("Precision-Recall Curve")
ax3.legend(loc="upper right")
ax3.grid(True, alpha=0.3)

SAVE_PATH = os.path.join(OUTPUT_DIR, 'evaluation_results.png')
plt.savefig(SAVE_PATH, dpi=150, bbox_inches="tight")
plt.show()
print(f"\n✅ Biểu đồ đã lưu tại: outputs/evaluation_results.png")
