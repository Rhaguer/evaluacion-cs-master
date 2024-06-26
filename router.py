class Router:
    def __init__(self, title="Menú de Operaciones CRUD"):
        self.routes = []
        self.title = title

    def register(self, controller):
        for attr_name in dir(controller):
            attr = getattr(controller, attr_name)
            if callable(attr) and getattr(attr, 'is_menu_action', False):
                self.routes.append((attr.menu_order, attr.menu_name, attr))

        # Ordenar las rutas por el atributo 'menu_order'
        self.routes.sort(key=lambda x: x[0])

    def run(self):
        max_length = max(len(name) for _, name, _ in self.routes)
        max_length = max(max_length, len(self.title)) + 5  # Añadir 5 para el espacio adicional y los números
        
        while True:

            print("+" + "-" * (max_length + 4) + "+")
            print(f"|  {self.title.ljust(max_length)}  |")
            print("+" + "-" * (max_length + 4) + "+")
            for idx, (_, name, _) in enumerate(self.routes, 1):
                print(f"| {idx}. {name.ljust(max_length)}|")
            print(f"| 0. Salir{' ' * (max_length - len('Salir'))}|")
            print("+" + "-" * (max_length + 4) + "+")

            choice = input("Seleccione una opción: ")

            if choice == '0':
                break

            try:
                choice = int(choice)
                if 1 <= choice <= len(self.routes):
                    action = self.routes[choice - 1][2]
                    action()
                else:
                    print("Opción inválida. Inténtelo de nuevo.")
            except ValueError:
                print("Opción inválida. Inténtelo de nuevo.")
