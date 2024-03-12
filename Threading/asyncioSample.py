''' concurrent task - asyncio.create_task() TaskGroup() 
   nesting await call- pass control back to event loop
'''
import asyncio
async def nested(): #coroutine
    print("42")

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')
    await nested()
asyncio.run(main())