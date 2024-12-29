from contextlib import contextmanager

@contextmanager
def managed_resource(filename, mode):
    f = open(filename, mode)
    try:
        yield f  # Виконання блоку with
    finally:
        f.close()
        print("Файл закрито")

# Використання:
with managed_resource("example.txt", "w") as f:
    f.write("This is Beetroot Academy")
