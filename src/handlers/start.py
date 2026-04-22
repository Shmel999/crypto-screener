def start_command_handler(update, context):
    welcome_message = "Welcome to the Crypto Screener Bot!\nHere are the instructions to get you started:\n1. Use /price to get the current price of a cryptocurrency.\n2. Use /trend to see the price trend for a specific crypto.\n3. Use /help for additional assistance.">
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)

# To enable this handler, you can add it to your dispatcher in the main bot file.