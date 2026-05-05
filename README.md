# Proyecto Urban Grocers - API Testing

## Descripción

Este proyecto contiene una suite de pruebas automatizadas para validar la API de Urban Grocers, una aplicación web para realizar pedidos de comida.

El objetivo principal del proyecto es verificar la creación de kits de productos y validar el comportamiento del campo `name` usando diferentes escenarios positivos y negativos.

## Tecnologías utilizadas

- Python
- Pytest
- Requests
- Git
- GitHub

## Funcionalidad probada

La suite valida el endpoint de creación de kits de productos.

Se prueban escenarios relacionados con el campo `name`, incluyendo:

- Nombre válido
- Nombre con longitud mínima permitida
- Nombre con longitud máxima permitida
- Nombre vacío
- Nombre con más caracteres de los permitidos
- Nombre con caracteres especiales
- Nombre con espacios
- Nombre con números
- Ausencia del parámetro `name`
- Tipo de dato incorrecto en `name`

## Estructura del proyecto

```txt
.
├── configuration.py
├── data.py
├── sender_stand_request.py
├── create_kit_name_kit_test.py
├── README.md
└── .gitignore