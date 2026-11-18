import torch
from torch import nn
from torchvision import transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader

device = "cuda" if torch.cuda.is_available() else "cpu"

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

train_dataset = datasets.ImageFolder(root="bottle_custom/train_custom", transform=transform)
val_dataset = datasets.ImageFolder(root="bottle_custom/val_cusotm", transform=transform)

train_dataloader = DataLoader(train_dataset, batch_size=16, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=16, shuffle=True)




