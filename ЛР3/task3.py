# TODO  Напишите функцию count_letters
def count_letters(text):
    letters = {}
    for char in text.lower():
        if char.isalpha():
            letters[char] = letters.get(char, 0) + 1
    return letters

def calculate_frequency(letter_count):
    total_letters = sum(letter_count.values())
    frequencies = {key: value / total_letters for key, value in letter_count.items()}
    return frequencies

# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
text_lower = main_str.lower()
letters_count = count_letters(text_lower)
frequencies = calculate_frequency(letters_count)
for key,value in frequencies.items():
    print(f"{key}: {round(value,2):.2f}")

# TODO Распечатайте в столбик букву и её частоту в тексте
