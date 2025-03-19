# Clase Tablero
# In:
# Dimensiones del Tablero, Flota

# Variables Propias de la clase
# Tablero con ubicaciones de flota propia.
# Tablero de impactos al rival
#
# Metodos
# Variables -- > IN Crear tableros Output -->
# Recibir disparo
#


# Clase Usuario
# In:
# Flota
# Tableros

# Variables Propias de la clase:
# Nombre
# Password
# Nivel = Disparos Acertados / Total Disparos
# Tableros Partida en curso
# Contador Disparos Acertados
# Contador Total de Disparo
# Contador Disparos Acertados Partida Actual
# Contador Total de Disparo Partida Actual
# Estado de Flota
#   - Ubicación y tamaño de los barcos 
#   - Estado actual de la flota
# 
# Lista de partidas guardadas.
# Indicador de Partida en Curso

# Metodos de la Clase
# Incluir nuevo usuario
# Loggearse como usuario
#   - Comprobar si el usuario existe pidiendo el password
#   - Ver si tiene un partida en curso y preguntar si quiere reiniciarla.
# Ver estado de la flota.
# Ver partidas jugadas
# 
#
#





# Clase Partidas
# In:
# Usuario Tablero 1, Tablero 1, Usuario Tablero 2, Tablero 2
# Variables Propias de la clase
# Turno (Tira Jugador 1 o Jugador 2)
# Contador Disparos Acertados Partida Actual x Jugador
# Contador Total de Disparo Partida Actual   x Jugador
# Estado de Flota  x Jugador
#     - Ubicación y tamaño de los barcos 
#     - Estado actual de la flota
# Lista de partidas guardadas.
# Indicador de Partida en Curso
#
# Metodos
# Gestionar registro de usuarios
#   - Comprobar usuario nuevo
#   - Ver si tiene partidas guardadas en curso y decidir entre partida nueva o continuar con la partida en curso.
#   - Si es partida nueva crear tableros para ambos jugadores.
#   - Si continua partida prepara tableros de ambos jugadores con la partida en curso.
# Gestion de los turnos:
#   - Jugador 1 tira:
#   - Jugador 2 tira
# Ver datos partida en curso:
#   - Mostrar estado de la flota de los jugadores en curso
#   - 

# Funcion para simular al jugador 2
# Elegir nivel de difilcultad:
#   - Nivel bajo --> Unico disparo random
#   - Nivel medio --> Varios disparos random
#   - Nivel alto --> - Tener en cuenta los tocados para generar los numeros aleatorios en un rango.
#                    - Cuando tenemos dos tocados seguir trayectoria de disparos

