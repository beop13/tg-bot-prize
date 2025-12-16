import os
import logging
import asyncio

import config
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ContextTypes,
)

logger = logging.getLogger("bot")

async def delayed_message(chat_id: int, context: ContextTypes.DEFAULT_TYPE, delay_minutes: int):
    """Отправляет сообщение через delay_minutes без блокировки"""
    await asyncio.sleep(delay_minutes * 60)  # минуты → секунды
    try:
        await context.bot.send_message(chat_id=chat_id, text="Это второе сообщение спустя N минут ⏰")
    except Exception as e:
        logger.error("cant send message: %s", e)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /start и deep-link обработка
    """
    args = context.args

    if args and args[0] == "gift":
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🔔 Подписаться на канал",
                        url=config.CHANNEL_URL
                    )
                ]
            ]
        )

        if update.message is None:
            logger.error("update message is none")
            return

        await update.message.reply_text(
            config.GIFT_TEXT,
            reply_markup=keyboard,
        )

        asyncio.create_task(delayed_message(update.message.chat_id, context, delay_minutes=1))

        return

    if update.message is None:
        logger.error("update message is none")
        return

    await update.message.reply_text(
        "Кукусики"
    )
    return
