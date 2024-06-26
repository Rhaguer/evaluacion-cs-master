from autenticacion import Autenticacion
from views.MainMenu import MainMenu
from contexto import Contexto

def main():

    username = input("Ingrese su nombre de usuario: ")
    usuario = Autenticacion.autenticar_usuario(username=username)
    if not usuario:
        return

    main_menu = MainMenu()
    main_menu.run()

    # Limpiar el contexto al finalizar
    Contexto.clear()

if __name__ == "__main__":
    main()