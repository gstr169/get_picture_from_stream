import cv2
from pathlib import Path


def get_image_from_video(video_path: str, images_number: int):
    video_cap = cv2.VideoCapture(video_path)
    video_name = video_path.split('\\')[-1]
    video_folder = video_path.replace(video_name, '')
    for i in range(images_number):
        success, image = video_cap.read()
        img_folder = Path(video_folder) / 'img'
        img_name = video_name.replace('.avi', ('_%d.jpg' % i))
        img_path = img_folder / img_name
        cv2.imwrite(str(img_path), image)     # save frame as JPEG file


data_folder = Path("tmp")
file_path = data_folder / "201809231759.avi"
get_image_from_video(str(file_path), 1)



