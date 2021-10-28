from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from config import BOT_USERNAME

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"💕Hi there, This is a music assistant service\n**❗️ Rules:**\n👉..No chatting allowed.\n👉..No spam allowed.\n✨𝗜 𝗖𝗮𝗻𝗻𝗼𝘁 𝗖𝗵𝗮𝘁 𝗛𝗲𝗿𝗲 𝗣𝗹𝗲𝗮𝘀𝗲 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗧𝗼 𝗠𝘆 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 @Dr_Asad_Ali🌟")
  return                       
