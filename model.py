import torch
import torch.nn as nn

class Classifier(nn.Module):
    def __init__(self, n_inputs):
        super(Classifier, self).__init__()
        self.fc = nn.Linear(n_inputs, 1)

    def forward(self, x):
        x = self.fc(x)
        return x
