from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from config import BOT_USERNAME

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"ð ðð¼ð»'ð ðð®ðð² ð§ð¶ðºð² ð§ð¼ ððµð®ð ðªð¶ððµ ð¬ð¼ð ..ðð¼ð ð This is a music assistant service\n**âï¸ Rules:**\nð..No chatting allowed.\nð..No spam allowed.\nâ¨ð ðð®ð»ð»ð¼ð ððµð®ð ðð²ð¿ð² ð£ð¹ð²ð®ðð² ðð¼ð»ðð®ð°ð ð§ð¼ ð ð ðð²ðð²ð¹ð¼ð½ð²ð¿ @Dr_Asad_Alið")
  return                       
