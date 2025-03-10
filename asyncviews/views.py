import asyncio
from time import sleep
import httpx
from django.http import HttpResponse

async def http_call_async():
    for num in range(1,6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        response = await client.get('https://httpbin.org')
        print(response)

def http_call_sync():
    for num in range(1,6):
        sleep(1)
        print(num)
    response = httpx.get('https://httpbin.org')
    print(response)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('Non-blocking HTTP request')

def sync_view(request):
    http_call_sync()
    return HttpResponse('Blocking HTTP request')

def home_view(request):
    return HttpResponse('<h1>Async views exercise in Django</h1><ul><li><a href="/sync">Sync Request</a></li><li><a href="/async">Async Request</a></li></ul>')