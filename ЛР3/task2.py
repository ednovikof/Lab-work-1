# TODO Напишите функцию find_common_participants
def find_common_participants(participants_1, participants_2, delimiter=","):
    participants_1 = participants_1.split(delimiter)
    participants_2 = participants_2.split(delimiter)
    result = list(set(participants_1) & set(participants_2))
    return sorted(result)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, "|")
print(result)

# TODO Провеьте работу функции с разделителем отличным от запятой
