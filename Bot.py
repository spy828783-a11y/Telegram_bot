from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)
import os

BOT_TOKEN = os.getenv("8676660393:AAFwUfe8scNfSAiCCnCkdYKP1hTaT9tJd1M") or "APNA_TOKEN_YAHAN"
CHANNEL_ID = -1004433068331

COUNTER_FILE = "counter.txt"


def get_post_number():
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "w") as f:
            f.write("0")

    with open(COUNTER_FILE, "r") as f:
        return int(f.read())


def save_post_number(num):
    with open(COUNTER_FILE, "w") as f:
        f.write(str(num))


async def setpost(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        num = int(context.args[0])
        save_post_number(num - 1)
        await update.message.reply_text(f"✅ Next post number set to {num}")
    except:
        await update.message.reply_text("Usage: /setpost 500")


async def postno(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current = get_post_number() + 1
    await update.message.reply_text(f"📌 Next Post No: {current}")


async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message or not update.message.video:
        return

    post_no = get_post_number() + 1
    save_post_number(post_no)

    link = (update.message.caption or "").strip()

    caption = f"""Post no - {post_no}

🎥 𝑪𝒍𝒊𝒄𝒌 👉 𝑽𝒊𝒅𝒆𝒐 𝙇𝒊𝒏𝒌👇👇

{link}

😈Must watch Guys😈
🚨🇯 🇴 🇮  🇳  🇳 🇴 🇼⬇️

🚨 Main Group Join Karna Zaroori Hai ⤵️
https://t.me/+CWSr7qJLAY81OGY1

🚨 Backup Group Bhi Join Kar Lo ⤵️
https://t.me/+RuwEjpHLE0hiNGE9

👀 Video Kaise Dekhein? ⤵️
https://youtube.com/shorts/bCSnonQDKCg

❤️ Video dekhne ke baad reaction dena mat bhoolna, aapka support hi motivation hai! 🙌🔥

👍 ❤️‍ 🔄
"""

    await context.bot.send_video(
        chat_id=CHANNEL_ID,
        video=update.message.video.file_id,
        caption=caption,
    )

    await update.message.reply_text(
        f"✅ Posted Successfully\n📌 Post No: {post_no}"
    )


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("setpost", setpost))
app.add_handler(CommandHandler("postno", postno))
app.add_handler(MessageHandler(filters.VIDEO, handle_video))

print("Bot Started...")
app.run_polling()