import torch

if torch.backends.mps.is_available():
    mps_device = torch.device('mps')
    x = torch.ones(1, device=mps_device)
    print(x)
    print(mps_device)
else:
    print('MPS device not found')