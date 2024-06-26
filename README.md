# Sistema de Gestión de Productos, Usuarios y Ventas

## Instrucciones para Ejecutar la Aplicación

### Prerrequisitos

-   Python 3.x (incluye `sqlite3` por defecto)
-   Bibliotecas necesarias (para instalarlas, usa `pip install -r requirements.txt`)

### Instalación

1. Clona este repositorio:

    ```sh
    git clone https://github.com/miguelalejandroff/evaluacion-cs.git
    cd evaluacion-cs
    ```

2. Instala las bibliotecas necesarias:

    ```sh
    pip install -r requirements.txt
    ```

3. Inicializa la base de datos:

    ```sh
    python initialize_db.py
    ```

4. Ejecuta la aplicación:
    ```sh
    python main.py
    ```

### Uso

1. Selecciona una opción del menú principal para gestionar productos, usuarios o ventas.
2. Sigue las instrucciones en pantalla para realizar las operaciones deseadas.

#### Menú Principal

-   **Menú de Productos**: Realiza operaciones CRUD sobre productos.
-   **Menú de Usuarios**: Gestiona usuarios y sus roles.
-   **Menú de Ventas**: Registra y lista ventas.

#### Menú de Productos

-   **Crear Producto**: Agrega un nuevo producto.
-   **Ver Producto**: Muestra los detalles de un producto específico.
-   **Actualizar Producto**: Modifica los detalles de un producto existente.
-   **Activar/Desactivar Producto**: Cambia el estado de un producto entre activo e inactivo.
-   **Listar Productos**: Muestra una lista de todos los productos activos.

#### Menú de Usuarios

-   **Crear Usuario**: Agrega un nuevo usuario y asigna un rol.
-   **Ver Usuario**: Muestra los detalles de un usuario específico.
-   **Actualizar Usuario**: Modifica los detalles de un usuario existente y su rol.
-   **Activar/Desactivar Usuario**: Cambia el estado de un usuario entre activo e inactivo.
-   **Listar Usuarios**: Muestra una lista de todos los usuarios activos.

#### Menú de Ventas

-   **Registrar Venta**: Registra una nueva venta.
-   **Listar Ventas**: Muestra una lista de todas las ventas registradas.

### Pruebas

1. Ejecuta las pruebas unitarias:

    ```sh
    python -m unittest discover tests -v
    ```

### Resultados de las Pruebas

-   Se realizaron pruebas unitarias para validar las operaciones CRUD sobre productos, usuarios y ventas.
