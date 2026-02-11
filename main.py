from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Bot tokenını buraya kendi bokunu yaz
TOKEN = "8242101995:AAFuuKvAETg17MVkfL-k3utQNPIpXMLEAzM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("👋 Merhaba Hez", callback_data='selam'),
        ],
        [
            InlineKeyboardButton("📢 Öneri, Şikayet ya da destek için", callback_data='destek'),
            InlineKeyboardButton("Kanala Katıl", url="https://t.me/botnosatisdestek"),
        ],
        [
            InlineKeyboardButton("Lütfen İşlemini seç", callback_data='secim'),
        ],
        [],  # boş satır
        [
            InlineKeyboardButton("🔹 Ad-Soyad Sorgula", callback_data='adsoyad'),
            InlineKeyboardButton("🔹 TC Sorgula", callback_data='tc'),
        ],
        [
            InlineKeyboardButton("🔹 İşyeri Sorgula", callback_data='isyeri'),
            InlineKeyboardButton("🔹 Adres Sorgula", callback_data='adres'),
        ],
        [
            InlineKeyboardButton("🔹 Aile Sorgula", callback_data='aile'),
            InlineKeyboardButton("🔹 Sülale Sorgula", callback_data='sulale'),
        ],
      
        
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Merhaba Hez,\n"
        "Lütfen İşlemini seç 👇",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # loading'i kapatır

    if query.data == 'selam':
        await query.edit_message_text(text="Selam lan piç, ne bok istiyon?")
    elif query.data == 'destek':
        await query.edit_message_text(text="Destek için kanala yaz orospu çocuğu")
    elif query.data == 'adsoyad':
        await query.edit_message_text(text="Ad-Soyad sorgu için bilgi ver lan, neyi arıyosun?")
    # diğer callback'leri de aynı şekilde ekle, hepsini tek tek yazmakla uğraşma şimdi
    else:
        await query.edit_message_text(text=f"Seçtiğin bok: {query.data}\nŞimdi ne yapalım piç?")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot sik gibi çalışıyor lan...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
