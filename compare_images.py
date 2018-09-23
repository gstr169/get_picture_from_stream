import cv2
import numpy as np
from pathlib import Path

# paths_list = []
# path = ''
# while path != 'done':
#     path = input()
#     paths_list.append(path)
# for i, path in enumerate(paths_list):
#     print(path)


def compare_two_images(image_path_1: str, image_path_2: str):
    img1 = cv2.imread(image_path_1)
    img2 = cv2.imread(image_path_1)
    vis = np.concatenate((img1, img2), axis=1)
    cv2.imwrite('out.png', vis)


data_folder = Path("tmp/img")
file_path = data_folder / "201809231759.avi_0.jpg"