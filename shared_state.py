# shared_state.py

def shared_logic():
    print("這是來自 shared_state 的共用邏輯")

# 從檔案讀入共享變數內容
with open("shared_state.txt", "r", encoding="utf-8") as f:
    shared_variable = f.read().strip()

