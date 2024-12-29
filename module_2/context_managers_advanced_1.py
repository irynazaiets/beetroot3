class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print("Файл закрито")
        # Повертаємо True, щоб не перекидати виключення
        return exc_type is None


# Використання:
with FileManager("example.txt", "w") as f:
    f.write("Hello, контекстний менеджер!")


# Приклад використання методу __exit__ з 
# використанням стандартних параметрів методу
class FilterErrors:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == ValueError:
            print(f"Ігноруємо ValueError: {exc_val}")
            return True  # Не передаємо далі виключення
        print(f"Не оброблене виключення: {exc_type.__name__}")
        return False  # Інші виключення підуть далі

with FilterErrors():
    raise ValueError("Це ValueError, і його проігнорують")  # Виключення буде оброблене

with FilterErrors():
    raise TypeError("Це TypeError, і його не оброблять")  # Виключення підніметься