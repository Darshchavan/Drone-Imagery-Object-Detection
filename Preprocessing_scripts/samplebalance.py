import os
import random
from collections import defaultdict

def read_labels(label_file):
    labels = defaultdict(list)
    with open(label_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            class_label = int(parts[0])
            bbox = [float(x) for x in parts[1:]]
            labels[class_label].append(bbox)
    return labels

def balance_labels(labels, min_samples_per_class):
    balanced_labels = {}
    for class_label, samples in labels.items():
        if len(samples) >= min_samples_per_class:
            balanced_labels[class_label] = random.sample(samples, min_samples_per_class)
        else:
            balanced_labels[class_label] = samples
    return balanced_labels

def balance_labels_in_folder(folder_path, min_samples_per_class):
    for subdir, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):  # Assuming all label files have .txt extension
                label_file = os.path.join(subdir, file)
                print("Balancing labels in:", label_file)
                labels = read_labels(label_file)
                balanced_labels = balance_labels(labels, min_samples_per_class)
                
                # Write balanced labels back to the file
                with open(label_file, 'w') as f:
                    for class_label, samples in balanced_labels.items():
                        for sample in samples:
                            f.write(f"{class_label} {' '.join(str(coord) for coord in sample)}\n")

# Example usage
visdrone_folder = r"C:\Users\Darshan chavan\Desktop\MYPROJECT\MYDATANEW"  # Change this to the actual path of your visdrone folder
min_samples_per_class = 22

labels_folder = os.path.join(visdrone_folder, "labels")
balance_labels_in_folder(labels_folder, min_samples_per_class)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# import os
# import random
# from collections import defaultdict
# import shutil

# def read_labels(label_file):
#     labels = defaultdict(list)
#     with open(label_file, 'r') as f:
#         for line in f:
#             parts = line.strip().split()
#             class_label = int(parts[0])
#             bbox = [float(x) for x in parts[1:]]
#             labels[class_label].append(bbox)
#     return labels

# def balance_labels(labels, min_samples_per_class):
#     balanced_labels = {}
#     for class_label, samples in labels.items():
#         if len(samples) >= min_samples_per_class:
#             balanced_labels[class_label] = random.sample(samples, min_samples_per_class)
#         else:
#             balanced_labels[class_label] = samples
#     return balanced_labels

# def balance_data(images_folder, labels_folder, min_samples_per_class):
#     for subdir, _, _ in os.walk(labels_folder):
#         for subdirname in _:
#             label_subdir = os.path.join(labels_folder, subdirname)
#             image_subdir = os.path.join(images_folder, subdirname)
#             for subdirpath, _, files in os.walk(label_subdir):
#                 for file in files:
#                     if file.endswith(".txt"):  # Assuming all label files have .txt extension
#                         label_file = os.path.join(subdirpath, file)
#                         image_file = os.path.join(image_subdir, "images", os.path.splitext(file)[0] + ".jpg")
#                         if not os.path.exists(image_file):
#                             print(f"Image file does not exist for label file: {label_file}")
#                             continue
#                         print("Balancing labels and images:", label_file, image_file)
#                         labels = read_labels(label_file)
#                         balanced_labels = balance_labels(labels, min_samples_per_class)
                        
#                         # Write balanced labels back to the file
#                         with open(label_file, 'w') as f:
#                             for class_label, samples in balanced_labels.items():
#                                 for sample in samples:
#                                     f.write(f"{class_label} {' '.join(str(coord) for coord in sample)}\n")
                        
#                         # Copy or move corresponding image file to a new location
#                         dest_image_file = os.path.join(image_subdir, "balanced_images", os.path.basename(image_file))
#                         os.makedirs(os.path.dirname(dest_image_file), exist_ok=True)
#                         shutil.copy(image_file, dest_image_file)  # Change this line to shutil.move if you want to move instead of copy
#                         print("Image file balanced and copied to:", dest_image_file)

# # Example usage
# visdrone_folder = r"C:\Users\Darshan chavan\Desktop\MYPROJECT\MYDATANEW - Copy"  # Change this to the actual path of your visdrone folder
# min_samples_per_class = 15

# images_folder = os.path.join(visdrone_folder, "images")
# labels_folder = os.path.join(visdrone_folder, "labels")

# balance_data(images_folder, labels_folder, min_samples_per_class)


