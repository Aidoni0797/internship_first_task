import asyncio

async def sleep():
  await asyncio.sleep(5)
  print('Hello world')

asyncio.run(sleep())