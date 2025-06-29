import asyncio

async def two():
  print('world')

async def one():
  print('hello')
  await asyncio.sleep(1)
  await two()
  print('end!')

asyncio.run(one())

#iDONi твой мозг начал воспринимать эту программу, это хорошо пока