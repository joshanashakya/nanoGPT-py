import torch
import sys
import psutil

print("--- SOFTWARE ENVIRONMENT ---")
print(f"Python Version : {sys.version.split()[0]}")
print(f"PyTorch Version: {torch.__version__}")

print("\n--- SYSTEM MEMORY (RAM) ---")
virtual_mem = psutil.virtual_memory()
print(f"Total System RAM: {virtual_mem.total / (1024**3):.2f} GB")
# print(f"Available RAM   : {virtual_mem.available / (1024**3):.2f} GB")

print("\n--- GPU ENVIRONMENT ---")
# print(f"CUDA Available (GPU): {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU Model           : {torch.cuda.get_device_name(0)}")
    print(f"Total GPU VRAM      : {torch.cuda.get_device_properties(0).total_memory / (1024**3):.2f} GB")
else:
    print("No NVIDIA GPU detected. Running on CPU.")