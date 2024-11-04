## Uma API de pokémon
## https://pokeapi.co/api/v2/pokemon/charmander

from httpx import Client

# pokemons = ['magikarp','bulbasaur', 'squirtle']

from pokes import pokes as pokemons

def evolucao(poke):
    print(f'Entrada: {poke}')
    with Client(base_url='https://pokeapi.co/api/v2') as client:
        # request 1
        response = client.get(f'/pokemon/{poke}')
        id_ = response.json().get('id')

        # request 2
        response2 = client.get(f'/pokemon-species/{id_}')
        evolution_chain = (
            response2
            .json()
            .get('evolution_chain')
            .get('url')
        )

        # request 3
        response3 = client.get(evolution_chain)
        chain_data = evolution_name = (
            response3
            .json()
            .get('chain')
        )
        # verificar se há evolução
        evolves_to = chain_data.get('evolves_to')
        if evolves_to:
            evolution_name = (
                evolves_to[0]
                .get('species')
                .get('name')
            )
            print(f'Saída: {poke} => {evolution_name}')
        else:
            print(f'Saída: {poke} => sem evolução')
        

for poke in pokemons:
    evolucao(poke)