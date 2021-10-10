from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from config import BOT_USERNAME

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"💕𝗛𝗲𝗿𝗲 𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝗰𝗲 𝗢𝗳 @{BOT_USERNAME}\n✨𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 @Dr_Asad_Ali\n🌟𝗗𝗼𝗻𝘁 𝗦𝗽𝗮𝗺 𝗛𝗲𝗿𝗲")
  return                        
