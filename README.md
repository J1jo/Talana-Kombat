
# TalanaKombat

TalanaKombat es un simulador de pelea text-based de dos jugadores donde Tonnyn Stallone y Arnaldor Schuatseneger se enfrentan a muerte!




## Como Funciona:

- Cada jugador empieza con 6 puntos de energia.
- Empieza el jugador con menor cantidad de movimientos
- La pelea transcurre en base a turnos y termina cuando uno se queda sin energia.
- Cada jugador tiene 2 habilidades especiales y 2 golpes basicos.



## Prerrequisitos

- Docker
- Clonar el repositorio

## Como ejecutar el proyecto?

### 1.- Debes clonar el proyecto

```bash
  git clone https://github.com/J1jo/SII_api.git
```

### 2.- Crear ambiente virtual

```bash
  python -m venv env
  env\Scripts\activate
```

### 3.- Casos de prueba

En la raíz se encuentra una carpeta llamada `tests` dentro de ella un archivo llamado `test_api.py`, desde el cual se hacen pruebas unitarias. Para probar diferentes casos es necesario modificar este archivo.
## Ejecutar pruebas

*Para poder ejecutar las pruebas deberá ejecutar el siguiente comando*

```bash
  python -m unittest discover -s tests/
```

