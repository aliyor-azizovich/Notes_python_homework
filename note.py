import json
import datetime

# Функция для сохранения заметок в JSON файл
def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file)

# Функция для чтения заметок из JSON файла
def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

# Функция для добавления новой заметки
def add_note(title, message):
    notes = load_notes()
    new_note = {
        'id': len(notes) + 1,
        'title': title,
        'message': message,
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    notes.append(new_note)
    save_notes(notes)
    print('Заметка успешно добавлена')

# Функция для чтения заметок из файла
def read_notes_from_file(filename):
    try:
        with open(filename, 'r') as file:
            notes = file.readlines()
            for note in notes:
                print(note)
    except FileNotFoundError:
        print('Файл с заметками не найден.')

# Функция для вывода всех заметок
def show_all_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")
        print(note['message'])
        print()

# Функция вывода по id
def show_by_id(note_id):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")
            print(note['message'])
            print()
            return
    print('Заметка с указанным ID не найдена')
# Функция для выборки заметок по дате
def show_notes_by_date(date):
    notes = load_notes()
    filtered_notes = [note for note in notes if note['timestamp'].split()[0] == date]
    if filtered_notes:
        for note in filtered_notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['timestamp']}")
            print(note['message'])
            print()
    else:
        print('Заметок на указанную дату нет')

# Функция для редактирования заметки
def edit_note(note_id, new_title, new_message):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            note['title'] = new_title
            note['message'] = new_message
            note['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_notes(notes)
            print('Заметка успешно отредактирована')
            return
    print('Заметка с указанным ID не найдена')

    # Функция для удаления заметки из файла по ID
def delete_note(note_id):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print('Заметка успешно удалена')
            return
    print('Заметка с указанным ID не найдена')
# Главная функция
def main():
    while True:
        command = input('Введите команду (add, read, edit, delete, show, show_by_date, show_by_id, exit): ')
        
        if command == 'add':
            title = input('Введите заголовок заметки: ')
            message = input('Введите текст заметки: ')
            add_note(title, message)
        
        elif command == 'read':
            filename = input('Введите имя файла для чтения заметок: ')
            read_notes_from_file(filename)    
        
        elif command == 'show':
            show_all_notes()
        
        elif command == "show_by_id":
            note_id = int(input("Введите ID заметки для показа: "))
            show_by_id(note_id)
        
        elif command == 'show_by_date':
            date = input('Введите дату в формате ГГГГ-ММ-ДД: ')
            show_notes_by_date(date)
        
        elif command == 'exit':
            break
        elif command == 'edit':
            note_id = int(input('Введите ID заметки для редактирования: '))
            new_title = input('Введите новый заголовок заметки: ')
            new_message = input('Введите новый текст заметки: ')
            edit_note(note_id, new_title, new_message)

        elif command == 'delete':
            note_id = int(input('Введите ID заметки для удаления: '))
            delete_note(note_id)
        else:
            print('Некорректная команда. Попробуйте снова.')

if __name__ == '__main__':
    main()
