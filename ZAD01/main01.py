import json
import datetime

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at
        }

class NoteApp:
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            with open(filepath, 'r') as f:
                self.notes = json.load(f)
        except FileNotFoundError:
            self.notes = []

    def create(self, title, body):
        id = len(self.notes) + 1
        note = Note(id, title, body)
        self.notes.append(note.to_dict())
        self.save()

    def list(self):
        for note in self.notes:
            print(f"ID: {note['id']}\nTitle: {note['title']}\nBody: {note['body']}\nCreated at: {note['created_at']}\n---")

    def update(self, id, title=None, body=None):
        for note in self.notes:
            if note['id'] == id:
                if title:
                    note['title'] = title
                if body:
                    note['body'] = body
                note['created_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break
        self.save()

    def delete(self, id):
        self.notes = [note for note in self.notes if note['id'] != id]
        self.save()

    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.notes, f)

if __name__ == "__main__":
    app = NoteApp('notes.json')
    while True:
        action = input("Что вы хотите сделать? (создать/список/обновить/удалить/выход): ")
        if action == "создать":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            app.create(title, body)
        elif action == "list":
            app.list()
        elif action == "update":
            id = int(input("Введите ID заметки для обновления: "))
            title = input("Введите новый заголовок заметки (оставьте пустым, чтобы сохранить текущий заголовок): ")
            body = input("Введите новый текст заметки (оставьте пустым, чтобы сохранить текущий текст): ")
            app.update(id, title=title or None, body=body or None)
        elif action == "delete":
            id = int(input("Введите ID заметки для удаления: "))
            app.delete(id)
        elif action == "quit":
            break
