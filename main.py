import requests

class WebScraping:

    def __init__(self, url):
        self.url = url

    def get_json_data(self):
        data = requests.get(url=self.url)
        return data.json().get("results")  # [] ko'p malumot qaytadi

    def copy_data_file(self):
        datas = self.get_json_data()
        with open("course.txt", "w") as file:
            for data in datas:
                file.write(f"{data.get('title')}\n")

url = "https://admin.soffstudy.uz/api/v1/courses/courses-list/"
a = WebScraping(url)

print(a.copy_data_file())

