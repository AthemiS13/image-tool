# Image Tool
## Description
The Image Tool is a Python-based script for bulk image resizing and renaming. It supports images located in folders or inside ZIP archives. The script resizes images to user-specified dimensions, renames them using a customizable base name with sequential numbering, and saves the processed images in a resized_images folder.
Additionally, it handles ZIP files by extracting their contents, processing the images, and deleting the original ZIP file after extraction.

## Features
ZIP File Handling: Automatically extracts ZIP archives, processes their images, and deletes the ZIP after extraction.
Folder Support: Processes images in folders and subfolders recursively.
Customizable Resizing: Allows users to specify width and height for resizing.
Batch Renaming: Renames images with a common base name and four-digit sequential numbers.
Cross-Platform Compatibility: Works on Windows, macOS, and Linux.
## Requirements
### Supported Operating Systems
-Windows (7, 10, 11)

-Linux (any distribution supporting Python)

-macOS
### Supported Python Versions
Python 3.7 and above
### Necessary Libraries

#### Pillow: For image processing.
#### tkinter: For folder and file selection dialogs.

## Installation
### Step 1: Install Python
Ensure Python 3.7 or higher is installed on your system. Download Python from the official Python website.

### Step 2: Install Required Libraries
Install the required libraries using pip:

pip install pillow tk

If you are using Linux, you may need to install tkinter manually if it is not pre-installed. Use the following commands depending on your distribution:

### On Ubuntu/Debian-based systems:

sudo apt-get install python3-tk

### On Fedora/RHEL-based systems:

sudo dnf install python3-tkinter

### On Windows/macOS, tkinter should be installed with Python by default. If it is missing, reinstall Python and ensure the tkinter option is selected or use the command.

### Step 3: Clone or Download the Repository
Clone the repository using git:

git clone shttps://github.com/AthemiS13/image-tool
Or download the repository as a ZIP file and extract it.

## Usage

### Running the Tool

Navigate to the directory containing the script and run it:

```bash
python image-tool.py
Steps in the Script
Select Input: Use the graphical file dialog to choose a folder or ZIP file.
Set Dimensions: Enter the desired width and height for resizing.
Set Base Name: Provide a base name for renaming the images.
## Output
Resized Images: Saved in a resized_images folder within the selected directory.
ZIP Files: Automatically extracted, processed, and deleted. Images from the ZIP are saved in the same directory.
