from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import BOT_NAME, BOT_USERNAME, GROUP_SUPPORT, OWNER_NAME, UPDATES_CHANNEL
from helpers.decorators import sudo_users_only
from helpers.filters import command

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ **Welcome {message.from_user.mention} Sweet Heart How Are You!** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Aɢᴀʀ ᴀᴘᴋᴏ ᴠᴄ ᴘᴇʏ sᴏɴɢ ᴘʟᴀʏ ᴋᴀʀɴᴇʏ ʜᴀɪɴ ᴛᴏ ᴍᴜᴊʜᴇʏ ᴀᴘɴᴇʏ ɢʀᴏᴜᴘ ᴍᴀɪɴ ʙᴀɴᴀ ᴅᴏ ᴠᴄ ʀɪɢʜᴛ ᴋᴇʏ sᴀᴛʜ ᴀᴜʀ /play ᴋɪ ᴄᴏᴍᴍᴀɴᴅ ᴅᴀʟᴀɪɴ ᴀɢᴀʀ ғɪʀ ʙʜɪ ɪssᴜ ʜᴀɪ ᴛᴏ ᴍᴇʀʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ sᴇʏ ᴄᴏɴᴛᴀᴄᴛ ᴋᴀʀᴀɪɴ 👉 @Dr_Asad_Ali!.**

 👨‍🔧 **Tʜɪs ᴡɪʟʟ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ ᴏɴ ʏᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠᴄ ᴄʜᴀᴛ ᴀɴʏ ɪssᴜᴇ ʀᴜɴ /help ᴄᴏᴍᴍᴀɴᴅs.!**

💡 **Find ᴏᴜᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜɪs ʙᴜᴛᴛᴏɴ..👉 » 📚 Cᴏᴍᴍᴀɴᴅs Bᴜᴛᴛᴏɴ 📚 **

❔ **How ᴛᴏ ᴜsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜɪs ʙᴜᴛᴛᴏɴ...👉  » ❓ Bᴀsɪᴄ Gᴜɪᴅᴇ Button!**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ Gʀᴏᴜᴘ ⚙️",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("👩‍💻 Bᴀsɪᴄ Gᴜɪᴅᴇ👩‍💻 ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Cᴏᴍᴍᴀɴᴅs︎ 📚", callback_data="cbcmds"),
                    InlineKeyboardButton("💝 Oᴡɴᴇʀ 💝", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Gʀᴏᴜᴘ 👥︎", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Cʜᴀɴɴᴇʟ 📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "👑 Kɪɴɢ 👑", url="https://t.me/Dr_Asad_Ali"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    
    keyboard=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ Gʀᴏᴜᴘ ✨︎", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Cʜᴀɴɴᴇʟ 📣︎", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ]
            ]
        )
    
    alive = f"★ ʙᴏᴛ : [ᴡᴏʀᴋɪɴɢ](https://t.me/rocks_music_bot)\n★ ᴅᴀᴛᴀʙᴀsᴇ : [ᴡᴏʀᴋɪɴɢ](https://t.me/Shayri_Music_Lovers)\n✨ ᴜᴘᴛɪᴍᴇ: `{uptime}`\n★ ʙᴏᴛ : [ᴅᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/Dr_Asad_Ali)"
    
    await message.reply_photo(
        photo="https://telegra.ph/file/86e7cc4fb3033dfddcc0a.png",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **Hello Sweet Heart ❣️ How Are You** {message.from_user.mention()}</b>

**Yᴏᴜ ᴄᴀɴ ғɪɴᴅ ʜᴇʀᴇ sᴇᴠᴇʀᴀʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡɪᴛʜ ʙʀɪᴇғ ᴇxᴘʟᴀɴᴀᴛɪᴏɴ 👇 !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="🤔 Hᴏᴡ ᴛᴏ ᴜsᴇ Mᴇ 🤔", callback_data="cbguide")]]
        ),
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>💡 Hello {message.from_user.mention} Sᴡᴇᴇᴛ Hᴇᴀʀᴛ ❤️ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʜᴇʟᴘ ᴍᴇɴᴜ !</b>

**Yᴏᴜ ᴄᴀɴ ғɪɴᴅ ʜᴇʀᴇ sᴇᴠᴇʀᴀʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡɪᴛʜ ʙʀɪᴇғ ᴇxᴘʟᴀɴᴀᴛɪᴏɴ 👇**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 Bᴀsɪᴄ Cᴍᴅ 📚", callback_data="cbbasic"),
                    InlineKeyboardButton("📕 Aᴅᴠᴀɴᴄᴇᴅ Cᴍᴅ 📕", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("📘 Aᴅᴍɪɴ Cᴍᴅ 📘", callback_data="cbadmin"),
                    InlineKeyboardButton("📗 Sᴜᴅᴏ Cᴍᴅ 📗", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("📙 Oᴡɴᴇʀ Cᴍᴅ 📙", callback_data="cbowner")],
                [InlineKeyboardButton("📔 Fᴜɴ Cᴍᴅ 📔", callback_data="cbfun")],
            ]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ᴍs`\n" f"⚡️ Bʏ Asᴀᴅ Aʟɪ` ")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 **Bot Status**:\n"
        f"• **Uᴘᴛɪᴍᴇ:** `{uptime}`\n"
        f"• **Sᴛᴀʀᴛ Tɪᴍᴇ:** `{START_TIME_ISO}`"
    )
