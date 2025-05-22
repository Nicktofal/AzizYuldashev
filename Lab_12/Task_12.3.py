with open('en-ru.txt', 'r', encoding='utf-8') as f:
    en_ru = [line.strip().split(' - ') for line in f]

ru_en = {}
for en, ru in en_ru:
    for ru_word in ru.split(', '):
        if ru_word not in ru_en:
            ru_en[ru_word] = []
        ru_en[ru_word].append(en)

with open('ru-en.txt', 'w', encoding='utf-8') as f:
    for ru in sorted(ru_en.keys()):
        f.write(f"{ru} - {', '.join(ru_en[ru])}\n")