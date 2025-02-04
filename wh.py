import pyautogui
import pyperclip
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

# 加载表情图片到剪贴板
choose_1 = eval(input("1发送信息，2发送表情:"))
if choose_1 == 1:
    messages = input("请输入你要轰炸的信息:")
    times = eval(input("请输入你要轰炸的次数:"))
    print("数据已被后台接受,请将光标移动至会话框")
    for i in range(3):
        print("距离信息轰炸还需要%d秒" % (3 - i))
        time.sleep(1)
    for i in range(times):
        keyboard.type(messages)
        keyboard.press(Key.ctrl)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.release(Key.ctrl)
        time.sleep(0.1)
    print("信息轰炸已经顺利完成，已退出！")
else:
    times = eval(input("请输入你要轰炸的次数:"))
    # 切换到QQ消息窗口（这里需要根据您的QQ窗口的标题来替换）
    qq_window_title = 'QQ 聊天窗口的标题'
    pyautogui.hotkey('alt', 'tab')  # 切换到QQ窗口
    print("把光标移动到输入栏")
    time.sleep(1)  # 等待窗口切换完成

    for i in range(3):
        print("距离信息轰炸还需要%d秒" % (3 - i))
        time.sleep(1)
    # 粘贴图像（假设图像已经复制到剪贴板）
    for i in range(times):
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('ctrl', 'enter')

    print("表情轰炸已经顺利完成,已退出!")


