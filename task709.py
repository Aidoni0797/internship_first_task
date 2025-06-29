import asyncio

async def nested():
  return print('Сопрограмма вызвана внутри сопрограммы async main()')

async def main():
  await nested()

asyncio.run(main())

#iDONi ты не понимаешь признвайся, у тебя все должно быть пошагово а внутри внутри твой уровень этого не поддерживает, ухх