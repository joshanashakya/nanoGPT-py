def print_gpu_stats():
    # Print GPU stats
    device = torch.cuda.current_device()
    memory_stats = torch.cuda.memory_stats(device=device)
    t = torch.cuda.get_device_properties(0).total_memory / (1024**3)
    allocated_memory_gb = memory_stats["allocated_bytes.all.current"] / (1024**3)
    print(f"Total Memory: {t:.2f} GB")
    print(f"Allocated Memory: {allocated_memory_gb:.2f} GB")