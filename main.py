import asyncio
import aiohttp


async def parse(address: str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://app.renzoprotocol.com/api/points/{address}') as r:
                if r.status != 200:
                    return None
                result_dict = await r.json()
                if 'data' not in result_dict:
                    return None
                return float(result_dict['data']['totals']['renzoPoints'])
    except Exception as e:
            await asyncio.sleep(5)
    raise ValueError(f'Can not get points')


async def main():
    with open("wallet.txt", "r") as file:
        wallet_addresses = file.readlines()

    for address in wallet_addresses:
        print(f'{address.strip()}: {await parse(address.strip())}')  # Убираем пробельные символы



if __name__ == '__main__':
    asyncio.run(main())


