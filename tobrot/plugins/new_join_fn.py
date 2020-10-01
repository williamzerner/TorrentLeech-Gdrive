#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram


from tobrot import (
    AUTH_CHANNEL
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    await message.reply_text("

    /gclone: This command is used to clone gdrive files or folder using gclone.

     Syntax:- `[ID of the file or folder][one space][name of your folder only(If the id is of file, don't put anything)]` and then reply /gclone to it.

    /log: This will send you a txt file of the logs.

    /ytdl: This command should be used as reply to a supported link

    /pytdl: This command will download videos from youtube playlist link and will upload to telegram.

    /ytdl gdrive: This will download and upload to your cloud.

    /pytdl gdrive: This download youtube playlist and upload to your cloud.

    /leech: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [this command will SPAM the chat and send the downloads a seperate files, if there is more than one file, in the specified torrent]

    /leech archive: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [This command will create a .tar.gz file of the output directory, and send the files in the chat, splited into PARTS of 1024MiB each, due to Telegram limitations]

    /gleech: This command should be used as reply to a magnetic link, a torrent link, or a direct link. And this will download the files from the given link or torrent and will upload to the cloud using rclone.

    /gleech archive This command will compress the folder/file and will upload to your cloud.

    /leech unzip: This will unzip the .zip file and dupload to telegram.

    /gleech unzip: This will unzip the .zip file and upload to cloud.

    /leech unrar: This will unrar the .rar file and dupload to telegram.

    /gleech unrar: This will unrar the .rar file and upload to cloud.

    /leech untar: This will untar the .tar file and upload to telegram.

    /gleech untar: This will untar the .tar file and upload to cloud..

    /tleech: This will mirror the telegram files to ur respective cloud cloud.

    /tleech unzip: This will unzip the .zip telegram file and upload to cloud.

    /tleech unrar: This will unrar the .rar telegram file and upload to cloud.

    /tleech untar: This will untar the .tar telegram file and upload to cloud.

    /getsize: This will give you total size of your destination folder in cloud.

    /renewme: This will clear the remains of downloads which are not getting deleted after upload of the file or after /cancel command.

    [Only work with direct link and youtube link for now]It is like u can add custom name as prefix of the original file name. Like if your file name is gk.txt uploaded will be what u add in CUSTOM_FILE_NAME + gk.txt

Only works with direct link/youtube link.No magnet or torrent.

And also added custom name like...

You have to pass link as www.download.me/gk.txt | new.txt

the file will be uploaded as new.txt.", quote=True)
    # channel_id = str(AUTH_CHANNEL)[4:]
    # message_id = 99
    # display the /help
    
    #await message.reply_text("""join this group forr help-- @GbotStoreSupport\n\n And also don't forget to fork this repo: <a href="https://github.com/gautamajay52/TorrentLeech-Gdrive">TorrentLeech-Gdrive</a>""", disable_web_page_preview=True)


async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="read this?",
            url="https://t.me/keralagram/698909"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "please use @renamebot",
        quote=True,
        reply_markup=reply_markup
    )
