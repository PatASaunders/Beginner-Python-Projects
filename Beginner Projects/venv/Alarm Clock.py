import time
import webbrowser
import schedule

video='https://www.youtube.com/watch?v=zWuWRE1o7Sk'
chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def video_open():
    webbrowser.get(chrome_path).open(video)
    return

def test(t):
    print("I'm working...", t)

schedule.every().day.at("10:00").do(video_open)

while True:
    schedule.run_pending()
    time.sleep(5)