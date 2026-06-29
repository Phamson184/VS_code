import torch
import torch.nn as nn

class AnomalyMLP(nn.Module):
    def __init__(self, input_dim):
        super(AnomalyMLP, self).__init__()
        
        # Kiến trúc Feed-Forward Neural Network
        self.net = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.ReLU(),
            nn.Dropout(0.3), # Chống Overfitting
            nn.Linear(256, 64),
            nn.ReLU(),
            nn.Linear(64, 1) # Đầu ra 1 node (0 = Normal, 1 = Anomaly)
        )
        
    def forward(self, x):
        return self.net(x).squeeze()