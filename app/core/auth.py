from functools import wraps

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler


def auth_user(user_id: int) -> bool:
    if user_id in [761213047]:
        return True
    return False


async def undefined_user(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "UNDEFINED USER",
    )

    return ConversationHandler.END


def auth(func):

    @wraps(func)
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        
        user = update.message.from_user
        is_authenticated = auth_user(user.id)
    
        if not is_authenticated:
            return await undefined_user(update, context)
        
        context.user_data['user_id'] = user.id

        return await func(update, context)
    
    return wrapper
