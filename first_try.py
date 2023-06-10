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