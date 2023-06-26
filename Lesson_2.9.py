# Створіть функцію, яка видаляє вказаний рядок з текстового файлу.

def remove_line(file_name, rem_line):
    with open(file_name, "r+") as file:
        str_txt = file.readlines()
        file.seek(0)

        for line in str_txt:
            if line.strip() != rem_line:
                file.write(line)

        file.truncate()


in_file_name = "New_file.txt"
input_line_rem = input("Введіть текст який потрібно видалити: \n")
remove_line(in_file_name, input_line_rem)

