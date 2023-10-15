import sys
from os import listdir, path
from exif import Image
from typing import Union

def check_image_has_exif(file_path: str) -> Union[Image, None]:
    if (file_path.endswith(".jpg") or file_path.endswith(".jpeg")):
        img = Image(open(file_path, 'rb'))
        if (img.has_exif):
            return img
    return None

def remove_license_if_exists(img: Image) -> Union[Image, None]:
    if "copyright" in img.list_all():
        img.delete("copyright")
        return img
    return None

def save_image(img: Image, file_path: str) -> None:
    with open(file_path, 'wb') as new_image_file:
        new_image_file.write(img.get_file())

def remove_exif_licenses(file_path: str) -> None:
    files = [f for f in listdir(file_path) if path.isfile(path.join(file_path, f))]
    for file_index, file in enumerate(files):
        img = check_image_has_exif(path.join(file_path, file).lower())
        if (img):
            removed = remove_license_if_exists(img)
            if (removed):
                save_image(removed, path.join(file_path, file))
                print(f"INFO {file_index + 1}/{len(files)}: Removed EXIF data from {file}...")
            else:
                print(f"ERROR {file_index + 1}/{len(files)}: No license found in {file}!")
        else:
            print(f"ERROR {file_index + 1}/{len(files)}: No image or EXIF data found in {file}!")

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("Usage: python exif-license-remover.py <path>")
        exit(1)
    dir = sys.argv[1]
    remove_exif_licenses(dir)