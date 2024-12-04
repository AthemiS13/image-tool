# Image Tool

## Description

The Image Tool is a Python-based script designed to streamline bulk image resizing and renaming tasks. It supports images in a folder or inside a ZIP archive. The tool resizes images to a user-specified resolution, renames them using a customizable base name and sequential numbering, and outputs them to a `resized_images` folder.

---

## Features

- **ZIP File Extraction**: Automatically extracts ZIP archives, processes their contents, and deletes the archive.
- **Folder Support**: Processes images in folders and subfolders recursively.
- **Customizable Resizing**: Users can specify target dimensions (width and height).
- **Batch Renaming**: Assigns a common base name and four-digit sequential numbers to output images.
- **Cross-Platform Compatibility**: Works on all major operating systems supported by Python.

---

## Requirements

### Supported Operating Systems

- **Windows** (7, 10, 11)
- **Linux** (any distribution supporting Python)
- **macOS**

### Supported Python Versions

- Python 3.7 and above

### Necessary Libraries

- **Pillow** (for image processing)
- **tkinter** (for folder/file selection dialogs)

---

## Installation

### Step 1: Install Python

Ensure you have Python 3.7 or higher installed. Download Python from the [official Python website](https://www.python.org/).

### Step 2: Install Required Libraries

Install the necessary libraries using `pip`:

```bash
pip install pillow
