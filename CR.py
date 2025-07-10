import subprocess

# 讀取計數器數字
with open("CR.txt", "r") as f:
    counter = f.read().strip()

# 檔名組合
filename = f"file-{counter}.py"

# 執行該檔案
subprocess.run(["python", filename])
