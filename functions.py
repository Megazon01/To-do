FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Opens file in filepath in read mode
    and returns lines as a list.
    """
    with open(filepath, "r") as file_func:
        todos_local = file_func.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Opens file in filepath in write mode
    and writes a new line.
    """
    with open(filepath, "w") as file_w:
        file_w.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())
