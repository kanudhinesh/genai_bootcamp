import asyncio
import random

async def fetch_data(task_id: int):
    print(f'Task {task_id}: Fetching data...')
    await asyncio.sleep(random.uniform(1, 3)) # simulate a random delay
    print(f'Task: {task_id}: Data fetched')
    return f'Data from task {task_id}'


async def main():
    print('Starting async tasks...')

    # Create tasks
    tasks = [fetch_data(i) for i in range(1, 6)]

    # Run tasks concurrently
    results = await asyncio.gather(*tasks)

    print('All tasks completed...')
    print('Results: ', results)

# Run the event loop
if __name__ == '__main__':
    asyncio.run(main())


