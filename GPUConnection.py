import torch
device = torch.device("cuda" if torch.cuda.is_available() else "CPU")
print(f"Using device {device}")



devnumber = torch.cuda.current_device()
print(f"cureent device number is {devnumber}")

devName = torch.cuda.get_device_name(devnumber)
print(f"GPU name is {devName}")

