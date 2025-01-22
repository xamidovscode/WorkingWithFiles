

# Faylni o'qish rejimida ochish
file = open("example.txt", "r")   #read rejim
content = file.read()  # Fayl ichini o'qish
print(content)
file.close()  # Faylni yopish


with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# Bu yerda fayl avtomatik yopiladi

