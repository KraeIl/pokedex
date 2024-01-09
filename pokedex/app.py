from flask import Flask, render_template, request, redirect, session
import requests

app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def index():
    
    if 'input' in session and session['input'] != None:
        try:
            data = fetchPokemon(session['input'])
            poke_image = data['sprites']['versions']['generation-viii']['black-white']['animated']['front_default']
            poke_name = data['name']
            poke_id = data['id']
            
        except Exception:
            session['input'] = '1'
            poke_image = '../static/MissingNo.png'
            poke_name = 'MissingNo.'
            poke_id = '?????'
        
    else:
        data = fetchPokemon('1')
    
    return render_template('index.html', poke_id = poke_id, poke_name = poke_name, poke_image = poke_image)

@app.route('/search', methods=['POST', ])
def search():
    session['input'] = request.form['input_search'].lower()
        
    return redirect('/')

def fetchPokemon(pokemon):
    APIresponse = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    data = APIresponse.json()    
    
    return data
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)


