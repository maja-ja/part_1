 # Clear the file before writing
import shared_state
# 自動遞增
def reCR():
    with open("CR.txt", "r+") as f:
        value = int(f.read().strip())
        f.seek(0)
        f.write(str(2))
        f.truncate()
print('hello world')
# file-1.py

print("我是 file-1")
shared_state.shared_logic()
print("共享變數內容：", shared_state.shared_variable)

reCR()