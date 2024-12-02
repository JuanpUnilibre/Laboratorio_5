--- 01-12-2024 19:13:27
--- SQLite
CREATE TABLE Estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(50),
    edad INTEGER,
    ciudad VARCHAR(50)
);

--- 01-12-2024 19:17:46
--- SQLite
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES
('Juan Pablo', 22, 'Santa Marta'),
('Tyrone Gonzales', 19, 'Mérida'),
('Lionel Messi', 21, 'Rosario'),
('Juan Martínez', 20, 'Valencia'),
('Laura Sánchez', 23, 'Madrid');

--- 01-12-2024 19:18:01
--- SQLite
SELECT * FROM Estudiantes;

--- 01-12-2024 19:19:32
--- SQLite
SELECT * FROM Estudiantes WHERE ciudad = 'Rosario';

--- 01-12-2024 19:20:46
--- SQLite
SELECT * FROM Estudiantes WHERE edad > 20;

