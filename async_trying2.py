import random
from time import sleep
import asyncio

def task(pid):
    """Synchronous non-deterministic task."""
    sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)

async def task_coro(pid):
    """Coroutine non-deterministic task."""
    await asyncio.sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)

def synchronous():
    for i in range(1, 10):
        task(i)

async def asynchronous():
    tasks = [asyncio.ensure_future(task_coro(i)) for i in range(1, 10)]
    await asyncio.wait(tasks)

print('Synchronous:')
synchronous()

# Explicitly set the event loop
asyncio.set_event_loop(asyncio.new_event_loop())
ioloop = asyncio.get_event_loop()

print('Asynchronous:')
# Use asyncio.run() to run the asynchronous code
asyncio.run(asynchronous())

