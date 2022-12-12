
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
  git clone https://github.com/J1jo/Talana-Kombat.git
```

### 2.- Obtener imagen

```bash
  docker pull jijoo/talana-kombat
```

### 3.- Casos de prueba

En la raíz se encuentra un archivo llamado `fight_script.json`, desde el cual se obtienen los datos para la pelea. Para probar diferentes casos es necesario modificar este archivo.
## Ejecutar pruebas

*Para poder ejecutar las pruebas deberá ejecutar el siguiente comando*

```bash
  docker run jijoo/talana-kombat
```

