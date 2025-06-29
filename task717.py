import asyncio
import random

async def two(x):
  await asyncio.sleep(random.randint(1,3))
  return print(x)

async def one(x):
  await asyncio.sleep(random.randint(1,3))
  return print(x)

async def main():
  for x in range(5):
    await asyncio.gather(one(1), two(2))

asyncio.run(main())