from asyncio import gather, run
from httpx import AsyncClient

from pokes import pokes

async def evolucao(poke):
    async with AsyncClient(
            base_url='https://pokeapi.co/api/v2'
        ) as client:
        # request 1
        response = await client.get(f'/pokemon/{poke}')
        id_ = response.json().get('id')

        # request 2
        response = await client.get(f'/pokemon-species/{id_}')
        evolution_chain = (
            response
            .json()
            .get('evolution_chain')
            .get('url')
        )

        # request 3
        response = await client.get(evolution_chain)
        chain_data = evolution_name = (
            response
            .json()
            .get('chain')
        )
        envolves_to = chain_data.get('evolves_to')
        if envolves_to:
            evolution_name = (
                envolves_to[0]
                .get('species')
                .get('name')
            )
            print(evolution_name)
        else:
            print('sem evolução')
            
        

async def main():
    tasks = [evolucao(poke) for poke in pokes]
    await gather(*tasks)

run(main())