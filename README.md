# Smart Band API

## Autores: Diego Pardo y Pablo Sandoval
## Introducción

Para hacer uso de la API de manera local es necesario realizar los siguientes pasos:

1) Ingresar los siguiente comandos en consola:

```python
python3 -m venv [nombreDelEntornoVirtual]
```

este comando les creara un entorno virtual para para poder importar posteriormente los paquetes ahi.Para activarlo se emplea el siguiente comando:

```python
source nombreDelEntornoVirtual/bin/activate
```

y para apagarlo:

```python
deactivate
```

2) despues correr el siguiente comando para obtener los paquetes empleados en la API:

```python
pip install -r requirements.txt
```


3) crear un archivo .env dentro del repositorio que debe contener el siguiente patron:
```docker
DB_USER=[NOMBRE DE USUARIO]
DB_PASSWORD=[CONTRASEÑA]
DB_HOST=localhost:[PUERTO]
DB_NAME=[NOMBRE DE LA BASE DE DATOS]
```
Esto es para emplear que la API se pueda conectar con la base de datos de manera apropiada.
Si se desease crear y usar una base  datos en docker se puede realizar corriendo el siguiente comando:
```docker
docker run --name [NOMBRE DEL CONTENEDOR] -e POSTGRES_PASSWORD=[CONTRASEÑA] -p [PUERTO]:[PUERTO] -d [NOMBRE DE USUARIO]
```