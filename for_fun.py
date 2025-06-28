text = 'Це просто текст для підрахунку символів та нічого більше, він повинен порахувати скільки тут симовлів без пробілів, а потім і з пробліами.'

count_without_spaces = 0
count_with_spaces = 0

for char in text:
    if char != ' ':
        count_without_spaces += 1
    count_with_spaces += 1

print(f"Кількість символів без пробілів: {count_without_spaces}")
print(f"Кількість символів з пробілами: {count_with_spaces}")