-- Crear tabla de roles
CREATE TABLE IF NOT EXISTS roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE
);

-- Crear tabla de permisos
CREATE TABLE IF NOT EXISTS permisos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE
);

-- Crear tabla intermedia para roles y permisos
CREATE TABLE IF NOT EXISTS rol_permiso (
    rol_id INTEGER NOT NULL,
    permiso_id INTEGER NOT NULL,
    FOREIGN KEY (rol_id) REFERENCES roles(id),
    FOREIGN KEY (permiso_id) REFERENCES permisos(id),
    PRIMARY KEY (rol_id, permiso_id)
);

-- Crear tabla intermedia para usuarios y roles
CREATE TABLE IF NOT EXISTS usuario_rol (
    usuario_id INTEGER NOT NULL,
    rol_id INTEGER NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (rol_id) REFERENCES roles(id),
    PRIMARY KEY (usuario_id, rol_id)
);

-- Crear tabla de usuarios (si no existe)
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    estado TEXT NOT NULL CHECK (estado IN ('activo', 'inactivo')) DEFAULT 'activo'
);

-- Crear tabla de productos (si no existe)
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,
    descripcion TEXT,
    precio REAL NOT NULL CHECK (precio > 0),
    cantidad INTEGER NOT NULL CHECK (cantidad >= 0),
    categoria TEXT NOT NULL,
    estado TEXT NOT NULL CHECK (estado IN ('activo', 'inactivo')) DEFAULT 'activo'
);

-- Crear tabla de ventas (si no existe)
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha DATE NOT NULL,
    vendedor_id INTEGER NOT NULL,
    FOREIGN KEY (producto_id) REFERENCES productos(id),
    FOREIGN KEY (vendedor_id) REFERENCES usuarios(id)
);

-- Insertar roles
INSERT INTO roles (nombre) VALUES ('Administrador');
INSERT INTO roles (nombre) VALUES ('Vendedor');

-- Insertar permisos
INSERT INTO permisos (nombre) VALUES ('crear_producto');
INSERT INTO permisos (nombre) VALUES ('ver_producto');
INSERT INTO permisos (nombre) VALUES ('actualizar_producto');
INSERT INTO permisos (nombre) VALUES ('eliminar_producto');
INSERT INTO permisos (nombre) VALUES ('listar_productos');
INSERT INTO permisos (nombre) VALUES ('registrar_venta');
INSERT INTO permisos (nombre) VALUES ('listar_ventas');
INSERT INTO permisos (nombre) VALUES ('crear_usuario');
INSERT INTO permisos (nombre) VALUES ('leer_usuario');
INSERT INTO permisos (nombre) VALUES ('actualizar_usuario');
INSERT INTO permisos (nombre) VALUES ('eliminar_usuario');
INSERT INTO permisos (nombre) VALUES ('listar_usuarios');

-- Asociar permisos con roles
-- Permisos para Administrador
INSERT INTO rol_permiso (rol_id, permiso_id) 
VALUES 
((SELECT id FROM roles WHERE nombre = 'Administrador'), (SELECT id FROM permisos WHERE nombre = 'crear_producto')),
((SELECT id FROM roles WHERE nombre = 'Administrador'), (SELECT id FROM permisos WHERE nombre = 'ver_producto')),
((SELECT id FROM roles WHERE nombre = 'Administrador'), (SELECT id FROM permisos WHERE nombre = 'actualizar_producto')),
((SELECT id FROM roles WHERE nombre = 'Administrador'), (SELECT id FROM permisos WHERE nombre = 'eliminar_producto')),
((SELECT id FROM roles WHERE nombre = 'Administrador'), (SELECT id FROM permisos WHERE nombre = 'listar_productos')),
((SELECT id FROM roles WHERE nombre = 'Administrador'), (SELECT id FROM permisos WHERE nombre = 'crear_usuario')),
((SELECT id FROM roles WHERE nombre = 'Administrador'), (SELECT id FROM permisos WHERE nombre = 'leer_usuario')),
((SELECT id FROM roles WHERE nombre = 'Administrador'), (SELECT id FROM permisos WHERE nombre = 'actualizar_usuario')),
((SELECT id FROM roles WHERE nombre = 'Administrador'), (SELECT id FROM permisos WHERE nombre = 'eliminar_usuario')),
((SELECT id FROM roles WHERE nombre = 'Administrador'), (SELECT id FROM permisos WHERE nombre = 'listar_usuarios')),
((SELECT id FROM roles WHERE nombre = 'Administrador'), (SELECT id FROM permisos WHERE nombre = 'registrar_venta')),
((SELECT id FROM roles WHERE nombre = 'Administrador'), (SELECT id FROM permisos WHERE nombre = 'listar_ventas'));

-- Permisos para Vendedor
INSERT INTO rol_permiso (rol_id, permiso_id) 
VALUES 
((SELECT id FROM roles WHERE nombre = 'Vendedor'), (SELECT id FROM permisos WHERE nombre = 'ver_producto')),
((SELECT id FROM roles WHERE nombre = 'Vendedor'), (SELECT id FROM permisos WHERE nombre = 'registrar_venta')),
((SELECT id FROM roles WHERE nombre = 'Vendedor'), (SELECT id FROM permisos WHERE nombre = 'listar_ventas'));

-- Insertar usuarios
INSERT INTO usuarios (nombre, username) VALUES ('Admin User', 'admin');
INSERT INTO usuarios (nombre, username) VALUES ('Vendedor User', 'vendedor');

-- Asociar usuarios con roles
-- Asignar rol Administrador al usuario admin
INSERT INTO usuario_rol (usuario_id, rol_id) 
VALUES ((SELECT id FROM usuarios WHERE username = 'admin'), (SELECT id FROM roles WHERE nombre = 'Administrador'));

-- Asignar rol Vendedor al usuario vendedor
INSERT INTO usuario_rol (usuario_id, rol_id) 
VALUES ((SELECT id FROM usuarios WHERE username = 'vendedor'), (SELECT id FROM roles WHERE nombre = 'Vendedor'));