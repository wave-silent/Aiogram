'''
Asyncio - это специальная библиотека, используемая для реализации концепции асинхронного и конкурентного программирования

'''

import asyncio

async def send_hello() -> None:
    await asyncio.sleep(2)
    print('Hello')

async def send_bye() -> None:
    await asyncio.sleep(1)
    print('Bye')

async def main():
    task_1 = asyncio.create_task(send_hello())
    task_2 = asyncio.create_task(send_bye())

    await task_1
    await task_2

asyncio.run(main())
