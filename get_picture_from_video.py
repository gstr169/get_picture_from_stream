import cv2
import os
from pathlib import Path


def get_image_from_video(video_path: str, images_number: int):
    video_cap = cv2.VideoCapture(video_path)
    video_name = video_path.split('\\')[-1]
    video_folder = video_path.replace(video_name, '')
    for i in range(images_number):
        success, image = video_cap.read()
        img_folder = Path(video_folder) / 'img'
        if not img_folder.exists():
            img_folder.mkdir()
        img_name = video_name.replace('.avi', ('_%d.jpg' % i))
        img_path = img_folder / img_name
        cv2.imwrite(str(img_path), image)  # save frame as JPEG file


def get_images_from_folder(video_folder: str):
    data_folder = Path(video_folder)
    for file_name in os.listdir(str(data_folder)):
        file_path = data_folder / file_name
        if os.path.isfile(file_path):
            print(file_path)
            get_image_from_video(str(file_path), 1)


get_images_from_folder('D:/Python Projects/get_picture_from_stream/tmp_cam_1')
get_images_from_folder('D:/Python Projects/get_picture_from_stream/tmp_cam_2')