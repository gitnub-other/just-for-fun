import webbrowser
import random
import time
import pyautogui
import os
while(1):
    file='whatever.html'
    num=int(input('按1,2,或4，无聊就按5或6，enter是确定'))
    def prank():
        pyautogui.PAUSE = 0
        pyautogui.FAILSAFE = False
        while(1):
            pyautogui.moveTo(922,621,duration=1)
            c = chr(random.randint(97, 122))
            pyautogui.typewrite(c)
    if num==1:
        print("你被骗了")
        time.sleep(3)
        webbrowser.open("https://www.bilibili.com/video/BV1eS4y157Ey/?spm_id_from=333.788.recommend_more_video.1")
    if num==2:
        print("鸡汤来了")
        time.sleep(3)
        webbrowser.open("https://www.bilibili.com/video/av984714877/")
    if num==3:
        print("你的电脑即将关机")
        os.system("shutdown -s -t  3 ")
    if num==4:
        webbrowser.open(file)
    if num==5:
        webbrowser.open(file)
        time.sleep(1)
        webbrowser.open_new_tab('bing.com')
        webbrowser.open_new_tab('bing.com')
        webbrowser.open_new_tab('bing.com')
        webbrowser.open_new_tab('bing.com')
        webbrowser.open_new_tab('bing.com')
        time.sleep(2)
        print("你被骗了")
        time.sleep(2)
        webbrowser.open("https://www.bilibili.com/video/BV1eS4y157Ey/?spm_id_from=333.788.recommend_more_video.1")
        time.sleep(15)
        os.system("shutdown -s -t  3 ")
    if num==6:
        prank()
