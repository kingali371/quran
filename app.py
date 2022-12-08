import asyncio, os, threading

from pyrogram import Client

from pytgcalls import PyTgCalls 

from pytgcalls import idle

from pytgcalls import StreamType

from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped

from pytgcalls.types.input_stream.quality import HighQualityAudio,    HighQualityVideo,    LowQualityVideo,    MediumQualityVideo

from pytube import YouTube

import aiohttp

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

from flask import Flask

site = Flask(__name__)
call_py = PyTgCalls(app)

@site.route("/")
def hello():
  return "Hi"

async def main ():
  await call_py.start()
  threading.Thread(target=site.run, daemon=True).start()
  print("✅")
  while True:
   await call_py.join_group_call(CHAT_ID,AudioPiped("https://bit.ly/3OWfmUp"),stream_type=StreamType().pulse_stream,)
   await asyncio.sleep(82753+10)

asyncio.run(main())
