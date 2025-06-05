import os, shutil  # Import necessary modules for file and directory handling

# Ask the user to enter the full path of the directory to organize
path = input("Enter a file path: ")

# Replace backslashes (common in Windows paths) with forward slashes for consistency
path = path.replace('\\', '/')

# Ensure the path ends with a forward slash to simplify file path construction
if path[-1] != '/':  
    path += '/'

# Get a list of all files and folders in the given directory
filee = os.listdir(path)

# Loop through each item in the directory
for file in filee:
    # Extract the file extension (e.g., '.jpg', '.pdf', etc.)
    ext = os.path.splitext(file)[1]

    # Proceed only if the item has a file extension (i.e., it's a file, not a folder)
    if ext:
        # Create a folder name based on the extension (e.g., 'jpgfile', 'pdffile')
        folder_name = ext[1:] + 'file'  # ext[1:] removes the leading dot from extension

        # If the folder for this file type doesn't exist, create it
        if not os.path.exists(path + folder_name):
            os.makedirs(path + folder_name)

        # Move the file to the appropriate folder if it doesn't already exist there
        if not os.path.exists(path + folder_name + '/' + file):
            shutil.move(path + file, path + folder_name + '/' + file)

