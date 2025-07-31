import frappe
import telegram
import asyncio
from frappe.model.document import Document

class TelegramUserSettings(Document):
    # Existing document methods here
    pass

@frappe.whitelist()
def get_chat_id_button(telegram_token, telegram_settings):
    """
    Button method to get the chat ID for a user's Telegram settings
    """
    telegram_settings_doc = frappe.get_doc("Telegram Settings", telegram_settings)
    telegram_token_bot = telegram_settings_doc.get_password("telegram_bot_token")
    
    chat_id = asyncio.run(get_chat_id(telegram_token_bot, telegram_token))
    
    return chat_id

async def get_chat_id(telegram_token_bot, telegram_token):
    """
    Get chat ID from Telegram bot
    
    First delete any existing webhook as Telegram doesn't allow both 
    webhook and polling methods to be active simultaneously.
    """
    bot = telegram.Bot(telegram_token_bot)
    
    # First delete any existing webhook
    await bot.delete_webhook()
    
    # Now safe to get updates
    updates = await bot.get_updates(limit=200)
    
    chat_id = None
    for u in updates:
        message = u.message or u.edited_message
        if message:
            if message.text == telegram_token:
                chat_id = message.chat.id
    
    # Note: If you were using webhooks before, you might want to restore them here
    # await bot.set_webhook(url="your_webhook_url")
    
    return chat_id