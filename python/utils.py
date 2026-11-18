import os
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt


device = "cuda" if torch.cuda.is_available() else "cpu"

def tensor_display(img_torch):

    img_np = img_torch.squeeze(0).permute(1, 2, 0).cpu().numpy()

    plt.figure()
    plt.imshow(img_np, interpolation='bicubic')
    plt.show()


def tensor_load(filename):

    img_np = plt.imread(filename)

    if img_np.max() > 1 :
        img_np = img_np/img_np.max()

    img_tensor = torch.tensor(img_np, dtype=torch.float, device=device, requires_grad=False).permute(2, 0, 1).unsqueeze(0)

    return img_tensor
