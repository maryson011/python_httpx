## Uma API de pokémon
## https://pokeapi.co/api/v2/pokemon/charmander

from httpx import Client

poke = 'magikarp'

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

    print(evolution_chain)

    # request 3
    response3 = client.get(evolution_chain)
    evolution_name = (
        response3
        .json()
        .get('chain')
        .get('evolves_to')[0]
        .get('species')
        .get('name')
    )
    print(evolution_name)

