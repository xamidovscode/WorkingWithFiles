import os

# Faylni o'chirish
file_path = "/home/joxacode/Documents/x.pptx"
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"Fayl {file_path} o'chirildi.")
else:
    print("Fayl mavjud emas!")
