from flask import Flask, render_template, request
import requests

app = Flask(__name__)


# Rutas
@app.route('/')
def index():
    # Obtener los primeros 151 Pokémon de la PokéAPI
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
    data = response.json()
    pokemons = [{'id': idx + 1, 'name': pokemon['name']} for idx, pokemon in enumerate(data['results'])]

    return render_template('index.html', pokemons=pokemons)


@app.route('/pokemon/<int:pokemon_id>')
def pokemon_detail(pokemon_id):
    # Obtener la información de un Pokémon específico
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    pokemon = response.json()

    return render_template('pokemon.html', pokemon=pokemon)


if __name__ == '__main__':
    app.run(debug=True)
