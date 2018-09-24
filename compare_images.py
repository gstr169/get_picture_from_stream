import cv2
import numpy as np
from re import sub
from pathlib import Path

# paths_list = []
# path = ''
# while path != 'done':
#     path = input()
#     paths_list.append(path)
# for i, path in enumerate(paths_list):
#     print(path)


def compare_two_images(image_path_1: str, image_path_2: str, out_path: str):
    img1 = cv2.imread(image_path_1)
    img2 = cv2.imread(image_path_2)
    out_path = Path(out_path)
    if not out_path.exists():
        out_path.mkdir()
    vis = np.concatenate((img1, img2), axis=1)
    img1_name = sub(r"_\d.jpg", '', str(image_path_1).split('\\')[-1])
    img2_name = sub(r"_\d.jpg", '', str(image_path_2).split('\\')[-1])
    out_file = out_path / (img1_name + '_' + img2_name + '.jpg')
    cv2.imwrite(str(out_file), vis)
    print('file written: ' + str(out_file))


data_folder = Path("D:/Python Projects/get_picture_from_stream/tmp_cam_1/img")
file_path_1 = data_folder / "2018_09_23_21_25_0.jpg"
file_path_2 = data_folder / "2018_09_23_21_34_0.jpg"
out_folder = data_folder / 'compared_images'

compare_two_images(str(file_path_1), str(file_path_2), str(out_folder))
