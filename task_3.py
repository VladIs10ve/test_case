# Задача предполагает 1 учителя и 1 ученика,
# исходя из этого я посчитал данные 2 теста невалидными.
def appearance(intervals):
    online = 0
    time_online = 0
    events = []
    # Заполняем список событиями (вход/выход), сортируем.
    for schedule_item in intervals.keys():
        for item in range(len(intervals[schedule_item])):
            if item % 2 == 0:
                events.append((intervals[schedule_item][item], 1))
            else:
                events.append((intervals[schedule_item][item], -1))
    events.sort()

    previous_online = None
    timestamp = None

    # Проходим по списку событий,
    # Вычисляем промежутки общего присутствия ученика и учителя на уроке.
    for event in events:
        online += event[1]
        if online == 3:
            timestamp = event[0]
        elif online != 3 and previous_online == 3:
            time_online += event[0] - timestamp
        previous_online = online

    return time_online


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    # {'data': {'lesson': [1594702800, 1594706400],
    #           'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
    #                     1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
    #                     1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
    #                     1594706524, 1594706524, 1594706579, 1594706641],
    #           'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    #  'answer': 3577
    #  },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
