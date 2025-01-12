import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить оценку ученика по предмету
        5. Изменить оценку ученика по предмету
        6. Удалить ученика
        7. Изменить ученика
        8. Удалить предмет
        9. Добавить предмет
        10. Изменить предмет
        11. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удалить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # удаляем оценку у ученика по предмету
            print(students_marks[student][class_])
            number = int(input('Введите порядковый номер оценки, которую хотите удалить: '))
            students_marks[student][class_].pop(number-1)
            print(f'Для {student} по предмету {class_} удалена оценка')
            print(students_marks[student][class_])
            # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 5:
        print('5. Изменить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # изменяем оценку у ученика по предмету
            print(students_marks[student][class_])
            number = int(input('Введите порядковый номер оценки, которую хотите изменить: '))
            mark = int(input('Введите оценку, которую хотите добавить: '))
            students_marks[student][class_][number - 1] = mark
            print(f'Для {student} по предмету {class_} изменена оценка')
            print(students_marks[student][class_])
            # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 6:
        print('6. Удалить ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # если данные введены верно
        if student in students:
            # удаляем ученика
            students.remove(student)
            print(f'Ученик {student} удален')
            # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: такого ученика нет в списке')
    elif command == 7:
        print('7. Изменить имя ученика')
        # считываем имя ученика
        student = input('Введите старое имя ученика: ')
        if student in students:
            student_new = input('Введите новое имя ученика: ')
            students.append(student_new)
            print(f'Ученик {student_new} добавлен')
            students_marks[student_new] = students_marks[student]
            students.remove(student)
        else:
            print('ОШИБКА: такого ученика нет в списке')
    elif command == 8:
        print('8. Удалить предмет')
        # считываем название предмета
        class_ = input('Введите название предмета: ')
        # если данные введены верно
        if class_ in classes:
            # удаляем предмет8
            classes.remove(class_)
            print(f'Предмет {class_} удален')
            # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: такого предмета нет в списке')
    elif command == 9:
        print('9. Добавить название предмета')
        # считываем название предмета
        class_new = input('Введите название предмета: ')
        if class_new in classes:
            print('Этот предмет уже есть в списке')
        else:
            classes.append(class_new)
            print(f'Предмет {class_new} добавлен')
            for student in students:
                students_marks[student][class_new] = students_marks[student][class_]
            classes.remove(class_)
            print(classes)
    elif command == 10:
        print('10. Изменить название предмета')
        # считываем название предмета
        class_ = input('Введите старое название предмета: ')
        if class_ in classes:
            class_new = input('Введите новое название предмета: ')
            classes.append(class_new)
            print(f'Предмет {class_new} добавлен')
            for student in students:
                students_marks[student][class_new] = students_marks[student][class_]
            classes.remove(class_)
            print(classes)
        else:
            print('ОШИБКА: такого предмета нет в списке')
    elif command == 11:
        print('11. Выход из программы')
        break