# Copyright (C) 2021 By AmortMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **مرحبآ عزيزي↤「 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 」!**\n
🤖 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) **
** ◈︙يتيح لك تشغيل الموسيقى والفيديو في مجموعات . **
◈︙ ** ◈︙اضفني مشرف مع صلاحيه اضافه مستخدمين .**
🔖 ** ◈︙الحساب المساعد :  @{ASSISTANT_NAME}  **
◈︙المطور : **[{ALIVE_NAME}](https://t.me/{OWNER_NAME}) **
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ اضغط لأضافه البوت لمجموعتك ›",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("‹ طــريــقــة الاســتخــدام ›", callback_data="cbhowtouse")],
                [InlineKeyboardButton("‹ الاوامــر الكامله المعربــه ›", callback_data="cbvamp")],                
                [
                    InlineKeyboardButton("‹ الاوامــــر ›", callback_data="cbcmds"),
                    InlineKeyboardButton("‹ الــمطــور ›", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "‹ جــروب الــدعـم ›", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "‹ 𝐒𝐎𝐔𝐑𝐂𝐄 ›", url=f"https://t.me/AOOOU"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        ALIVE_NAME, url=f"https://t.me/{OWNER_NAME}"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" ◈︙الدليل الأساسي لاستخدام هذا البوت:

 1 ↤ أولاً ، أضفني إلى مجموعتك .
 ↤ بعد ذلك ، قم بترقيتي كمشرف ومنح جميع الصلاحيات باستثناء الوضع الخفي .
 ↤ بعد ترقيتي ، اكتب «تحديث» او /reload مجموعة لتحديث بيانات المشرفين .
3 ↤ أضف  @{ASSISTANT_NAME} إلى مجموعتك أو اكتب او «انضم»  /userbotjoin لدعوة حساب المساعد .
4 ↤ قم بتشغيل المكالمة  أولاً قبل البدء في تشغيل الفيديو / الموسيقى .
5 ↤ في بعض الأحيان ، يمكن أن تساعدك إعادة تحميل البوت باستخدام الأمر «تحديث» او /reload في إصلاح بعض المشكلات .
◈︙إذا لم ينضم البوت إلى المكالمة ، فتأكد من تشغيل المكالمة  بالفعل ، أو اكتب «غادر» /userbotleave ثم اكتب «انضم» او /userbotjoin مرة أخرى .

› إذا كانت لديك أسئلة  حول هذا البوت ، فيمكنك إخبارنا منن خلال مجموعه الدعم الخاصة بي هنا ↤ @{GROUP_SUPPORT}

◈︙قناة البوت @AOOOU .
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(" ‹ رجوع › ", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""› **Hello :  [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) .

◈︙قم بالضغط علي الزر الذي تريده لمعرفه الاوامر لكل فئه منهم .

◈︙قناة البوت »  @AOOOU  .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("‹ اوامــر المشــرف ›", callback_data="cbadmin"),
                    InlineKeyboardButton("‹ اوامــر المطــور ›", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("‹ الاوامــر الكامله المعربــه ›", callback_data="cbvamp")                    
                ],[
                    InlineKeyboardButton("‹ رجوع ›", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""◈︙ها هي الأوامر الاساسية :

» /mplayاو «تشغيل» 「اسم الأغنية / رابط تشغيل الصوت mp3
» /vplay او «فديو» 「اسم / رابط الفيديو」 تشغيل الفيديو داخل المكالمة 
» /stream او«تشغيل» 「رابط 」تشغيل صوت
» /vstream او «فديو» 「رابط」 تشغيل فيديو مباشر من اليوتيوب
» /stop  او «ايقاف» لايقاف التشغيل
» /resume «او لاستئناف التشغيل«مواصله  
» /skip  او «تقدم» تخطي الئ التالي
» /pauseاو «وقف» ايقاف التشغيل موقتآ
» /vmute «لكتم البوت او «كتم
» /vunmute«او «الغاء الكتم لرفع الكتم عن البوت

◈︙قناة البوت @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("‹ رجوع ›", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""  »
 » /playlist  او «تحكم» ↤ تظهر لك قائمة التشغيل
 » /videoاو «تنزيل» + الاسم  تنزيل فيديو من youtube
 » /song +  او« تحميل» الاسم تنزيل صوت من youtube
» /volume  او «الصوت»+ الرقم لضبط مستوئ الصوت
» /reload  او «تحديث» لتحديث البوت و قائمة المشرفين
» /userbotjoin  او «انضم» لاستدعاء حساب المساعد
» /userbotleave  او «غادر» لطرد حساب المساعد 
 » /pingاو«تيست» - إظهار حالة البوت بينغ
 » /alive   او «السورس» إظهار معلومات البوت  (في المجموعه) 
  قناة البوت @{UPDATES_CHANNEL}
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("‹ رجوع ›", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

» /rmw  »او «مسح- clean all raw files
» /rmd  » او «تنظيف- clean all downloaded files
» /sysinfo»او «معلومات- show the system information
» /update»او «ترقيه - update your bot to latest version
» /restart «او «تنصيب - restart your bot
» /leaveall»او «غادرالجميع - order userbot to leave from all group

 ◈︙قناة البوت @{UPDATES_CHANNEL}
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("‹ رجوع ›", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbvamp"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""◈︙ها هي الاوامر  الكامله بالعربي: 
الاوامر المعربه تكتب كما هي بدون شرط او اي شيء
━━━━━━━━━━━━
◈︙تشغيل + 「اسم الأغنية او / رابط」تشغيل الصوت  mp3

◈︙فديو +  「اسم الفديو او / رابط الفيديو」 تشغيل الفيديو داخل المكالمة  .

◈︙فيديو + لينك + | جودة < 360 - 480- 720 >| » » تشغيل فيديو مباشر من يوتيوب .

◈︙ايقاف او انهاء » »  لايقاف التشغيل .

◈︙قف » » ايقاف التشغيل موقتآ  .

◈︙استئناف  » »  استئناف التشغيل  .

◈︙تخطي » » تخطي الئ التالي  .

◈︙ كتم او ميوت  » »   لكتم البوت .

◈︙الغاء الكتم » »  لرفع كتم البوت  .
━━━━━━━━━━━━
◈︙تحكم » » تظهر لك قائمة التشغيل . 

◈︙تنزيل + اسم فيديو » » لتحميل فيديوهات من يوتيوب .

◈︙تحميل  + اسم اغنية  » لتحميل اغاني mP3 من يوتيوب .  

◈︙بحث » »  اي شيء تريد البحث عنه باليوتيوب .

◈︙الصوت + < رقم 1 - 200 >  » »  الرقم لضبط مستوئ الصوت .

◈︙تحديث » » لتحديث البوت و قائمة المشرفين .

◈︙انضم » »  لاستدعاء حساب المساعد .

◈︙غادر » »  لطرد حساب المساعد .

◈︙تيست او بينج » »  إظهار حالة البوت بينج .

◈︙الوقت » » اظهار الوقت تشغيل البوت . 

◈︙السورس » »  إظهار معلومات البوت . 

◈︙المطور » »  إظهار مطورين البوت .

━━━━━━━━━━━━
◈︙الاوامر او اوامراغاني او اغاني » » لعرض قائمه الاوامر في مجموعتك 
◈︙اوامر  المطور ⌯

◈︙مسح » » لمسح جميع الملفات المستخدمه .

◈︙تنضيف » »  لتنظيف جميع الملفات المحمله .

◈︙معلومات » » لرؤيه معلومات النظام  البوت .

◈︙ترقيه » » لتحديث البوت لاخر اصدار من السورس .

◈︙ريستارت » لاعادة تشغيل البوت .

◈︙غادرالجميع  » » لمغادره الحساب المساعد لجميع جروبات .
━━━━━━━━━━━━━━
 قناة السورس » @{UPDATES_CHANNEL}
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("‹ رجوع ›", callback_data="cbcmds")]]
        ),
    )
           

@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("◈︙المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الإعدادات** {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("‹ اغلاق ›", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("‹ قائمة التشغيل فارغه ›", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("◈︙ المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()
