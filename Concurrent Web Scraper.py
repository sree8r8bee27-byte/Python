import asyncio, aiohttp

async def fetch_title(session, url):
    async with session.get(url) as response:
        html = await response.text()
        # Basic parsing for demonstration
        try:
            title = html.split('<title>')[1].split('</title>')[0]
            return f"{url}: {title}"
        except IndexError:
            return f"{url}: No title found"

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_title(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# Usage: titles = asyncio.run(main(['https://google.com', 'https://python.org']))
