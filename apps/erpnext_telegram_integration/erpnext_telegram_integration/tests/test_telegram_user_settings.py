import frappe
import unittest
from unittest.mock import patch, MagicMock
from erpnext_telegram_integration.erpnext_telegram_integration.doctype.telegram_user_settings.telegram_user_settings import TelegramUserSettings, get_chat_id_button, get_chat_id

class TestTelegramUserSettings(unittest.TestCase):

    def setUp(self):
        frappe.db.begin()

    def tearDown(self):
        frappe.db.rollback()

    def test_telegram_user_settings_creation(self):
        # Test basic creation of the DocType
        settings = frappe.new_doc("Telegram User Settings")
        settings.user = "test_user"
        settings.telegram_chat_id = "12345"
        settings.insert()
        self.assertIsNotNone(frappe.get_doc("Telegram User Settings", settings.name))

    @patch('erpnext_telegram_integration.erpnext_telegram_integration.doctype.telegram_user_settings.telegram_user_settings.get_chat_id')
    @patch('frappe.get_doc')
    def test_get_chat_id_button(self, mock_get_doc, mock_get_chat_id):
        # Mock frappe.get_doc to return a Telegram Settings document
        mock_telegram_settings = MagicMock()
        mock_telegram_settings.telegram_bot_token = "mock_token"
        mock_get_doc.return_value = mock_telegram_settings

        # Mock get_chat_id to return a chat ID
        mock_get_chat_id.return_value = "mock_chat_id"

        telegram_token = "test_telegram_token"
        telegram_settings_name = "Telegram Settings"

        result = get_chat_id_button(telegram_token, telegram_settings_name)

        mock_get_doc.assert_called_with("Telegram Settings", telegram_settings_name)
        mock_get_chat_id.assert_called_with(mock_telegram_settings.telegram_bot_token, telegram_token)
        self.assertEqual(result, "mock_chat_id")

    @patch('frappe.msgprint')
    @patch('telegram.Bot')
    async def test_get_chat_id_success(self, mock_bot, mock_msgprint):
        # Mock the Bot and its methods
        mock_instance = MagicMock()
        mock_bot.return_value = mock_instance
        mock_instance.delete_webhook.return_value = True

        # Mock get_updates to return a message with the matching token
        mock_update = MagicMock()
        mock_update.message.text = "test_token"
        mock_update.message.chat.id = "12345"
        mock_instance.get_updates.return_value = [mock_update]

        telegram_token_bot = "bot_token"
        telegram_token = "test_token"

        chat_id = await get_chat_id(telegram_token_bot, telegram_token);

        mock_instance.delete_webhook.assert_called_once()
        mock_instance.get_updates.assert_called_once_with(offset=0)
        self.assertEqual(chat_id, "12345")
        mock_msgprint.assert_called_with("Chat ID: 12345")

    @patch('frappe.msgprint')
    @patch('telegram.Bot')
    async def test_get_chat_id_no_match(self, mock_bot, mock_msgprint):
        # Mock get_updates to return messages without the matching token
        mock_instance = MagicMock()
        mock_bot.return_value = mock_instance
        mock_instance.delete_webhook.return_value = True

        mock_update_other = MagicMock()
        mock_update_other.message.text = "another_token"
        mock_instance.get_updates.return_value = [mock_update_other]

        telegram_token_bot = "bot_token"
        telegram_token = "test_token"

        chat_id = await get_chat_id(telegram_token_bot, telegram_token);

        self.assertIsNone(chat_id)
        mock_msgprint.assert_called_with("No chat ID found. Please send the token again.")

    @patch('frappe.msgprint')
    @patch('telegram.Bot')
    async def test_get_chat_id_telegram_error(self, mock_bot, mock_msgprint):
        # Mock Bot initialization to raise an error
        mock_bot.side_effect = Exception("Telegram API Error")

        telegram_token_bot = "bot_token"
        telegram_token = "test_token"

        chat_id = await get_chat_id(telegram_token_bot, telegram_token);

        self.assertIsNone(chat_id)
        mock_msgprint.assert_called_with("Error fetching chat ID: Telegram API Error")
