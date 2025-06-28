import asyncio
import aiohttp
from codetiming import Timer

urls = [
    "http://google.com",
    "http://yahoo.com",
    "http://apple.com",
    "http://microsoft.com",
    "https://habr.com",
    "https://www.youtube.com/",
    "https://stepik.org",
    "https://docs.python.org",
    "https://stackoverflow.com/",
    "https://www.reg.ru"
]

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.url)

async def main():
    with Timer(text="Затрачено времени на запросы: {:.3f} сек"):
        tasks = [asyncio.create_task(fetch_url(link)) for link in urls]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
