

# Example usage:
text_folder = r'C:\Users\Darshan chavan\Desktop\MYPROJECT\VisDrone\labels\val'
output_folder = r'C:\Users\Darshan chavan\Desktop\MYPROJECT\MYDATANEW\labels\val'


import os

# Function to filter annotations for specified classes and assign new class labels starting from 0
def filter_annotations(text_folder, output_folder):
    # Define the classes to include and their corresponding new labels
    classes_to_include = {'0': 0, '1': 1, '3': 2, '5': 3, '8': 4}

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each text file in the text folder
    for text_file in os.listdir(text_folder):
        if text_file.endswith('.txt'):
            print(f'Processing text file: {text_file}')
            with open(os.path.join(text_folder, text_file), 'r') as file:
                lines = file.readlines()

            # Create a new text file to store filtered annotations
            filtered_lines = []
            for line in lines:
                # Split the line and extract class label
                parts = line.strip().split()
                class_label = parts[0]

                # If the class label is in the classes to include, assign it the new label
                if class_label in classes_to_include:
                    parts[0] = str(classes_to_include[class_label])
                    filtered_lines.append(' '.join(parts) + '\n')

            # Save the filtered annotations to a new text file if there are any annotations
            if filtered_lines:
                output_file = os.path.join(output_folder, text_file)
                with open(output_file, 'w') as file:
                    file.writelines(filtered_lines)
                    print(f'Saved filtered annotations to: {output_file}')



filter_annotations(text_folder, output_folder)

