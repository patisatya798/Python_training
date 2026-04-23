import os
import time

def get_files(directories):
    files = []
    for directory in directories:
        for root, dirs, filenames in os.walk(directory):
            for file in filenames:
                full_path = os.path.join(root, file)
                files.append(full_path)
    return files

def is_stale(file_path, days):
    current_time = time.time()
    modified_time = os.path.getmtime(file_path)

    days_old = (current_time - modified_time) / (60 * 60 * 24)

    return days_old > days

def get_file_info(file_path):
    name = os.path.basename(file_path)
    size = os.path.getsize(file_path)
    modified_time = time.ctime(os.path.getmtime(file_path))
    _, ext = os.path.splitext(file_path)

    return name, ext, size, modified_time

def generate_report(stale_files):
    total_files = 0
    total_size = 0

    print("\n--- Stale Files Report ---\n")

    for file in stale_files:
        name, ext, size, modified_time = file
        print(f"Name: {name}")
        print(f"Type: {ext}")
        print(f"Size: {size} bytes")
        print(f"Last Modified: {modified_time}")
        print("-" * 30)

        total_files += 1
        total_size += size

    print("\nTotal Files:", total_files)
    print("Total Size:", total_size, "bytes")

def main():
    directories = input("Enter directories: ").split(",")
    days = int(input("Enter number of days: "))

    files = get_files(directories)

    stale_files = []

    for file in files:
        try:
            if is_stale(file, days):
                info = get_file_info(file)
                stale_files.append(info)
        except Exception:
            pass  

    generate_report(stale_files)

if __name__ == "__main__":
    main()