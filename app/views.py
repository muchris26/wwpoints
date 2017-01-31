from app import app
from flask import render_template, request

from nutritionix import Nutritionix

# Use when deployed locally
# NUTRITIONIX_API_ID = open('env_vars/nutritionix_id', 'r')
# NUTRITIONIX_API_KEY = open('env_vars/nutritionix_key', 'r')
# nix = Nutritionix(app_id=NUTRITIONIX_API_ID, api_key=NUTRITIONIX_API_KEY)

# Use when deployed to Heroku
nix = Nutritionix(app_id=process.env.NUTRITIONIX_API_ID, api_key=process.env.NUTRITIONIX_API_KEY)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Search Page')

@app.route('/search', methods=['GET', 'POST'])
def search():
    search_term = request.args.get('search_term')

    brand_search = nix.brand().search(query=search_term).json()

    return render_template("brand_results.html",
                           title='Brand Results',
                           results=brand_search['hits'])

@app.route('/results')
def results():
    brand = request.args.get('id')

    results = []
    result_count_lower_bound = "0"
    result_count_upper_bound = "50"
    hit_count = nix.search(brand_id=brand, cal_min=50, results="0:50", fields="*").json()['total_hits']
    while len(results) < hit_count:
      result_range = result_count_lower_bound + ":" + result_count_upper_bound
      search = nix.search(brand_id=brand, cal_min=50, results=result_range, fields="*").json()['hits']

      for item in search:
        try:
          item['points'] = round((item['fields']['nf_calories'] + (item['fields']['nf_saturated_fat'] * 9) + (item['fields']['nf_sugars'] * 4) - (3.2 * item['fields']['nf_protein'])) / 33)
        except:
          item['points'] = 'NA'
        results.append(item)

      result_count_lower_bound = str(int(result_count_lower_bound) + 50)
      result_count_upper_bound = str(int(result_count_upper_bound) + 50)

    print(len(results))
    print(results)
    return render_template("search_results.html",
                           title='Search Results',
                           total_hits = len(results),
                           results=results)