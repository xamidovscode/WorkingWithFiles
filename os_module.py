# import os
#
# # Faylni o'chirish
# file_path = "/home/joxacode/Documents/x.pptx"
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f"Fayl {file_path} o'chirildi.")
# else:
#     print("Fayl mavjud emas!")


import os

dir_path = "/home/joxacode/Documents/WorkingWithFiles"

if os.path.exists(dir_path) and os.path.isdir(dir_path):
    os.rmdir(dir_path)  # Bo'sh direktoriyani o'chiradi
    print(f"Direktoriya {dir_path} o'chirildi.")
else:
    print("Direktoriyaning mavjud emasligi yoki u bo'sh emasligi.")
