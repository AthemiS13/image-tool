import os
from PIL import Image
from tkinter import Tk, filedialog

def resize_images_in_folder(folder_path, target_width, target_height, base_name):
    # Ensure the target folder exists
    output_folder = os.path.join(folder_path, "resized_images")
    os.makedirs(output_folder, exist_ok=True)

    image_counter = 1

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

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
    # Open a file dialog to select a folder
    Tk().withdraw()  # Hide the root Tkinter window
    folder_path = filedialog.askdirectory(title="Select Folder Containing Images")

    if not folder_path:
        print("No folder selected. Exiting.")
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

    resize_images_in_folder(folder_path, target_width, target_height, base_name)
    print(f"All images resized and renamed. Check the folder '{os.path.join(folder_path, 'resized_images')}'.")

if __name__ == "__main__":
    main()
