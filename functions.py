FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Citeste taskurile dintr-un fisier text precizat
    :param filepath: Fisierul din care citeste taskurile
    :return: Lista de taskuri pastrata in fisierul text precizat
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_list, filepath=FILEPATH):
    """
    Scrie elementele todo list in fisierul text specificat
    :param todos_list: lista de elemente todo
    :param filepath: calea catre fisierul in care se vor scrie taskurile
    :return: None
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_list)


# print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
