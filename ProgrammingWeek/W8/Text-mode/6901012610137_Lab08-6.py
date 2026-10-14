import os

# Change this to the folder you want to scan
directory = "."

image_extensions = (".jpg", ".jpeg", ".gif", ".png")


def list_all_files(path):
    entries = os.listdir(path)
    files = []
    for entry in entries:
        if os.path.isfile(os.path.join(path, entry)):
            files.append(entry)
    return files


def total_size(path, files):
    total = 0
    for f in files:
        total += os.path.getsize(os.path.join(path, f))
    return total


def filter_images(files):
    images = []
    for f in files:
        if f.lower().endswith(image_extensions):
            images.append(f)
    return images


def show_file_list(path, files, label):
    print(f"\n{label} ({len(files)} files)")
    for f in files:
        size = os.path.getsize(os.path.join(path, f))
        print(f"  {f:30} {size:>10} bytes")


all_files = list_all_files(directory)
show_file_list(directory, all_files, f"All files in '{directory}'")
print(f"\nTotal size of all files: {total_size(directory, all_files)} bytes")

image_files = filter_images(all_files)
show_file_list(directory, image_files, "Image files only (.jpg, .jpeg, .gif, .png)")
print(f"\nTotal size of image files: {total_size(directory, image_files)} bytes")
#6901012610137
#lab7-6