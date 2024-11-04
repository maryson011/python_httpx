from asyncio import all_tasks, create_task, run, sleep

async def ola(val, delay=1):
    print(f'Inicio da corrotina {val}')
    await sleep(delay)
    print(f'Meio da corrotina {val}')
    await sleep(delay)
    print(f'Fim da corrotina {val}')

async def main():
    task1 = create_task(ola(1, 2)) # COrrotina
    task2 = create_task(ola(2)) # COrrotina
    task3 = create_task(ola(3)) # COrrotina
    task4 = create_task(ola(4)) # COrrotina
    print('Fila de taks: ', all_tasks())

    await task1
    await task2
    await task3
    await task4
    print('Fila de taks: ', all_tasks())

run(main()) # Corrotina