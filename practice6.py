import asyncio

async def send_one() -> None:
    n = 0
    while True:
        await asyncio.sleep(1)
        n += 1
        print(f'Прошло {n} секунд' if n%3!=0 else)

async def send_three() -> None:
    while True:
        await asyncio.sleep(3)
        print(f'Прошло еще 3 секунды')


async def main() -> None:
    task_1 = asyncio.create_task(send_one())
    task_2 = asyncio.create_task(send_three())

    await task_1
    await task_2


if __name__ == '__main__':
    asyncio.run(main())
