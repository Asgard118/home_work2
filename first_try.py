import requests

url = "https://akabab.github.io/superhero-api/api/"
compare_names = ["Hulk", "Captain America", "Thanos"]
compare_stat = "intelligence"

all_hero = f"{url}/all.json"
respounce = requests.get(all_hero)
hero_dara = respounce.json()

intelligence_dict = {
    hero["name"]: hero["powerstats"][compare_stat]
    for hero in hero_dara 
    if hero["name"] in compare_names
}
print(max(intelligence_dict))

with open ('Token.txt', 'r') as file:
    tok = file.readline()

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        param = {
            'path': file_path
        }
        headers = {
            'Authorization': token
        }
        respounce = requests.get(url, params=param, headers=headers)
        url_upload = respounce.json().get('href', '')
        with open (file_path, "br") as the_best:
            upload_respounce = requests.put(url_upload, files={'file': the_best})

if __name__ == '__main__':
    path_to_file = 'gosling.jpg'
    token = tok
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    # в пути файла содержется название файла ?