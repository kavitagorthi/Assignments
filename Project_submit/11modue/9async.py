import webbrowser, sys
from urllib.request import urlopen
import asyncio
import threading


def thr(i):
    # we need to create a new loop for the thread, and set it as the 'default'
    # loop that will be returned by calls to asyncio.get_event_loop() from this
    # thread.
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(do_stuff(i))
    loop.close()


async def do_stuff(i):
    await asyncio.sleep(2)  # NOTE if we hadn't called
    # asyncio.set_event_loop() earlier, we would have to pass an event
    # loop to this function explicitly.

    webbrowser.open('http://inventwithpython.com/')
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    print(html.read())
    print(i)


def main():
    num_threads = 10
    threads = [threading.Thread(target=thr, args=(i,)) for i in range(num_threads)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print("bye")


if __name__ == "__main__":
    main()

