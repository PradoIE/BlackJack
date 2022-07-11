Elaborado por:
  Shannon Torres
  Alonso Prado
  Andrés Vega


Introducción y funcionamiento:
El programa a ejecutar corresponde a blackjack_GUI.py.
El juego comienza en un menú principal donde se puede decidir entre tres opciones: 
  1. Iniciar la partida
  2. Ver puntuaciones más altas
  3. Salir del juego 
  
1. Cuando se inicia la partida el jugador selecciona la cantidad de fichas por apostar, tiene botones para comer una carta o quedarse. El objetivo es
acercarse lo más posible a 21 sin sobrepasarse. Cuando el jugador deja de comer y pasa a ser turno del dealer, este come hasta que su mano tenga un valor
de 17 o más. Gana el jugador cuya mano tenga un mayor valor sin sobrepasar 21.
Luego de que se verifica el ganador se puede empezar otra mano y empezar nuevamente o Finalizar el juego y volver al menu principal.

2. La pantalla de puntuaciones más altas muestra una lista con las cantidades de fichas que tenía el jugador a la hora de finalizar el juego. 

3. Sale del juego.

Intrucciones para ejecutar:

El archivo blackjack_GUI.py debe estar al mismo nivel que una carpeta llamada "imagenes", donde está la imagen de fondo y otra carpeta llamada "cartas",
donde están todas las cartas que se usan en el juego. 
El directorio debe tener esta estructura: 
  blackjack_GUI.py
  imagenes
    fondo.jpg
    cartas
      As_Corazones
      As_Diamantes
      ...
