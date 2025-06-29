import asyncio

async def nested(text, number):
  return print(text, number)

async def main():
  task = asyncio.create_task(nested('Переданное число', 333))
  await task

asyncio.run(main())