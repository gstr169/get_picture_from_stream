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

data_folder = Path("tmp/img")
file_path = data_folder / "201809231759.avi_0.jpg"
img1 = cv2.imread(str(file_path))
img2 = cv2.imread(str(file_path))
vis = np.concatenate((img1, img2), axis=1)
cv2.imwrite('out.png', vis)
