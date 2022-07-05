import requests
from bs4 import BeautifulSoup

# Время работы скрипта 1-2 минуты
# Может понадобиться установка lxml ( pip3 install lxml )

var = 'Аардоникс'

animals = {'А': set(), 'Б': set(), 'В': set(), 'Г': set(), 'Д': set(), 'Е': set(), 'Ж': set(), 'З': set(),
           'И': set(), 'Й': set(), 'К': set(),
           'Л': set(), 'М': set(), 'Н': set(), 'О': set(), 'П': set(), 'Р': set(), 'С': set(), 'Т': set(), 'У': set(),
           'Ф': set(), 'Х': set(), 'Ц': set(),
           'Ч': set(), 'Ш': set(), 'Щ': set(), 'Э': set(), 'Ю': set(), 'Я': set()}

for i in range(250):
    response = requests.get(
        url="https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom=" + var,
    )
    soup = BeautifulSoup(response.content, 'lxml')

    local = soup.find(class_="mw-category mw-category-columns").find_all(class_='mw-category-group')
    for item in local:
        list_of_names = item.text.split('\n')
        if list_of_names[0] in animals.keys():
            animals[list_of_names[0]].update(set(list_of_names[1:]))
        else:
            break
        var = list_of_names[-1]

for key, value in animals.items():
    print(key, ':', len(value))
    # print(key, ':', value)  # Вывод списка всех животных по алфавиту
