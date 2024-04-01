from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler,
)

from core.auth import auth
from core.env_handler import load_env
from core.error_handlers import error_handler
from core.file_handler import save_record
from core.logger import get_logger
from core.types import State
from core.utils import process_record_message


logger = get_logger()
env = load_env()

# Commands
@error_handler
@auth
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Hello. What you want to do?",
        reply_markup=ReplyKeyboardMarkup(
            one_time_keyboard=True,
            keyboard=[['/record', '/analycit', '/cancel']]
        ),
    )

    return State.ADD_RECORD


@error_handler
@auth
async def add_record(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.info(f"Adding record")

    new_record = process_record_message(update.message.text)
    # save_record(context.user_data['user_id'], new_record)

    logger.info(f"Adding record: \n {new_record}")
    
    await update.message.reply_text(
        f"{new_record} was added \n"
        "going back to start"
    )

    return ConversationHandler.END

@error_handler
@auth
async def get_analysis(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.info(f"Generate analysis")

    # new_record = process_record_message(update.message.text)
    # save_record(context.user_data['user_id'], new_record)

    # logger.info(f"Adding record: \n {new_record}")
    
    # await update.message.reply_text(
    #     f"{new_record} was added \n"
    #     "going back to start"
    # )

    return ConversationHandler.END


@error_handler
@auth
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    logger.info('Press cancel button')
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main():
    
    logger.info('Starting the application')

    app = Application.builder().token(env.TOKEN).build()
    
    logger.info('Application initiated')

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            State.ADD_RECORD: [
                MessageHandler(filters.TEXT, add_record),
                CommandHandler("cancel", cancel),
            ]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)

    logger.info('Run polling...')
    app.run_polling(poll_interval=3)
    logger.info('Polling runned')


if __name__ == "__main__":
    main()
