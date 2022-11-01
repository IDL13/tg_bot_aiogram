import os
from message import MESSAGES
from parser import info, vip_info
from dotenv import load_dotenv
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from aiogram.types.message import ContentType
from main import dp, bot
from db.models import *
from db.config import *
from aiogram.types import BotCommand, BotCommandScopeDefault

load_dotenv()

PRICES = [LabeledPrice(label='VIP', amount = 2550)]

@dp.message_handler(commands=['start'])
async def start_cmd(message:Message):
    await message.answer(MESSAGES['start'])

@dp.message_handler(commands=['terms'])
async def terms_cmd(message:Message):
    await message.answer(MESSAGES['terms'])

@dp.message_handler(commands=['help'])
async def help_cmd(message:Message):
    await message.answer(MESSAGES['help'])

@dp.message_handler(commands=['get'])
async def get_cmd(message:Message):
    await message.answer(info)

@dp.message_handler(commands=['vip'])
async def buy_process(message: Message):
    await bot.send_invoice(message.chat.id,
                           title=MESSAGES['title'],
                           description=MESSAGES['description'],
                           provider_token=os.getenv('PAY_KEY'),
                           currency='rub',
                           photo_url=os.getenv('ITEM_URL'),
                           photo_height=212,
                           photo_width=212,
                           photo_size=212,
                           need_email=True,
                           need_phone_number=True,
                           is_flexible=False,
                           prices=PRICES,
                           start_parameter='example',
                           payload='some_invoice')

@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_process(pre_checkout_query: PreCheckoutQuery):
    userinfo = pre_checkout_query.order_info
    id = pre_checkout_query.from_user.id
    name = pre_checkout_query.from_user.username
    new_user = User(tg_id = str(id),name = str(name),phone = str(userinfo['phone_number']),email = str(userinfo['email']))
    session.add(new_user)
    session.commit()
    # user_serch = session.query(User).filter(User.tg_id == f"{id}").first()
    # print(f' id:{id}\n username:{name}\n phone: {userinfo["phone_number"]}\n email: {userinfo["email"]}')
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message):
    await bot.send_message(
        message.chat.id,
        MESSAGES['success'].format(total_amount=message.successful_payment.total_amount // 100,
                                    currency=message.successful_payment.currency)
)
    @dp.message_handler(commands=['get_vip'])
    async def get_vip_cmd(message:Message):
        await message.answer(vip_info)


