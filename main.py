import os

import cv2

from convert import convert_image


def convert_all_images():
    input_folder = "photos"
    print(f"Converting all images in {input_folder}...")

    for file in os.listdir(input_folder):
        print(f"Converting {file}")
        convert_image(input_folder, file)

    print("Complete!")




convert_all_images()
