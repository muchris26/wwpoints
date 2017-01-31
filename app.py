from nutritionix import Nutritionix
import urllib

nix = Nutritionix(app_id="8e67c8aa", api_key="417132652b6773b0ac8f06398637d6b4")

# pizza = nix.search("pizza")

# results = pizza.json()

# print(results)


# brand_search = nix.brand().search(query="McDonalds").json()
# {'total': 2, 'max_score': 10.270647, 'hits': [{'_index': 'f762ef22-e660-434f-9071-a10ea6691c27', '_type': 'brand', '_id': '513fbc1283aa2dc80c000053', '_score': 10.270647, 'fields': {'name': "McDonald's", 'website': 'http://www.mcdonalds.com', 'type': 1, '_id': '513fbc1283aa2dc80c000053'}}, {'_index': 'f762ef22-e660-434f-9071-a10ea6691c27', '_type': 'brand', '_id': '55918cab54929366608f7483', '_score': 6.3471847, 'fields': {'name': "Mcdonald's Grocery", 'website': None, 'type': 2, '_id': '55918cab54929366608f7483'}}]}

brand_search = urllib.request("https://api.nutritionix.com/v1_1/search/?brand_id=51cb34aa97c3e632be9f397e&results=0%3A50&cal_min=300&fields=*&appId=8e67c8aa&appKey=417132652b6773b0ac8f06398637d6b4")

print(brand_search)