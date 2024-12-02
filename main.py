import os
import cv2

from convert import convert_path, convert_obj, get_max_pos


def convert_all_images():
    input_folder = "input/photos"
    print(f"Converting all images in {input_folder}...")

    for file in os.listdir(input_folder):
        convert_image(input_folder, file)

    print("Complete!")


def convert_image(folder, file):
    print(f"Converting {file}")

    convert_path(folder, file)


def convert_all_videos():
    input_folder = "input/videos"
    print(f"Converting all videos in {input_folder}...")

    for file in os.listdir(input_folder):
        convert_video(input_folder, file)

    print("Complete!")


def convert_video(folder, file):
    print(f"Converting {file}")

    video = cv2.VideoCapture(f"{folder}/{file}")

    max_y, max_x = get_max_pos()
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    output = cv2.VideoWriter(f"output/{file}", fourcc, 30, (width - max_x, height - max_y))

    while video.isOpened():
        ret, frame = video.read()

        if not ret:
            break

        output.write(convert_obj(frame))

    output.release()


convert_all_images()
convert_all_videos()
