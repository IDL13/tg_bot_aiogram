help_message = '''
/help - помощь.
/vip - покупка vip подписки.
/terms - правила пользования ботом.
/get - получение курса валют
/get_vip - получение вип информации
'''

start_message = 'Привет! Тебя приветствует бот по корсу валют\n' + help_message

terms = '''\
Правила.
'''

error = '''\
Что-то пошло не так. Попробуй ешё!
'''

item = '''VIP подписка'''

successful_payment = '''
Вы провели платеж на сумму `{total_amount} {currency}` совершено успешно! Спасибо!
'''

menu = '''
Выберите нужную вам услугу:
___________________________
'''

description = '''
Получение дополнительных курсов валют
'''

MESSAGES = {
    'start': start_message,
    'help': help_message,
    'terms': terms,
    'error': error, 
    'title': item,
    'menu': menu, 
    'success': successful_payment,
    'description': description,
}
