# Вывести последнюю букву в слове
word = 'Архангельск'
print(f"Последная буква - {word[-1]}")
print()


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(f"В слове {word} {word.lower().count('а')} буквы а")
print()


# Вывести количество гласных букв в слове
word = 'Архангельск'
letters = 'аоуэиыяюеё'
count = 0
for i in word.lower():
    if i in letters:
        count += 1
print(f"Количество гласных букв в слове {word} - {count}")
print()



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f"Количество слов в предложении -  {len(sentence.split())}")
print()


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print("Первые буквы каждого слова в предложении: ", end='')
for i in sentence.split():
    print(i[0], end=' ')
print("\n")


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
letters_counter = []

for word in sentence.split():
    letters_counter.append(len(word))
print(f"Средняя длинна слов в предложении - {sum(letters_counter)/len(letters_counter)}")