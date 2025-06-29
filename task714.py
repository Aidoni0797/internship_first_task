import asyncio

async def two(x):
  return print(x)

async def one(x):
  return print(x)

async def main():
  task1 = asyncio.create_task(one(1))
  task2 = asyncio.create_task(two(2))
  await task1
  await task2

asyncio.run(main())