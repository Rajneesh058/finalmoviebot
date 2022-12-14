import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    START_TXT = """
<i>ð Há´Ê,</i>{}\n
<i>I'á´ á´á´Êá´É¢Êá´á´ á´á´á´ Éªá´ð­ ê°ÉªÉ´á´á´Ê & á´á´á´á´ ê°ÉªÊá´á´Ê Êá´á´ð¤</i>\n
<i>CÊÉªá´á´ á´É´ Há´Êá´ð á´á´ É¢á´á´ á´á´Êá´ ÉªÉ´Òá´Êá´á´á´Éªá´É´</i>n\

<i><b>á´á´ÉªÉ´á´á´ÉªÉ´á´á´ ÊÊ : @Rajneesh_Singh_Tomar</b>"""


<i>Aá´á´ á´á´ á´á´ Êá´á´Ê É¢Êá´á´á´ á´á´ sá´á´ á´Êá´ á´á´É¢Éªá´ á´Ê Êá´á´á´ á´á´Êá´ ÒÊá´á´ á´Êá´ á´á´É´á´ Êá´Êá´á´¡</i>''')
    HELP_TXT = """ð {}
ð·ð´ðð´ ð¸ð ðð·ð´ ð·ð´ð»ð¿ ðµð¾ð ð¼ð ð²ð¾ð¼ð¼ð°ð½ð³."""
    ABOUT_TXT = """<b><i>ð¤ á´Ê É´á´á´á´ : <a href=https://t.me/Search_zone_bot><b>Search Bot</b></a>\n
ð¨âð» á´á´á´ á´Êá´á´á´Ê : <a href=https://t.me/GreyMatter_Owner><b>GreyMatter</b></a>\n
ð Êá´É´É¢á´á´É¢á´ : á´ÊÊá´É¢Êá´á´\n
ð ê°Êá´á´á´á´¡á´Êá´ : á´Êá´Êá´É´ 3\n
ð¡ Êá´sá´á´á´ á´É´ : VPS\n
ð¢ á´á´á´á´á´á´s á´Êá´É´É´á´Ê : <a href=https://t.me/GreyMatter_Bots><b></b>á´ÊÉªá´á´ Êá´Êá´</a>\n
ð á´ á´ÊsÉªá´É´ : á´  4.0\n</b></i>"""
    SOURCE_TXT = """<b>NOTE:</b>
- <b>FP BOT is a open source project. 
- Source ð <a href=https://t.me/Rajneesh_Singh_Tomar>CLICK HERE</a></b>

<b>DEVS:</b>
- <a href=https://t.me/Rajneesh_Singh_Tomar>Rajneesh_Singh_Tomar</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and FP Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. FILMY PITARA have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¢ /filter - <code>add a filter in chat</code>
â¢ /filters - <code>list all the filters of a chat</code>
â¢ /del - <code>delete a specific filter in chat</code>
â¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- FP Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. FP Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Rajneesh_Singh_Tomar)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¢ /connect  - <code>connect a particular chat to your PM</code>
â¢ /disconnect  - <code>disconnect from a chat</code>
â¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Search Bot

<b>Commands and Usage:</b>
â¢ /id - <code>get id of a specified user.</code>
â¢ /info  - <code>get information about a user.</code>
â¢ /imdb  - <code>get the film information from IMDb source.</code>
â¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â¢ /logs - <code>to get the rescent errors</code>
â¢ /stats - <code>to get status of files in db.</code>
â¢ /delete - <code>to delete a specific file from db.</code>
â¢ /users - <code>to get list of my users and ids.</code>
â¢ /chats - <code>to get list of the my chats and ids </code>
â¢ /leave  - <code>to leave from a chat.</code>
â¢ /disable  -  <code>do disable a chat.</code>
â¢ /ban  - <code>to ban a user.</code>
â¢ /unban  - <code>to unban a user.</code>
â¢ /channel - <code>to get list of total connected channels</code>
â¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â ðð¾ðð°ð» ðµð¸ð»ð´ð: <code>{}</code>
â ðð¾ðð°ð» ððð´ðð: <code>{}</code>
â ðð¾ðð°ð» ð²ð·ð°ðð: <code>{}</code>
â ððð´ð³ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±
â ðµðð´ð´ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±"""
    LOG_TEXT_G = """#ððð°ðð«ð¨ð®ð©
    
<b>áâº ðð«ð¨ð®ð© âª¼ {}(<code>{}</code>)</b>
<b>áâº ðð¨ð­ðð¥ ððð¦ððð«ð¬ âª¼ <code>{}</code></b>
<b>áâº ððððð ðð² âª¼ {}</b>
"""
    LOG_TEXT_P = """#ððð°ðð¬ðð«  
    
<b>áâº ðð - <code>{}</code></b>
<b>áâº ððð¦ð - {}</b>
"""
START_TXT = """
<i>ð Há´Ê,</i>{}\n
<i>I'á´ á´á´Êá´É¢Êá´á´ á´á´á´ Éªá´ð­ ê°ÉªÉ´á´á´Ê & á´á´á´á´ ê°ÉªÊá´á´Ê Êá´á´ð¤</i>\n
<i>CÊÉªá´á´ á´É´ Há´Êá´ð á´á´ É¢á´á´ á´á´Êá´ ÉªÉ´Òá´Êá´á´á´Éªá´É´</i>n\

<i><b>á´á´ÉªÉ´á´á´ÉªÉ´á´á´ ÊÊ : @Rajneesh_Singh_Tomar</b>"""

    GHHM_TXT = """<b>ð Thanks For Your Support...

ð©ððð ð ð½ð½ ð®ðð ð¡ðð ð³ð ð¸ððð ð¦ðððð ð ð ð ð½ððð, ð¨ð ð¶ððð ð¯ððððð½ð¾ ð¬ðððð¾ð ð³ðð¾ðð¾... ð


     âï¸ ðð²ð®ððð¿ð²ð âï¸

ð AutoFilter, Manual Filter
ð IMDb HD Posters
ð IMDb Real Details
ð Two Buttons Mode
ð Force Subscribe
ð Extra Features: download songs, download you tube video, URL Shortner,  

â More Features Adding Soon</b> ð"""

    GHHN_TXT = """Extra features"""
    URLSHORT_TXT = """<b>â¤ ððð¥ð©: ð´ðð ððððððð¾ð

ðððð ððððððð ððððð ð¢ðð ðð ððððð ð ððð 

â¤ ðð¨ð¦ð¦ðð§ðð¬ ðð§ð ðð¬ðð ð:

âª /short: ððð¾ ðððð ð¼ððððºðð½ ðððð ðððð ðððð ðð ðð¾ð ðððððð¾ð½ ððððð

âð¤ððºðððð¾:
/short https://t.me/+veUIdIW2CQ5GU5</b>"""


    URLSHORTN_TXT = """<b>â¤ ððð¥ð©: ð´ðð ððððððð¾ð

ðððð ððððððð ððððð ð¢ðð ðð ððððð ð ððð 

â¤ ðð¨ð¦ð¦ðð§ðð¬ ðð§ð ðð¬ðð ð:

âª /short: ððð¾ ðððð ð¼ððððºðð½ ðððð ðððð ðððð ðð ðð¾ð ðððððð¾ð½ ððððð

âð¤ððºðððð¾:
/short https://t.me/+veUIdIW25mOGU5</b>"""

    VIDEO_TXT ="""<b>ð·ð´ð»ð¿ ðð¾ð ðð¾ ð³ð¾ðð½ð»ð¾ð°ð³ ðð¸ð³ð´ð¾ ðµðð¾ð¼ ðð¾ðððð±ð´.

â¢ ðð´ð¢ð¨ð¦
ð ð°ð¶ ðð¢ð¯ ðð°ð¸ð¯ð­ð°ð¢ð¥ ðð¯ðº ððªð¥ð¦ð° ðð³ð°ð® ð ð°ð¶ðµð¶ð£ð¦

ðð¤ð¬ ðð¤ ðð¨ð
â¢ ððºð±ð¦ /video or /mp4 ðð¯ð¥ (ððªð¥ð¦ð° Link)
â¢ ðð¹ð¢ð®ð±ð­ð¦:
/ð®ð±4 https://youtu.be/Your Link</b>"""

    VIDEOS_TXT ="""<b>ð·ð´ð»ð¿ ðð¾ð ðð¾ ð³ð¾ðð½ð»ð¾ð°ð³ ðð¸ð³ð´ð¾ ðµðð¾ð¼ ðð¾ðððð±ð´.

â¢ ðð´ð¢ð¨ð¦
ð ð°ð¶ ðð¢ð¯ ðð°ð¸ð¯ð­ð°ð¢ð¥ ðð¯ðº ððªð¥ð¦ð° ðð³ð°ð® ð ð°ð¶ðµð¶ð£ð¦

ðð¤ð¬ ðð¤ ðð¨ð
â¢ ððºð±ð¦ /video or /mp4 ðð¯ð¥ (ððªð¥ð¦ð° Link)
â¢ ðð¹ð¢ð®ð±ð­ð¦:
/ð®ð±4 https://youtu.be/Your Link</b>"""

    YTTHUMB_TXT = """<b>ð·ð´ð»ð¿ð ðð¾ ð³ð¾ðð½ð»ð¾ð°ð³ ð°ð½ð ðð¾ðððð±ð´ ðð¸ð³ð´ð¾ ðð·ðð¼ð±ð½ð°ð¸ð»
    
â­ðð¤ð¬ ðð¤ ðð¨ð
ððºð±ð¦ /ytthumb ðð¯ð¥ ððªð¥ð¦ð° ððªð¯ð¬

â¢ ðð¹ð¢ð®ð±ð­ð¦
/ytthumb https://youtu.be/yourlink</b>"""

    SONG_TXT = """<b>ðð¾ð½ð¶ ð³ð¾ðð½ð»ð¾ð°ð³ ð¼ð¾ð³ðð»ð´...

ðð¾ð½ð¶ ð³ð¾ðð½ð»ð¾ð°ð³ ð¼ð¾ð³ðð»ð´, ðµð¾ð ðð·ð¾ðð´ ðð·ð¾ ð»ð¾ðð´ ð¼ððð¸ð². ðð¾ð ð²ð°ð½ ððð´ ðð·ð¸ð ðµð´ð°ððð´ ðµð¾ð ð³ð¾ðð½ð»ð¾ð°ð³ ð°ð½ð ðð¾ð½ð¶ ðð¸ðð· ððð¿ð´ð ðµð°ðð ðð¿ð´ð´ð³.ðð¾ððºð ð¾ð½ð»ð ð¾ð½ ð¶ðð¾ðð¿ð..

<ð²ð¾ð¼ð¼ð°ð½ð³ð

âºâº  /song ðð¾ð½ð¶ ð½ð°ð¼ð´ 

ðð¾ððºð ð¾ð½ð»ð ð¾ð½ ð¶ðð¾ðð¿

ð²ðð´ð³ð¸ðð :- <a href=https://t.me/Rajneesh_Singh_Tomar>Rajneesh_Singh_Tomar </b></a>"""


    FILESTORE_TXT = """â¤ ððð¥ð©: ðð¢ð¥ð ðð­ð¨ð«ð ðð¨ðð®ð¥ð../

<b>ð±ð ððð¸ð½ð¶ ðð·ð¸ð ð¼ð¾ð³ðð»ð´ ðð¾ð ð²ð°ð½ ððð¾ðð´ ðµð¸ð»ð´ð ð¸ð½ ð¼ð ð³ð°ðð°ð±ð°ðð´ ð°ð½ð³ ð¸ ðð¸ð»ð» ð¶ð¸ðð´ ðð¾ð ð° ð¿ð´ðð¼ð°ð½ð´ð½ð ð»ð¸ð½ðº  ðð¾ ð°ð²ð²ð´ðð ðð·ð´ ðð°ðð´ð³ ðµð¸ð»ð´ð.ð¸ðµ ðð¾ð ðð°ð½ð ðð¾ ð°ð³ð³ ðµð¸ð»ð´ð ðµðð¾ð¼ ð° ð¿ðð±ð»ð¸ð² ð²ð·ð°ð½ð½ð´ð» ðð´ð½ð³ ðð·ð´ ðµð¸ð»ð ð»ð¸ð½ðº ð¾ð½ð»ð  ð¾ð ðð¾ð ðð°ð½ð ðð¾ ð°ð³ð³ ðµð¸ð»ð´ð ðµðð¾ð¼ ð°  ð¿ðð¸ðð°ðð´ ð²ð·ð°ð½ð½ð´ð» ðð¾ð ð¼ððð ð¼ð°ðºð´ ð¼ð´ ð°ð³ð¼ð¸ð½ ð¾ð½ ðð·ð´ ð²ð·ð°ð½ð½ð´ð» ðð¾ ð°ð²ð²ð´ðð ðµð¸ð»ð´ð...//</b>

âª¼ ðð¨ð¦ð¦ðð§ðð¬ ðð§ð ðð¬ðð ð âº

âª /plink âºâº <b>ðð´ð¿ð»ð ðð¾ ð°ð½ð ð¼ð´ð³ð¸ð° ðð¾ ð¶ð´ð ð»ð¸ð½ðº.</b>
âª /pbatch âºâº <b>ððð´ ðð¾ðð ð¼ð´ð³ð¸ð° ð»ð¸ð½ðº ðð¸ðð· ðð·ð¸ð ð²ð¾ð¼ð¼ð°ð½ð³.</b>
âª /batch âºâº <b>ðð¾ ð²ðð´ð°ðð´ ð»ð¸ð½ðº ðµð¾ð ð¼ðð»ðð¸ð¿ð»ð´ ðµð¸ð»ð´ð.</b>

âª¼ ðð±ðð¦ð©ð¥ð âº

<code>/batch https://t.me/gjcjknxz/2 https://t.me/jfksucxhb/8</code>

ð²ðð´ð³ð¸ðð âºâº <a href=https://t.me/Rajneesh_Singh_Tomar>Rajneesh_Singh_Tomar</a></b>"""

    FORCESUB_TXT = """Já´ÉªÉ´  Official á´Êá´É´É´á´Ê á´á´ Proceed ð """
    
    OWNER_TXT = """<b>>ââââá Owner Details áââââ<
    
â­ï¸ FULL NAME : Rajneesh Singh Tomar
â­ï¸ USERNAME: @Rajnesh_Singh_Tomar
â­ï¸PERMANENT DM LINK : <a href=https://t.me/Rajneesh_Singh_Tomar>CLICK Here</a></b>"""

    GROUP_R_TXT = """<b>GROUP RULES

âï¸  Search With Correct Spelling..

âï¸ Try to Search movie With  Year If The bot is Not Sending You Accurate Result..

âï¸ Search Series In The Given From Example : Gotham S03E01 And S03E10..

âï¸ Search Movies  in The Given From Example:    
(1) Avengers.. â
(2) Avengers Hindi. â
(3) Don't Tipe Avengers Hindi Dubbed..â

âï¸Don't Do Any Self Promotion.

âï¸ Don't Send Any Kind Of Photo Video Documents URL ETC.

âï¸ Sending The Above  Mantained Things Will Lead To Permanent Ban.

âï¸Don't Request Any Things Other Than Movie Series Animes.

âï¸ Give and Tak Respect</b>.."""

MALIK_PHH = """<b>Hay ð {}.... ð· â¤ï¸

ð welcome to Our Group...

ð You Can Find ð Movies / Series / Animes etc.</b>"""

ALURT_FND = """<b>.

CHECK YOUR MOVIE ON THE GIVEN LIST AND SELECT YOUR MOVIE.. 

à¤¦à¥ à¤à¤ à¤¸à¥à¤à¥ à¤®à¥à¤ à¤à¤ªà¤¨à¥ à¤«à¤¿à¤²à¥à¤® à¤¦à¥à¤à¥à¤ à¤à¤° à¤à¤ªà¤¨à¥ à¤«à¤¿à¤²à¥à¤® à¤à¥à¤¨à¥à¤</b> ððð"""

ADG = """<b>Hay. {}..\n\nThankyou For Adding Me In.. â£ï¸

             ð <s>{}</s> ð 

If you have any questions & doubts about using me..\n\n Contact my Owner >> @Rajneesh_Singh_Tomar</b>"""

ADDG = """
<i>ð Há´Ê,</i>{}{}\n
<i>I'á´ á´á´Êá´É¢Êá´á´ á´á´á´ Éªá´ð­ ê°ÉªÉ´á´á´Ê & á´á´á´á´ ê°ÉªÊá´á´Ê Êá´á´ð¤</i>\n
<i>CÊÉªá´á´ á´É´ Há´Êá´ð á´á´ É¢á´á´ á´á´Êá´ ÉªÉ´Òá´Êá´á´á´Éªá´É´</i>\n

<i><b>á´á´ÉªÉ´á´á´ÉªÉ´á´á´ ÊÊ : @Rajneesh_Singh_Tomar</b>"""

M_NT_FND = """<b>â­ï¸ This Movie Not Found my Database... \n\nâ­ï¸ Request to admin.. ð</b>"""
