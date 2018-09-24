import time
import requests
from pathlib import Path


def get_middle_playlist_name(url: str):
    with requests.Session() as session:
        response = session.get(url)
        text = str(response.content, encoding='utf-8').strip(' \n')
        return text.split('\n')[-1]


def get_video_name(url: str):
    with requests.Session() as session:
        response = session.get(url)
        text = str(response.content, encoding='utf-8').strip(' \n')
        return text.split('\n')[-1]


def write_video_to_file(url: str, directory_path: str):
    print("Recording video...")
    data_folder = Path(directory_path)
    if not data_folder.exists():
        data_folder.mkdir()
    filename = data_folder / (time.strftime("%Y_%m_%d_%H_%M", time.localtime()) + ".avi")
    try:
        file_create = open(filename, 'x')
        file_create.close()
    except FileExistsError:
        print('File exist')
    file_handle = open(filename, 'wb')
    with requests.Session() as session:
        response = session.get(url)
        file_handle.write(response.content)
        file_handle.close()
    print("File writen")


def get_video_from_m3u8_url(m3u8_url: str, directory_path: str):
    playlist_name = m3u8_url.split('/')[-1]
    stream_url = m3u8_url.replace(playlist_name, '')
    playlist_name = get_middle_playlist_name(stream_url + playlist_name)
    video_name = get_video_name(stream_url + playlist_name)
    write_video_to_file(stream_url + video_name, directory_path)


# time in seconds, for recording
start_time_in_seconds = time.time()

cam_url = "https://video.kvartalkotelniki.ru/live/F3.stream/"
name = 'playlist.m3u8'
path = 'D:/Python Projects/get_picture_from_stream/tmp_cam_1'
get_video_from_m3u8_url(cam_url + name, path)

cam_url = "https://video.kvartalkotelniki.ru/live/F1.stream/"
name = 'playlist.m3u8'
path = 'D:/Python Projects/get_picture_from_stream/tmp_cam_2'
get_video_from_m3u8_url(cam_url + name, path)

elapsed_time = time.time() - start_time_in_seconds
print('Time elapsed: {0} seconds'.format(elapsed_time))
