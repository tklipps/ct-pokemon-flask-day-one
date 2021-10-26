from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html.j2')


@app.route('/pokeinfo', methods=['GET', 'POST'])
def pokeinfo():
    if request.method == 'POST':
        poke = request.form.get('poke')
        url = f"https://pokeapi.co/api/v2/pokemon/{poke}"
        response = requests.get(url)
        if response.ok:           
            if not response.json():
                 return "That's not a Pokemon!!!"
            data = response.json()            
            
            poke_dict={
                'poke_name':data['name'],
                'base_hp':data['stats'][0]['base_stat'],
                'base_defense':data['stats'][2]['base_stat'],
                'base_attack':data['stats'][1]['base_stat'],                    
                'front_shiny':data["sprites"]["front_shiny"],
            }
                
            print(poke_dict)
            return render_template('pokeinfo.html.j2', poke=poke_dict)     
        
        else:
            return "That's not a Pokemon!!!"
            

    return render_template('pokeinfo.html.j2')