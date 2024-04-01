from functools import wraps

from app.core.logger import get_logger

logger = get_logger()


async def undefined_error(update, context):

    await update.message.reply_text(
        "ERROR",
    )


def error_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwds):
        try:
            return await func(*args, **kwds)
        except Exception as exc:
            logger.error(f'UNHANDLED ERROR: {str(exc)}')
            return await undefined_error(*args, **kwds)
        
    return wrapper
