CREATE DATABASE IF NOT EXISTS TAREA5DI
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_spanish2_ci;


USE TAREA5DI;

-- Crear tablas con utf8mb4
CREATE TABLE usuarios (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    contrasenia VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
);

CREATE TABLE tipos_reservas (
    tipo_reserva_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    requiere_jornadas TINYINT(1) NOT NULL DEFAULT 0,
    requiere_habitaciones TINYINT(1) NOT NULL DEFAULT 0
);

CREATE TABLE tipos_cocina (
    tipo_cocina_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
);

CREATE TABLE salones (
    salon_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
);

CREATE TABLE clientes (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    Apellidos VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    Num_Identificacion VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL UNIQUE,
    Fec_Nac DATE,
    Pais VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    Telefono VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    email VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    Sexo VARCHAR(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    Menores INT
);

CREATE TABLE reservas (
    reserva_id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_reserva_id INT NOT NULL,
    salon_id INT NOT NULL,
    tipo_cocina_id INT NOT NULL,
    id_cliente INT NOT NULL,
    fecha DATE NOT NULL,
    ocupacion INT NOT NULL,
    jornadas INT NOT NULL,
    habitaciones INT NOT NULL DEFAULT 0,
    FOREIGN KEY (id_cliente) REFERENCES clientes(Id),
    FOREIGN KEY (salon_id) REFERENCES salones(salon_id),
    FOREIGN KEY (tipo_cocina_id) REFERENCES tipos_cocina(tipo_cocina_id),
    FOREIGN KEY (tipo_reserva_id) REFERENCES tipos_reservas(tipo_reserva_id),
    UNIQUE (salon_id, fecha)
);

SET FOREIGN_KEY_CHECKS=0;

-- Insertar datos en tablas base

INSERT INTO usuarios (usuario, contrasenia) VALUES
('valentina', 'secreta'),
('hotel', 'Brianda23$');

INSERT INTO tipos_reservas (nombre, requiere_jornadas, requiere_habitaciones) VALUES
('Banquete', 0, 0),
('Jornada', 0, 0),
('Congreso', 1, 1);

INSERT INTO tipos_cocina (nombre) VALUES
('Bufé'),
('Carta'),
('Pedir cita con el chef'),
('No precisa');

INSERT INTO salones (nombre) VALUES
('Salón Habana'),
('Otro Salón');

INSERT INTO clientes (Nombre, Apellidos, Num_Identificacion, Fec_Nac, Pais, Telefono, email, Sexo, Menores) VALUES
('Iván', 'Cuartango Del Río', '2W', '2003-08-02', 'España', '416568265', 'icuartan@gmail.com', 'H', 1),
('María Azucena', 'García Mayor', '3A', '2003-06-13', 'España', '602724480', 'mgarcía@gmail.com', 'M', 1),
('Álvaro', 'Gómez Tejada', '4G', '2006-09-11', 'Reino Unido', '721376842', 'ágómez t@gmail.com', 'H', 0),
('Adrián', 'Gregorio Ortiz', '5M', '2005-02-07', 'Nigeria', '659641230', 'agregori@gmail.com', 'H', 0),
('Alonso', 'Guerrero García', '6Y', '1983-09-06', 'Somalia', '1697052230', 'aguerrer@gmail.com', 'H', 0),
('Bilal', 'Hamdach El Amri', '7F', '2002-10-16', 'Tailandia', '393331228', 'bhamdach@gmail.com', 'M', 1),
('Sergio', 'Lapeña Martínez', '8P', '2006-07-17', 'Irán', '726568228', 'slapeña@gmail.com', 'H', 0),
('Pablo', 'Menéndez Mendoza', '9D', '1991-04-08', 'España', '222837147', 'pmenénde@gmail.com', 'H', 0),
('DanielA', 'Monje Malvar', '10X', '2004-05-31', 'Colombia', '1357985817', 'dmonje m@gmail.com', 'M', 0),
('Javier', 'Muela Mazarío', '11B', '2006-04-21', 'USA', '726775466', 'jmuela m@gmail.com', 'N', 0),
('Raimundo Jesús Atuba', 'Nguema Ayetebe', '12N', '2003-07-08', 'España', '474131221', 'rnguema@gmail.com', 'N', 1),
('César', 'Nicolás Carrascosa', '13J', '2000-02-26', 'España', '497856212', 'cnicolás@gmail.com', 'H', 1),
('Borislav', 'Nikolaev Mladenov', '14Z', '2005-04-25', 'Países Bajos', '630812215', 'bnikolae@gmail.com', 'M', 1),
('Sergio', 'Romero Tejedor', '15S', '2004-01-03', 'México', '1629071747', 'sromero@gmail.com', 'H', 1),
('David', 'Vargas Del Santo', '16Q', '2006-11-16', 'Reino Unido', '703998180', 'dvargas@gmail.com', 'H', 0),
('Diego', 'Barroso Torres', '1R', '2006-07-28', 'España', '711133226', 'dbarroso@gmail.com', 'H', 0);

-- Insertar datos en reservas
INSERT INTO reservas (tipo_reserva_id, salon_id, tipo_cocina_id, id_cliente, fecha, ocupacion, jornadas, habitaciones) VALUES
(1, 1, 1, 1, '2024-12-20', 35, 0, 0),
(2, 2, 2, 2, '2025-01-14', 2, 0, 0),
(1, 2, 1, 3, '2025-01-17', 1, 0, 0),
(2, 2, 1, 4, '2025-01-20', 3, 0, 0),
(1, 1, 2, 5, '2024-11-20', 35, 0, 0),
(1, 1, 1, 6, '2024-11-21', 3, 0, 0),
(3, 2, 3, 7, '2025-01-10', 2, 0, 0),
(1, 1, 1, 8, '2024-10-21', 1, 0, 0),
(1, 2, 1, 9, '2025-01-13', 1, 0, 0),
(3, 1, 2, 10, '2024-12-01', 3, 1, 1),
(2, 1, 2, 11, '2024-10-01', 5, 0, 0),
(2, 1, 2, 12, '2024-10-02', 5, 0, 0),
(1, 1, 2, 14, '2024-12-25', 3, 0, 0),
(2, 2, 1, 15, '2025-01-23', 3, 0, 0),
(2, 2, 1, 10, '2024-12-27', 4, 0, 0),
(2, 2, 3, 17, '2025-01-22', 4, 0, 0);

SET FOREIGN_KEY_CHECKS=1;

