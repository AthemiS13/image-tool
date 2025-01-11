import os
import zipfile
from PIL import Image
from tkinter import Tk, filedialog

def extract_zip_file(zip_path, destination_folder):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(destination_folder)
            print(f"Extracted ZIP file: {zip_path}")
        os.remove(zip_path)
        print(f"Deleted ZIP file: {zip_path}")
    except Exception as e:
        print(f"Error extracting ZIP file {zip_path}: {e}")

def resize_images_recursively(folder_path, target_dimension, resize_by, base_name):
    output_folder = os.path.join(folder_path, "resized_images")
    os.makedirs(output_folder, exist_ok=True)

    image_counter = 1

    for root, _, files in os.walk(folder_path):
        if os.path.basename(root) == "resized_images":
            continue

        for filename in files:
            file_path = os.path.join(root, filename)

            if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                continue

            try:
                with Image.open(file_path) as img:
                    original_width, original_height = img.size
                    
                    if resize_by == "width":
                        aspect_ratio = original_height / original_width
                        target_height = int(target_dimension * aspect_ratio)
                        target_size = (target_dimension, target_height)
                    elif resize_by == "height":
                        aspect_ratio = original_width / original_height
                        target_width = int(target_dimension * aspect_ratio)
                        target_size = (target_width, target_dimension)
                    else:
                        print("Invalid resize choice. Exiting.")
                        return

                    resized_img = img.resize(target_size, Image.Resampling.LANCZOS)

                    new_name = f"{base_name}_{image_counter:04d}{os.path.splitext(filename)[1]}"
                    output_path = os.path.join(output_folder, new_name)

                    resized_img.save(output_path)
                    print(f"{image_counter:04d}: {filename} -> {new_name}")

                    # Increment the counter after saving a file
                    image_counter += 1
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

def main():
    Tk().withdraw()  
    print("Choose input type:")
    print("1. Folder")
    print("2. ZIP File")
    choice = input("Enter your choice (1 or 2): ")

    folder_path = ""
    if choice == "1":
        folder_path = filedialog.askdirectory(title="Select a Folder")
    elif choice == "2":
        zip_path = filedialog.askopenfilename(title="Select a ZIP File", filetypes=[("ZIP files", "*.zip")])
        if zip_path:
            folder_path = os.path.splitext(zip_path)[0]  
            os.makedirs(folder_path, exist_ok=True)
            extract_zip_file(zip_path, folder_path)
    else:
        print("Invalid choice. Exiting.")
        return

    if not folder_path:
        print("No folder or ZIP file selected. Exiting.")
        return


    print("Choose how you want to resize:")
    print("1. Specify width")
    print("2. Specify height")
    resize_choice = input("Enter your choice (1 or 2): ")

    if resize_choice == "1":
        resize_by = "width"
    elif resize_choice == "2":
        resize_by = "height"
    else:
        print("Invalid choice. Exiting.")
        return


    try:
        target_dimension = int(input(f"Enter the target {resize_by}: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the dimension.")
        return

    base_name = input("Enter the base name for the images: ")

    resize_images_recursively(folder_path, target_dimension, resize_by, base_name)
    print(f"All images resized and renamed. Check the folder '{os.path.join(folder_path, 'resized_images')}'.")

if __name__ == "__main__":
    main()
