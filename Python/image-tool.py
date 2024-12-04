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

def resize_images_recursively(folder_path, target_width, target_height, base_name):
    # Ensure the target folder exists
    output_folder = os.path.join(folder_path, "resized_images")
    os.makedirs(output_folder, exist_ok=True)

    image_counter = 1

    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Skip non-image files
            if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                print(f"Skipping non-image file: {filename}")
                continue

            try:
                with Image.open(file_path) as img:
                    # Resize the image using LANCZOS resampling
                    resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

                    # Generate a new name with base name and four-digit counter
                    new_name = f"{base_name}_{image_counter:04d}{os.path.splitext(filename)[1]}"
                    output_path = os.path.join(output_folder, new_name)

                    # Save the resized and renamed image
                    resized_img.save(output_path)
                    print(f"Resized and renamed: {output_path}")

                    image_counter += 1
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

def main():
    # Ask the user if they want to select a folder or a ZIP file
    Tk().withdraw()  # Hide the root Tkinter window
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
            folder_path = os.path.splitext(zip_path)[0]  # Remove .zip extension for the folder name
            os.makedirs(folder_path, exist_ok=True)
            extract_zip_file(zip_path, folder_path)
    else:
        print("Invalid choice. Exiting.")
        return

    if not folder_path:
        print("No folder or ZIP file selected. Exiting.")
        return

    # Get the target resolution from the user
    try:
        target_width = int(input("Enter the target width: "))
        target_height = int(input("Enter the target height: "))
    except ValueError:
        print("Invalid input. Please enter valid integers for width and height.")
        return

    # Get the base name for renaming images
    base_name = input("Enter the base name for the images: ")

    resize_images_recursively(folder_path, target_width, target_height, base_name)
    print(f"All images resized and renamed. Check the folder '{os.path.join(folder_path, 'resized_images')}'.")

if __name__ == "__main__":
    main()
