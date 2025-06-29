import asyncio

async def two():
  print('world')

async def one():
  print('hello')
  await asyncio.sleep(1)
  await two()
  print('end!')

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(one())