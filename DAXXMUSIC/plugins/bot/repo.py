from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ωεℓ¢σмє ƒσя 𝚍𝚊𝚡𝚡 яєρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/LofiUpdates"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/LofiOwner"),
          ],
               [
                InlineKeyboardButton("𝐓𝐞𝐚𝐦 𝐋𝐨𝐟𝐢", url="https://t.me/TeamLofi"),

],
[
              InlineKeyboardButton("𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url=f"https://t.me/LofiUpdates"),
              InlineKeyboardButton("︎𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url=f"https://t.me/LofiSupports"),
              ],
              [
              InlineKeyboardButton("𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧︎", url=f"https://github.com/TeamLofi/TeamLofi"),
InlineKeyboardButton("𝐋𝐨𝐟𝐢 𝐁𝐨𝐭", url=f"https://t.me/LofiMuisxcBot"),
],
[
InlineKeyboardButton("𝐒𝐭𝐫𝐢𝐧𝐠𝐆𝐞𝐧𝐁𝐨𝐭", url=f"https://t.me/String_Genertor_bot"),
InlineKeyboardButton("𝐒𝐞𝐬𝐬𝐢𝐨𝐧𝐇𝐚𝐜𝐤𝐁𝐨𝐭", url=f"https://t.me/Sesssion_hack_bot"),
],
[
              InlineKeyboardButton("𝐓𝐞𝐚𝐦𝐋𝐨𝐟𝐢", url=f"https://t.me/TeamLofi"),
              InlineKeyboardButton("𝐓𝐞𝐚𝐦𝐋𝐨𝐟𝐢", url=f"https://t.me/TeamLofi"),
              ],
              [
              InlineKeyboardButton("𝐓𝐞𝐚𝐦𝐋𝐨𝐟𝐢", url=f"https://t.me/TeamLofi"),
InlineKeyboardButton("𝐓𝐞𝐚𝐦𝐋𝐨𝐟𝐢", url=f"https://t.me/TeamLofi"),
],
[
InlineKeyboardButton("𝐓𝐞𝐚𝐦𝐋𝐨𝐟𝐢", url=f"https://t.me/TeamLofi"),
InlineKeyboardButton("𝐓𝐞𝐚𝐦𝐋𝐨𝐟𝐢", url=f"https://t.me/TeamLofi"),
],
[
InlineKeyboardButton("𝐓𝐞𝐚𝐦𝐋𝐨𝐟𝐢", url=f"https://t.me/TeamLofi"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/o7ugdm.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/TeamLofi/KiyomiRobo/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/TeamLofi/KiyomiRobo) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/TeamLofi)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
