#Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі, так і маленькі).
#Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

while True:
    input_word = input("Введіть слово або фразу, яка містить букву 'h' або 'H': ")
    if 'h' in input_word.lower():
        print("Дякую! Ви ввели правильне слово:", input_word)
        break
    else:
        print("Спробуйте ще раз. У слові немає літери 'h' або 'H'.")