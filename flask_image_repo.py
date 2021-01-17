import requests
from flask import Flask, render_template, Markup, request, redirect


app = Flask(__name__)
API_KEY = '563492ad6f91700001000001b468a1cff0e34319b5287f382e03b2e1'
default_search = 'Elephant'


@app.route('/', methods=['GET', 'POST'])
def home():
    search_query = request.form.get('search') if request.method=='POST' else default_search
    return redirect(f'/search/{search_query}')
    

@app.route('/search/<search_query>')
def search(search_query):
    endpoint = 'search'
    res = requests.get(
        f'https://api.pexels.com/v1/{endpoint}', 
        params={'query': search_query}, 
        headers={'Authorization': API_KEY}
    )

    try:
        res_json = res.json()
        img_type = 'medium'
        img_urls = [{'url':img['url'], 'img':img['src'][img_type]} for img in res_json['photos']]
        results_html = ""
        for data in img_urls:
            url = data['url']
            img = data['img']
            results_html += f'<div class="search_image"><a href="{url}" target="_blank"><img src="{img}"></a><div>'
        return render_template("index.html", results = Markup(results_html))
    except:
        return "An Error Occured"


app.run(debug=True)