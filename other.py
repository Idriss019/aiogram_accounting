from datetime import date

mysring = "дата 21 кредит 345 раздел молоко описание лекарство"

# mylist_ = "стоимость", "2312", "раздел", "хозрасход", "описание", "мешки", "цемента",

# trigger02 = {"цена": "цена",
#            "стоимость": "цена",
#            "раздел": "раздел",
#            "класс": "раздел",
#            "описание": "описание",
#            "дата": "дата"}

trigger = {"дата": "date",
           "число": "date",
           "+": "debt",
           "плюс": "debt",
           "дебит": "debt",
           "-": "credit",
           "минус": "credit",
           "кредит": "credit",
           "раздел": "section",
           "класс": "section",
           "описание": "description",
           "айди": "id"
           }
trigger_in_russian = {"дата": "date",
                      "приход": "debt",
                      "расход": "credit",
                      "раздел": "section",
                      "описание": "description",
                      "айди": "id"
                      }


def sorting_in_data(string_):
    list_ = string_.split()
    dictionary_for_list = {}
    trigger_in_list = None
    other_in_list = None
    number = False

    for i in list_:
        if i in trigger.keys():
            if number:
                dictionary_for_list[trigger_in_list] = other_in_list
                other_in_list = None
                trigger_in_list = trigger[i]
            else:
                number = True
                trigger_in_list = trigger[i]
        elif trigger_in_list:
            if other_in_list:
                other_in_list += " "
                other_in_list += i
            else:
                other_in_list = i

    dictionary_for_list[trigger_in_list] = other_in_list
    if dictionary_for_list.get('date'):
        if dictionary_for_list['date'] == "вчера":
            dictionary_for_list['date'] = date(date.today().year, date.today().month, date.today().day - 1)
        elif dictionary_for_list['date'] == "нету" or dictionary_for_list['date'] == "нет" or dictionary_for_list[
            'date'] == "отсуствует":
            dictionary_for_list['date'] = None
        elif dictionary_for_list['date']:
            date_ = int(dictionary_for_list['date'])
            dictionary_for_list['date'] = date(date.today().year, date.today().month, date_)

    return dictionary_for_list


def translate_dir(dir_):
    new_dir = {}
    for k, v in trigger_in_russian.items():
        if dir_.get(v):
            new_dir[k] = dir_[v]
    return new_dir

# print(sorting_in_russian(sorting_in_data(mysring)))

# r = sorting_in_data(mysring)
# print(type(r))
# for i in r:
#     print(i)
#     print(type(i))
#     print(i[i])
