import asyncio
import time

async def greet(name):
    print(f"Start {name}")
    await asyncio.sleep(2)
    print(f"End {name}")

async def main():
    await asyncio.gather(
        greet("Alice"),
        greet("Bob"),
        greet("Charlie"),
    )

asyncio.run(main())
