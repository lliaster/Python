# -*- coding: utf-8 -*-
# @Time     : 2024/11/25 21:09
# @Author   : Lliaster
# @File     : 下载视频_test.py


from tqdm import tqdm
import requests

douyin_url = 'https://www.douyin.com/aweme/v1/play/?video_id=v0300fg10000cs8rlmvog65n9f050s00&line=0&file_id=08c6e9cb0f8e4b03b73a53a8db455798&sign=b5f5c8f2387c1cd5d26f59e8b8b8957e&is_play_url=1&source=PackSourceEnum_SEARCH'
douyin_url2 ='https://www.douyin.com/aweme/v1/play/?video_id=v1e00fgi0000csi4u9fog65skoj4m3u0&line=0&file_id=0e2b191ecdb74b81b38d54e632e751d5&sign=29b0c588b03be123cfa5197133c141e3&is_play_url=1&source=PackSourceEnum_PUBLISH'


def download_file(file_url, file_path):
    response = requests.get(file_url, stream=True)

    total_size = int(response.headers.get('content-length', 0))

    dowload_size = 0
    with open(file_path, 'wb') as f, tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as bar:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                dowload_size += len(chunk)
                bar.update(len(chunk))
                # print(f'下载进度:{dowload_size / total_size * 100:.2f}%')
        print('下载完成...')


path = './douyin3.mp4'

download_file(douyin_url2, path)
