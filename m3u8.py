import re
import subprocess

import pyperclip

payedList = []

def filter_url(flow):
    stop = False
    pattern = re.compile('^https?://m3u8\S+.m3u8')
    str = flow.request.pretty_url
    result = pattern.search(str)
    if result:
        print(f"{flow.request.pretty_url}")
        """
            将内容设置到系统剪贴板
            """
        pyperclip.copy(flow.request.pretty_url)
        stop = True
        # 自动打开 PotPlayer 播放视频
        if flow.request.pretty_url not in payedList:
            play_video_with_potplayer(flow.request.pretty_url)

    if stop:
        # 拦截所有请求并中断
        flow.kill()

def play_video_with_potplayer(url):
    try:

        # 创建一个平行的子进程
        # 使用 PotPlayerMini.exe 播放视频
        subprocess.Popen([
            "D:\Program Files\PotPlayer\PotPlayerMini64.exe",
            "/play",
            url
        ], creationflags=subprocess.DETACHED_PROCESS, shell=True)
        payedList.append(url)
    except subprocess.CalledProcessError as e:
        print(f"无法打开 PotPlayer 播放视频: {e}")
