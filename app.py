from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    dog_image_respon = requests.get('https://dog.ceo/api/breeds/image/random')
    dog_fact_respon = requests.get('https://dogapi.dog/api/v2/facts')
    
    dog_image = dog_image_respon.json()['message']
    dog_fact = dog_fact_respon.json()['data'][0]['attributes']['body']
    
    cat_image_respon = requests.get('https://api.thecatapi.com/v1/images/search')
    cat_fact_respon = requests.get('https://meowfacts.herokuapp.com/')
    
    cat_image = cat_image_respon.json()[0]['url']
    cat_fact = cat_fact_respon.json()['data'][0]
    
    return render_template('index.html', dog_image=dog_image, dog_fact=dog_fact, cat_image=cat_image, cat_fact=cat_fact)

if __name__ == '__main__':
    app.run(debug=True)
