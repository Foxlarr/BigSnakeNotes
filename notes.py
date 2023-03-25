import datetime
import json

# Открытие файла с заметками (если файл не существует, он будет создан)
try:
    with open("notes.json", "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    notes = []

# Функция для сохранения заметок в файл
def save_notes():
    with open("notes.json", "w") as f:
        json.dump(notes, f)

# Функция для добавления новой заметки
def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": len(notes)+1, "title": title, "body": body, "timestamp": timestamp}
    notes.append(note)
    save_notes()

# Функция для просмотра списка заметок
def view_notes():
    for note in notes:
        print(f"ID: {note['id']}, Title: {note['title']}, Timestamp: {note['timestamp']}")

# Функция для просмотра конкретной заметки
def view_note():
    id = int(input("Введите ID заметки: "))
    note = [n for n in notes if n["id"] == id]
    if note:
        note = note[0]
        print(f"Title: {note['title']}, Timestamp: {note['timestamp']}")
        print(f"Body:\n{note['body']}")
    else:
        print("Заметка не найдена")

# Функция для редактирования заметки
def edit_note():
    id = int(input("Введите ID заметки: "))
    note = [n for n in notes if n["id"] == id]
    if note:
        note = note[0]
        title = input(f"Текущий заголовок: {note['title']}\n Введите новый заголовок или нажмите Enter для сохранения текущего: ")
        if title:
            note["title"] = title
        body = input(f"Текущий текст:\n{note['body']}\n Введите новый текст или нажмите Enter для сохранения текущего: ")
        if body:
            note["body"] = body
        note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_notes()
    else:
        print("Заметка не найдена")

