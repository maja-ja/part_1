import keyboard
import time
import os

def 按ESC兩下停止程式():
    esc_count = 0
    last_time = 0
    while True:
        if keyboard.is_pressed('esc'):
            now = time.time()
            if now - last_time < 0.5:
                esc_count += 1
            else:
                esc_count = 1
            last_time = now
            if esc_count == 2:
                print("偵測到兩次 ESC，程式結束。")
                os._exit(0)
            while keyboard.is_pressed('esc'):
                time.sleep(0.05)  # 等待放開
        time.sleep(0.05)