import os
from collections import defaultdict

def count_samples(label_file):
    class_counts = defaultdict(int)
    with open(label_file, 'r') as f:
        for line in f:
            class_label = int(line.strip().split()[0])
            class_counts[class_label] += 1
    return class_counts

def count_samples_in_folder(folder_path):
    class_counts_in_folders = {}
    for subdir, _, files in os.walk(folder_path):
        folder_name = os.path.basename(subdir)
        class_counts_in_folders[folder_name] = defaultdict(int)
        for file in files:
            if file.endswith(".txt"):  # Assuming all label files have .txt extension
                label_file = os.path.join(subdir, file)
                class_counts = count_samples(label_file)
                for class_label, count in class_counts.items():
                    class_counts_in_folders[folder_name][class_label] += count
    
    return class_counts_in_folders

# Example usage
visdrone_folder = r"C:\Users\Darshan chavan\Desktop\MYPROJECT\MYDATANEW"  # Change this to the actual path of your visdrone folder

labels_folder = os.path.join(visdrone_folder, "labels")
class_counts_in_folders = count_samples_in_folder(labels_folder)

# Print the class counts for each subfolder
for folder_name, class_counts in class_counts_in_folders.items():
    print(f"Subfolder: {folder_name}")
    for class_label, count in class_counts.items():
        print(f"Class {class_label}: {count} samples")
    print()
