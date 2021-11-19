### PARALLEL PROCESSING at kernel level (see screenshot); 
###     context switches when there is a wait (or process taking time)
import asyncio

async def upload():
    print('Started uploading process')
    # await actual_upload_long_process()
    await asyncio.sleep(5) # fake upload; await tells main thread to wait. Handled by Event Loop
    print('upload done')

async def download():
    print('Started downloading process')
    await asyncio.sleep(4) #  
    print('download done')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # task()
    loop.run_until_complete(asyncio.gather(upload(), download()))
    print('All done')