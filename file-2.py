def reCR():
    with open("CR.txt", "r+") as f:
        value = int(f.read().strip())
        f.seek(0)
        f.write(str(1))
        f.truncate()
print('hello world2')
# file-2.py
import shared_state

print("我是 file-2")
shared_state.shared_logic()
print("共享變數內容：", shared_state.shared_variable)

reCR()