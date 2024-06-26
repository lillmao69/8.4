import datetime as dt

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(friend):
    # Находим город, где живет друг
    city = DATABASE.get(friend)
    
    # Если друга нет в словаре, возвращаем сообщение об ошибке
    if city is None:
        return f"Друг '{friend}' не найден в словаре DATABASE"
    
    # Находим смещение UTC для города
    offset = UTC_OFFSET.get(city)
    
    # Если города нет в словаре смещений, возвращаем сообщение об ошибке
    if offset is None:
        return f"Город '{city}' не найден в словаре UTC_OFFSET"
    
    # Получаем текущее время в UTC
    utc_now = dt.datetime.utcnow()
    
    # Вычисляем текущее время в городе друга
    local_time = utc_now + dt.timedelta(hours=offset)
    
    return local_time.strftime('%Y-%m-%d %H:%M:%S')

print(what_time('Соня'))
