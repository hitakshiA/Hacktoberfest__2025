import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(urls):
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(fetch(session, u) for u in urls))
        print([len(r) for r in results])

urls = ["https://example.com", "https://httpbin.org/get"]
asyncio.run(main(urls))
