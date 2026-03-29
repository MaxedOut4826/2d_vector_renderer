from os import system as terminal, name as operation_system

def clear_screen():
    if operation_system == "nt":
        terminal("cls")
    else:
        terminal("clear")