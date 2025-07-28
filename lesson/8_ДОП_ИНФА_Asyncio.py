import asyncio

async def send_time(second: int) -> None:
    #n = 0
    await asyncio.sleep(second)
    #n += second
    print(f'Прошло {second} секунд')

async def main() -> None:
    task_1 = asyncio.create_task(send_time(2))    # различные обьекты корутин! 
    task_2 = asyncio.create_task(send_time(5))
    
    await task_1
    await task_2
    

if __name__ == '__main__':
    asyncio.run(main())
