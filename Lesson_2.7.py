# Реалізуйте програму, яка копіює вміст одного файлу в інший.

def copy_file(txt_file_one, txt_file_two):
    try:
        with open(txt_file_one, "r") as file1:
            with open(txt_file_two, "w") as file2:
                file2.write(file1.read())
        print("Файл успішно скопійовано.")
    except FileNotFoundError:
        print("Помилка! Файл не знайденно...")
    except:
        print("Помилка при копіюванні.")


name_file1 = "Import_this.txt"
name_file2 = "New_File.txt"
copy_file(name_file1, name_file2)

