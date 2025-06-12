"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
from collections import defaultdict

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def wrote_the_most_msg(messages):
    '''
    Какой пользователь отправил больше всего сообщений
    '''
    msg_counter = defaultdict(int)
    for msg in messages:
        msg_counter[msg["sent_by"]] += 1
    result =  max(msg_counter.items(),
               key=lambda v: v[1])
    return f"Пользователь с id {result[0]} отправил больше всего сообщений - {result[1]}"


def most_quoted_user(messages):
    '''
    Какому пользователю больше всего отвечали
    '''
    counter = defaultdict(int)
    for msg in messages:
        if not msg["reply_for"] is None:
            msg_id = msg["id"]
            for message in messages:
                if message["id"] == msg_id:
                    counter[message["sent_by"]] += 1
    result = max(counter.items(),
                 key=lambda v: v[1])
    return f"Пользователю с id {result[0]} отвечали больше всего раз - {result[1]}"


def most_readed_user(messages):
    '''
    Сообщения какого юзера читали больше всего
    '''
    counter = {}
    for msg in messages:
        counter.setdefault(msg["sent_by"], []).extend(msg["seen_by"])

    result = max(counter.items(),
                 key=lambda v: len(set(v[1])))
    return f"Сообщения пользователя с id {result[0]} читали больше всего уникальных пользователей - {len(set(result[1]))}"


def more_popular_time(messages):
    #когда отправляется больше всего сообщений
    counter = {"утром": 0,
               "днем": 0,
               "вечером": 0,
               }
    for msg in messages:
        time = msg["sent_at"].time()
        if time < datetime.time(hour=12):
            counter["утром"] += 1
        elif time < datetime.time(hour=18):
            counter["днем"] += 1
        else:
            counter["вечером"] += 1
    result = max(counter.items(),
                 key=lambda v: v[1])
    return f"Больше всего сообщений - {result[1]} отправляется {result[0]}"



def is_reply_for(messages, id, lk_count):
    for msg in messages:
        if msg["id"] == id:
            if msg["reply_for"] is None:
                return (lk_count, id)
            else:
                lk_count += 1
                id = msg["reply_for"]
                return is_reply_for(messages, id, lk_count)



def long_trade(messages):
    '''
    Какое сообщение начало самый длинный трейд
    '''
    gl_count = 0
    msg_id = ""
    for msg in messages:
        if msg["reply_for"] is not None:
            tmp = is_reply_for(messages, msg["reply_for"], lk_count=1)
            if tmp[0] > gl_count:
                gl_count, msg_id = tmp
    return f"Самый длинный трейд из {gl_count} сообщений начался с сообщения с id - {msg_id}"



if __name__ == "__main__":
    messages = generate_chat_history()
    print(wrote_the_most_msg(messages))
    print(most_quoted_user(messages))
    print(most_readed_user(messages))
    print(more_popular_time(messages))
    print(long_trade(messages))








