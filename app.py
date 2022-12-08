import asyncio, os, threading

from server import web_server

from pyrogram import Client

from pytgcalls import PyTgCalls 

from pytgcalls import idle

from pytgcalls import StreamType

from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped

from pytgcalls.types.input_stream.quality import HighQualityAudio,    HighQualityVideo,    LowQualityVideo,    MediumQualityVideo


import aiohttp

from aiohttp import web

from Python_ARQ import ARQ

from pyrogram.types import Message

ARQ_API_KEY = "HMPXNS-BDPCCB-UJKRPU-OQADHG-ARQ"

aiohttpsession = aiohttp.ClientSession()

arq = ARQ("https://thearq.tech", ARQ_API_KEY, aiohttpsession)

API_ID = int(os.getenv("API_ID"))
CHAT_ID = int(os.getenv("CHAT_ID"))
API_HASH = os.getenv("API_HASH")


SESSION = os.getenv("SESSION")

app = Client(

    "MyBot",

    api_id=API_ID,

    api_hash=API_HASH,
    
    session_string=SESSION

)

call_py = PyTgCalls(app)
PORT = "8080"

async def main ():
  await call_py.start()
  app = web.AppRunner(await web_server())
  await app.setup()
  bind_address = "0.0.0.0"
  await web.TCPSite(app, bind_address, PORT).start()
  print("🎉✅🎉")
  while True:
   await call_py.join_group_call(CHAT_ID,AudioPiped("https://bit.ly/3OWfmUp"),stream_type=StreamType().pulse_stream,)
   await asyncio.sleep(82753+10)

asyncio.run(main())
