from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ================= TOKEN =================
TOKEN = "8577856126:AAGfwWDSha-FetVwietv-TXz9EcvovTUzhw"

# ================= KANAL =================
CHANNEL_USERNAME = "@Hybrid_Day_trader"


# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)

    if member.status == "left":
        keyboard = ReplyKeyboardMarkup(
            [[KeyboardButton("✅ Obuna bo‘ldim")]],
            resize_keyboard=True
        )
        await update.message.reply_text(
            f"Botdan foydalanish uchun kanalga obuna bo‘ling:\n{CHANNEL_USERNAME}",
            reply_markup=keyboard
        )
        return

    keyboard = ReplyKeyboardMarkup(
        [
            [KeyboardButton("📚 Kitoblar")],
            [KeyboardButton("🎬 Video darslar")]
        ],
        resize_keyboard=True
    )
    await update.message.reply_text("Kerakli bo‘limni tanlang:", reply_markup=keyboard)


# ================= OBUNA TEKSHIRISH =================
async def check_sub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)

    if member.status == "left":
        await update.message.reply_text("❌ Hali obuna bo‘lmagansiz.")
    else:
        keyboard = ReplyKeyboardMarkup(
            [
                [KeyboardButton("📚 Kitoblar")],
                [KeyboardButton("🎬 Video darslar")]
            ],
            resize_keyboard=True
        )
        await update.message.reply_text("✅ Obuna tasdiqlandi!", reply_markup=keyboard)


# ================= VIDEO FILE ID OLISH =================
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        file_id = update.message.video.file_id
        await update.message.reply_text(f"FILE_ID:\n{file_id}")


# ================= XABARLAR =================
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # obuna tekshir tugmasi
    if text == "✅ Obuna bo‘ldim":
        await check_sub(update, context)
        return


    # ================= KITOBLAR =================
    if text == "📚 Kitoblar":
        keyboard = ReplyKeyboardMarkup(
            [
                [KeyboardButton("📘 Aka FX")],
                [KeyboardButton("📗 Bozorni zabt etish 1")],
                [KeyboardButton("📗 Bozorni zabt etish 2")],
                [KeyboardButton("📕 Trading in the Zone")],
                [KeyboardButton("📕 Trading in the Zone (1)")],
                [KeyboardButton("📕 The Business Book")],
                [KeyboardButton("📕 The Manipulation Mastery")],
                [KeyboardButton("📕 Sign FX")],
                [KeyboardButton("📕 Tafakkur")],
                [KeyboardButton("⬅️ Orqaga")]
            ],
            resize_keyboard=True
        )
        await update.message.reply_text("Kitobni tanlang:", reply_markup=keyboard)


    elif text == "📘 Aka FX":
        await update.message.reply_document(open("aka_fx.pdf", "rb"))

    elif text == "📗 Bozorni zabt etish 1":
        await update.message.reply_document(open("Bozorni zabt etish 1-kitob 10-ta dars.pdf", "rb"))

    elif text == "📗 Bozorni zabt etish 2":
        await update.message.reply_document(open("Bozorni zabt etish 2-kitob.pdf", "rb"))

    elif text == "📕 Trading in the Zone":
        await update.message.reply_document(open("Trading_in_the_Zone.pdf", "rb"))

    elif text == "📕 Trading in the Zone (1)":
        await update.message.reply_document(open("Trading_in_the_Zone (1).pdf", "rb"))

    elif text == "📕 The Business Book":
        await update.message.reply_document(open("The_Business_Book_Big_Ideas_Simply_Explained.pdf", "rb"))

    elif text == "📕 The Manipulation Mastery":
        await update.message.reply_document(open("The_Manipulation_Mastery (7).pdf", "rb"))

    elif text == "📕 Sign FX":
        await update.message.reply_document(open("Sign Fx - Book Original.pdf", "rb"))

    elif text == "📕 Tafakkur":
        await update.message.reply_document(open("TAFAKKUR.pdf", "rb"))


    # ================= VIDEO =================
    elif text == "🎬 Video darslar":
        keyboard = ReplyKeyboardMarkup(
            [
                [KeyboardButton("MALAYSIAN SNR 1-dars"), KeyboardButton("MALAYSIAN SNR 2-dars")],
                [KeyboardButton("MALAYSIAN SNR 3-dars"), KeyboardButton("MALAYSIAN SNR 4-dars")],
                [KeyboardButton("MALAYSIAN SNR 5-dars"), KeyboardButton("Texnik analiz boshlang’ich darslari Trend va Trend line bilan ishlash mavzusi")],
                [KeyboardButton("Engulfing (Pogloshenie) Mavzusi"), KeyboardButton("7 svecha strategiyasi")],
                [KeyboardButton("Mavzu: Fibonachi Instrumenti"), KeyboardButton("Mavzu: Gold Zone strategy")],
          
                [KeyboardButton("⬅️ Orqaga")]
            ],
            resize_keyboard=True
        )
        await update.message.reply_text("Darsni tanlang:", reply_markup=keyboard)


    elif text == "MALAYSIAN SNR 1-dars":
        await update.message.reply_video("BAACAgIAAxkBAAOAaYtGF7r0VA1gG-XrtjG1KU-cdnIAAleTAALI0mFIZbtDomZ0-GY6BA")

    elif text == "MALAYSIAN SNR 2-dars":
        await update.message.reply_video("BAACAgIAAxkBAAOJaYtLui_Y2aZyrHINOnMZA2QoZocAAqqTAALI0mFIPveLO2mRWo06BA")

    elif text == "MALAYSIAN SNR 3-dars":
        await update.message.reply_video("BAACAgIAAxkBAAOpaYtUKYAMsVKRO9j-d8OtDNO8hR4AAkKUAALI0mFI7Nui85y0Sdc6BA")

    elif text == "MALAYSIAN SNR 4-dars":
        await update.message.reply_video("BAACAgIAAxkBAAOraYtUd_fkArFvcRw2veDFhVRNM4YAAlGUAALI0mFIAzFAigSAlzQ6BA")

    elif text == "MALAYSIAN SNR 5-dars":
        await update.message.reply_video("BAACAgIAAxkBAAOtaYtVBtmmWJSR7oORTeoEcw8OcgkAAmaUAALI0mFIsE9u-QZwrhI6BA")

    elif text == "Texnik analiz boshlang’ich darslari Trend va Trend line bilan ishlash mavzusi":
        await update.message.reply_video("BAACAgIAAxkBAAPGaYt8Hh4ilLL3vYzC_evX9fc1giEAAkmXAALI0mFIWB9XK5R2yF46BA")
    elif text == "Engulfing (Pogloshenie) Mavzusi":
        await update.message.reply_video("BAACAgIAAxkBAAPIaYt_LYTWNbZcz8HtcPpcDYaGRiwAApSXAALI0mFIrGf7dZfYU3Y6BA")

    elif text == "7 svecha strategiyasi":
        await update.message.reply_video("BAACAgIAAxkBAAPKaYuAFHfmL1oQKh3vXy1zI0C0_9IAAqaXAALI0mFIQ1DeFNGYHe86BA")

        
    elif text == "Mavzu: Fibonachi Instrumenti":
        await update.message.reply_video("BAACAgIAAxkBAAPMaYuAxstWhiI8nrfypi7xx1nWd70AAraXAALI0mFIAh9E-E51XyU6BA")

        
    elif text == "Mavzu: Gold Zone strategy":
        await update.message.reply_video("BAACAgIAAxkBAAPOaYuBPFYvKi4dIlLyoGGmDYsRdbEAAsCXAALI0mFIOEZgSY8_3Rs6BA")


    # ================= ORQAGA =================
    elif text == "⬅️ Orqaga":
        keyboard = ReplyKeyboardMarkup(
            [
                [KeyboardButton("📚 Kitoblar")],
                [KeyboardButton("🎬 Video darslar")]
            ],
            resize_keyboard=True
        )
        await update.message.reply_text("Bosh menyu:", reply_markup=keyboard)


# ================= MAIN =================
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, message_handler))

    # VIDEO YUBORILSA FILE ID CHIQARADI
    app.add_handler(MessageHandler(filters.VIDEO, get_file_id))

    print("🤖 Bot ishga tushdi...")
    app.run_polling()


if __name__ == "__main__":
    main()
