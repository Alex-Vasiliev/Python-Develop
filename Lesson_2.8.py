# Напишіть програму, яка відкриває два файли для читання та порівнює їх вміст,
# виводячи рядки, які є у першому файлі, але відсутні у другому.


def copy_file(txt_file_one, txt_file_two):
    try:
        with open(txt_file_one, "r") as file1, open(txt_file_two, "r") as file2:
            txt1 = file1.read().splitlines()
            txt2 = file2.read().splitlines()
            comparison = set(txt1).difference(txt2)

        for item in comparison:
            print(item)
    except FileNotFoundError:
        print("Помилка! Один або обидва файли не знайдено.")
    except Exception as e:
        print("Помилка виконання дій:", e)


name_file1 = "File-1_for_task_2.8.txt"
name_file2 = "File-2_for_task_2.8.txt"
copy_file(name_file1, name_file2)
