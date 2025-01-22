try:
    with open("example.txt", "x") as file:
        file.write("Fayl yangi ma'lumot bilan yaratildi.")
except FileExistsError:
    print("Fayl allaqachon mavjud!")
