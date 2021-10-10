import asyncio

from callsmusic.callsmusic import client as USER
from config import BOT_USERNAME, SUDO_USERS
from helpers.decorators import authorized_users_only, errors
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant


@Client.on_message(
    command(["join", f"join@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b> 𝗜 𝗗𝗼𝗻'𝘁 𝗛𝗮𝘃𝗲 𝗣𝗲𝗿𝗺𝗲𝘀𝘀𝗶𝗼𝗻\n\n» ❌ __𝗔𝗱𝗱 𝗨𝘀𝗲𝗿𝘀__</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "music assistant"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(
            message.chat.id, "🤖: 𝗜 𝗛𝗮𝘃𝗲 𝗝𝗼𝗶𝗻𝗱 𝗛𝗲𝗿𝗲 𝗧𝗼 𝗣𝗹𝗮𝘆 𝗠𝘂𝘀𝗶𝗰 𝗢𝗻 𝗩𝗖 𝗖𝗵𝗮𝘁 "
        )
    except UserAlreadyParticipant:
        await message.reply_text(
            f"<b>✅ 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗜𝗻 𝗖𝗵𝗮𝘁</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 𝗙𝗹𝗼𝗼𝗱 𝗘𝗿𝗿𝗼𝗿 𝗕𝗮𝘀 𝗞𝗮𝗿 𝗗𝗼 𝗕𝗲𝗵𝗻𝗰𝗵𝗼 🛑 \n\n User {user.first_name} 𝗖𝗼𝘂𝗹𝗱𝗻'𝘁 𝗝𝗼𝗶𝗻 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝗗𝘂𝗲 𝗧𝗼 𝗛𝗲𝗮𝘃𝘆 𝗝𝗼𝗶𝗻 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗙𝗼𝗿 𝗨𝘀𝗲𝗿𝗯𝗼𝘁."
            "\n\n 𝗢𝗿 𝗠𝗮𝗻𝘂𝗮𝗹𝗹𝘆 𝗔𝗱𝗱  @{ASSISTANT_NAME}  𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝗔𝗻𝗱 𝗧𝗿𝘆 𝗔𝗴𝗮𝗶𝗻</b>",
        )
        return
    await message.reply_text(
        f"<b>✅ 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗝𝗼𝗶𝗻 𝗧𝗵𝗲 𝗖𝗵𝗮𝘁t</b>",
    )


@Client.on_message(
    command(["leave", f"leave@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
@authorized_users_only
async def rem(client, message):
    try:
        await USER.send_message(message.chat.id, "✅ 𝗝𝗮 𝗥𝗮𝗵𝗮 𝗛𝗼𝗻 𝗠𝗮𝗶𝗻 𝗚𝗿𝗼𝘂𝗽 𝗖𝗵𝗵𝗼𝗱 𝗞𝗲𝘆")
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            "<b>𝗨𝘀𝗲𝗿 𝗖𝗼𝘂𝗹𝗱𝗻'𝘁 𝗟𝗲𝗮𝘃𝗲 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽, 𝗠𝗮𝘆 𝗙𝗹𝗼𝗼𝗱𝘄𝗮𝗶𝘁 𝗘𝗿𝗿𝗼𝗿.\n\n 𝗞𝗶𝗰𝗸 𝗠𝗲 𝗠𝗮𝗻𝘂𝗮𝗹𝗹𝘆</b>"
        )

        return


@Client.on_message(command(["leaveall", f"leaveall@{BOT_USERNAME}"]))
async def bye(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **userbot** leaving all chats !")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"Userbot leaving all group...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        except:
            failed += 1
            await lol.edit(
                f"Userbot leaving...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        await asyncio.sleep(0.7)
    await client.send_message(
        message.chat.id, f"Left {left} chats.\nFailed {failed} chats."
    )


@Client.on_message(
    command(["joinchannel", "ubjoinc"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
        conchat = await client.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except:
        await message.reply(
            "❌ `NOT_LINKED`\n\n• **The userbot could not play music, due to group not linked to channel yet.**"
        )
        return
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>• 𝗜 𝗗𝗼𝗻'𝘁 𝗛𝗮𝘃𝗲 𝗣𝗲𝗿𝗺𝗲𝘀𝘀𝗶𝗼𝗻\n\n» ❌ __𝗔𝗱𝗱 𝗨𝘀𝗲𝗿𝘀__</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "helper"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(
            message.chat.id, "🤖: 𝗜 𝗛𝗮𝘃𝗲 𝗝𝗼𝗶𝗻𝗱 𝗛𝗲𝗿𝗲 𝗧𝗼 𝗣𝗹𝗮𝘆 𝗠𝘂𝘀𝗶𝗰 𝗢𝗻 𝗩𝗖"
        )
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>✅ 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗜𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑\n\n**userbot couldn't join to channel** due to heavy join requests for userbot, make sure userbot is not banned in channel."
            f"\n\nor manually add @{ASSISTANT_NAME} to your channel and try again</b>",
        )
        return
    await message.reply_text(
        "<b>✅ 𝗠𝗮𝗶𝗻 𝗔𝗮 𝗚𝗮𝘆𝗮 𝗔𝗽𝗸𝗲𝘆 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗠𝗮𝗶𝗻</b>",
    )
