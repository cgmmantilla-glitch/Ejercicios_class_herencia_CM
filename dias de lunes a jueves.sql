CREATE TABLE lunes (
    id SERIAL PRIMARY KEY,
    actividades VARCHAR(100)
);

CREATE TABLE martes (
    id SERIAL PRIMARY KEY,
    actividades VARCHAR(100)
);

CREATE TABLE miercoles (
    id SERIAL PRIMARY KEY,
    actividades VARCHAR(100)
);

CREATE TABLE jueves (
    id SERIAL PRIMARY KEY,
    actividades VARCHAR(100)
);


INSERT INTO lunes (actividades)
VALUES
('Ir al instituto'),
('Hacer tareas');

INSERT INTO martes (actividades)
VALUES
('Jugar voley'),
('Descansar');

INSERT INTO miercoles (actividades)
VALUES
('Pasar tiempo con mi novecita'),
('Realizar ejercicios');

INSERT INTO jueves (actividades)
VALUES
('Estudiar POO'),
('Activacion de Flask');

select*from lunes
select*from martes
select*from miercoles
select*from jueves