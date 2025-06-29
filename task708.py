import asyncio

async def main():
  await asyncio.sleep(1)
  running_loop = asyncio.get_running_loop()
  print(running_loop)

asyncio.run(main())