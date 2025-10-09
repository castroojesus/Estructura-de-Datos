
//PRIMERA REVISION 26/09/25
//ULTIMA REVISION 06/10/25


import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class BATALLANAVAL {
    
    final static int TamFilas = 14; //constante del tamaño de las filas
    final static int TamColumns = 6;
    
    static class Posicion {  //clase para calcular las coordenadas de los barcos
        int x, y;  
        
        public Posicion() {}
        public Posicion(int x, int y) {
            this.x = x; //atributo para las cordenadas de las filas
            this.y = y; //atributo para las coordenadas de las columnas
        }
    }

    static class Tablero { //clase para poder darle un tablero para poner las posiciones a cada jugador
        char[][] TABLERO = new char[TamFilas][TamColumns]; //matriz tablero que mide 14x6
        List<Barco> barcos = new ArrayList<>(); //lista para manejar el control de los barcos
        int CantBarcos = 0; //contador de cuantos barcos se van agregando
        
        //funcion para Inicializar tablero
        public void IniciaTab() { 
            for(int i = 0; i < TamFilas; i++) {
                for(int j = 0; j < TamColumns; j++) {
                    TABLERO[i][j] = '~';
                }
            }
            barcos.clear(); //cada juego nuevo me limpia la lista de barcos
            CantBarcos = 0; //y me reinicia el contador
        }
        
        //funcion para verificar que los barcos se hayan agregado correctamente
        public boolean agregarBarco(Barco barco) {
            //verificar si los barcos estan fuera de los limites o que no se sobrepongan
            for (Posicion pos : barco.posiciones) {
                if (pos.x < 0 || pos.x >= TamFilas || pos.y < 0 || pos.y >= TamColumns) {
                    return false; // fuera de límites
                }
                if (TABLERO[pos.x][pos.y] != '~') {
                    return false; // posición ocupada
                }
            }
            
            //agregar los barcos en las coordenadas que diga el usuario
            for (Posicion pos : barco.posiciones) {
                TABLERO[pos.x][pos.y] = 'B';
            }
            
            barcos.add(barco); //se van agregando los barcos
            CantBarcos++; //aumenta el contador
            return true;
        }
        
        // funcion para mostrar el tablero
        public void mostrarTableroCompleto() {
            System.out.println("\n  0 1 2 3 4 5");
            
            for (int i = 0; i < TamFilas; i++) {
                System.out.print(i + " ");
                for (int j = 0; j < TamColumns; j++) {
                    System.out.print(TABLERO[i][j] + " ");
                }
                System.out.println();
                
                if (i == 6) {
                    System.out.println("----------------------");
                }
            }
        }
     // Método para mostrar tablero durante el juego (oculta barcos)
        public void mostrarTableroJuego() {
            System.out.println("\n  0 1 2 3 4 5");
            
            for (int i = 0; i < TamFilas; i++) {
                System.out.print(i + " ");
                for (int j = 0; j < TamColumns; j++) {
                    // Si es un barco que no ha sido impactado, mostrar como agua
                    if (this.TABLERO[i][j] == 'B') {
                        System.out.print("~ "); // Oculta los barcos, muestra como agua
                    } else {
                        System.out.print(this.TABLERO[i][j] + " "); // Muestra impactos (X) y agua (O)
                    }
                }
                System.out.println();
                
                if (i == 6) {
                    System.out.println("----------------------");
                }
            }
        }
    }
    
    //clase para cada barco
    static class Barco {
        String nombre; //atributo de nombre
        int tamaño; //tamaño
        boolean esHorizontal; //verificar si es horizontal
        Posicion start; //en que posicion va a iniciar
        List<Posicion> posiciones; //lista de posiciones para los barcos
        
        public Barco(String nombre, int tamaño) {
            this.nombre = nombre;
            this.tamaño = tamaño;
            this.esHorizontal = true;
            this.posiciones = new ArrayList<>();
        }
        
        // funcion para calcular la posicion de los barcos
        public void calcularPosiciones() {
            posiciones.clear(); //me limpia la lista cada juego nuevo
            for (int i = 0; i < this.tamaño; i++) {
                Posicion pos = new Posicion(); //variable temporal para el calculo
                if (this.esHorizontal) { //si el barco es horizontal
                    pos.x = this.start.x; //la fila en la que inicia se mantiene
                    pos.y = this.start.y + i; //y aumenta en columnas [(2,1),(2,2),(2,3)]
                } else {
                    pos.x = this.start.x + i; //aumenta en filas [(2,1),(3,1),(4,1)]
                    pos.y = this.start.y; //se queda en columnas
                }
                posiciones.add(pos); //se agrega la nueva posicion en la lista posiciones
            }
        }
        
        //funcion para rotar la orientacion del barco
        public void rotar() {
            this.esHorizontal = !this.esHorizontal;
            if (this.start != null) {
                calcularPosiciones();
            }
        }
    }
    
    //funcion para mostrarle al jugador el barco que tiene que agregar
    public static void ColocarBarco(Scanner scanner, Barco[] barcos, int jugador, Tablero tablero) {
        System.out.print("\n=== JUGADOR " + jugador + " ===  ->  Coloca tus barcos: ");
        
        //contador para cuando llegue a 5 limpie el tablero asi el otro jugador no sepa donde estan los barcos
        int barcosColocados = 0;
        
        for (int i = 0; i < barcos.length; i++) {
            Barco barco = barcos[i];
            boolean colocado = false;
            
            while (!colocado) {
                int fila, columna;
                
                // Mensajes específicos para cada jugador según su rango de filas
                if (jugador == 1) {
                    System.out.print("\nJUGADOR " + jugador + " Ingresa FILA (7-13) para " + barco.nombre + " ("+barco.tamaño+") Casillas: ");
                    fila = scanner.nextInt();
                    System.out.print("JUGADOR " + jugador + " Ingresa COLUMNA (0-5) para " + barco.nombre + " ("+barco.tamaño+") Casillas: ");
                    columna = scanner.nextInt();
                    
                    // Validar zona de colocación para jugador 1
                    if ((fila < 7 || fila > 13)||(columna<0||columna>5)) {
                        System.out.println("Jugador 1 solo puede colocar barcos en las filas 7-13 y columnas 0-5. Intenta de nuevo.");
                        continue; 
                    }
                    
                } else { // jugador == 2
                    System.out.print("\nJUGADOR " + jugador + " Ingresa FILA (0-6) para " + barco.nombre + " ("+barco.tamaño+") Casillas: ");
                    fila = scanner.nextInt();
                    System.out.print("JUGADOR " + jugador + " Ingresa COLUMNA (0-5) para " + barco.nombre + " ("+barco.tamaño+") Casillas: ");
                    columna = scanner.nextInt();
                    
                    // Validar zona de colocación para jugador 2
                    if ((fila < 0 || fila > 6)||(columna<0||columna>5)) {
                        System.out.println("Jugador 2 solo puede colocar barcos en las filas 0-6 y columnas 0-5. Intenta de nuevo.");
                        continue; 
                    }
                }
                
                scanner.nextLine(); // limpiar buffer
                
                barco.start = new Posicion(fila, columna);
                
                System.out.println("Quieres mantener el barco horizontal o vertical? H)HORIZONTAL y V)VERTICAL: ");
                String answer = scanner.next();
                answer = answer.toUpperCase().trim();
                
                if ((answer.equals("V") && barco.esHorizontal) || (answer.equals("H") && !barco.esHorizontal)) {
                    barco.rotar();
                }
                
                barco.calcularPosiciones();
                
                if (tablero.agregarBarco(barco)) {
                    colocado = true;
                    barcosColocados++; // Incrementar contador
                    System.out.println(barco.nombre + " colocado correctamente.");
                    System.out.print("Así queda tu tablero: ");
                    tablero.mostrarTableroCompleto();
                    
                    // Verificar si ya colocó todos los barcos
                    if (barcosColocados == barcos.length) {
                        System.out.println("\n\nJUGADOR "+ jugador+ " ¡Has colocado todos tus barcos!");
                        
                        mostrarTableroLimpio();
                    }
                } else {
                    System.out.println("Posición inválida, ocupada o fuera de rango intenta de nuevo.");
                }
            }
        }
    }
    
    //funcion para los diparos de cada jugador, usando como base la funcion de colocar barcos
    //donde uso como parametro el tablero del enemigo y otro para saber donde ya ataque y donde no
    public static void disparos(Scanner scanner, int jugador, Tablero tableroEnemigo, Tablero tableroPropio) {
        System.out.print("\n=== TURNO DEL JUGADOR " + jugador + " ===");
        
        boolean turnoActivo = true; //variable booleana para saber si el turno del jugador actual ya paso o no
        
        while (turnoActivo) {//mientras sea true
            System.out.println("\n--- Disparo del Jugador " + jugador + " ---");
            
            boolean disparoValido = false; //variable para verificar ya hice mi disparo 
            int fila = -1, columna = -1;
            
            while (!disparoValido) { //turno del jugador 1 hasta que disparoValido sea false
                if (jugador == 1) {
                    System.out.print("Ingresa FILA (0-6) para atacar: ");
                    fila = scanner.nextInt();
                    System.out.print("Ingresa COLUMNA (0-5) para atacar: ");
                    columna = scanner.nextInt();
                    
                    if ((fila < 0 || fila > 6)||(columna<0||columna>5)) {
                        System.out.println("Solo puedes atacar en las filas 0-6 y columnas 0-5. Intenta de nuevo.");
                        continue; 
                    }
                    
                } else {
                    System.out.print("Ingresa FILA (7-13) para atacar: ");
                    fila = scanner.nextInt();
                    System.out.print("Ingresa COLUMNA (0-5) para atacar: ");
                    columna = scanner.nextInt();
                    
                    if ((fila < 7 || fila > 13)||(columna<0||columna>5)) {
                        System.out.println("Solo puedes atacar en las filas 7-13 y columnas 0-5. Intenta de nuevo.");
                        continue; 
                    }
                }
                
                scanner.nextLine();
                
                // Verificar si ya disparó en las coordenadas ingresadas
                if (tableroPropio.TABLERO[fila][columna] == 'X' || tableroPropio.TABLERO[fila][columna] == 'O') {
                    System.out.println("Ya disparaste aquí. Elige otra posición.");
                    continue;
                }
                
                disparoValido = true;
            }
            
            // verificar si el disparo en el tablero enemigo es igual a b que lo marque como x
            if (tableroEnemigo.TABLERO[fila][columna] == 'B') {
                System.out.println("\n¡IMPACTO! Has golpeado un barco enemigo.");
                tableroPropio.TABLERO[fila][columna] = 'X'; // Marcar impacto
                tableroEnemigo.TABLERO[fila][columna] = 'X'; // También marcar en el tablero enemigo
                
             
                
                // Mostrar resultado
                System.out.println("\nTu tablero de disparos:");
                tableroPropio.mostrarTableroJuego();
                
                // Verificar si el juego terminó
                if (verificarVictoria(tableroEnemigo)) {
                    System.out.println("¡¡¡JUGADOR " + jugador + " GANA LA BATALLA!!!");
                    return; // Terminar el juego
                }
                
                
             // Verificar si el barco fue hundido completamente
                if (verificarBarcoHundido(tableroEnemigo)) {
                    System.out.println("\n¡¡¡BARCO HUNDIDO!!!");
                }
                // Si fue impacto, sigue en el mismo turno
                System.out.println("¡Ganas otro disparo!");
                
            } else {
                System.out.println("¡AGUA! No hay ningún barco en esa posición.");
                tableroPropio.TABLERO[fila][columna] = 'O'; // Marcar agua
                
                // Mostrar resultado
                System.out.println("Tu tablero de disparos:");
                tableroPropio.mostrarTableroJuego();
                
                // Si fue agua, termina el turno
                System.out.println("Turno terminado. Pasando al siguiente jugador...");
                turnoActivo = false;
            }
        }
    }
 // Método para verificar si algún barco fue hundido completamente
    public static boolean verificarBarcoHundido(Tablero tablero) {
        for (Barco barco : tablero.barcos) {
            boolean barcoHundido = true;
            // Verificar si todas las posiciones del barco han sido impactadas
            for (Posicion pos : barco.posiciones) {
                if (tablero.TABLERO[pos.x][pos.y] != 'X') {
                    barcoHundido = false; // Todavía hay partes del barco sin impactar
                    break;
                }
                	
                }
            if (barcoHundido) {
            	return true;
            }
            
        }
        return false; // Ningún barco hundido
    }
    // Solo mantener la función de verificar victoria
    public static boolean verificarVictoria(Tablero tablero) {
        // Verificar si todos los barcos han sido hundidos
        for (Barco barco : tablero.barcos) {
            for (Posicion pos : barco.posiciones) {
                if (tablero.TABLERO[pos.x][pos.y] == 'B') {
                    return false; // Todavía hay barcos con partes sin impactar
                }
            }
        }
        return true; // Todos los barcos hundidos
    }
    
    public static void mostrarTableroLimpio() {
        System.out.println("\n  0 1 2 3 4 5");
        
        for (int i = 0; i < TamFilas; i++) {
            System.out.print(i + " ");
            for (int j = 0; j < TamColumns; j++) {
                System.out.print("~ "); // Siempre muestra olas, sin importar lo que haya en el tablero real
            }
            System.out.println();
            
            if (i == 6) {
                System.out.println("----------------------");
            }
        }
    }
    

    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        //creo los tableros para cada jugador
        Tablero tableroJ1 = new Tablero();
        Tablero tableroJ2 = new Tablero();
        tableroJ1.IniciaTab();
        tableroJ2.IniciaTab();
        
        Tablero referenciaJ1 = new Tablero();
        Tablero referenciaJ2 = new Tablero();
        referenciaJ1.IniciaTab();
        referenciaJ2.IniciaTab();
        
        //barcos para jugador 1
        Barco[] barcosj1 = {
            new Barco("PortaAviones", 5),
            new Barco("Acorazado", 4),
            new Barco("Destructor", 3),
            new Barco("Submarino", 3),
            new Barco("Lancha", 2)
        };
        
        //barcos para jugador 2
        Barco[] barcosj2 = {
            new Barco("PortaAviones", 5),
            new Barco("Acorazado", 4),
            new Barco("Destructor", 3),
            new Barco("Submarino", 3),
            new Barco("Lancha", 2)
        };
        
        //llamo a la funcion de colocar los barcos para cada jugador
        ColocarBarco(scanner, barcosj1, 1, tableroJ1);
        ColocarBarco(scanner, barcosj2, 2, tableroJ2);
        System.out.println("Todos los barcos han sido colocados, que comience la batalla");
        
        boolean fin = false;
        int jugadorActual = 1;
        
        while (!fin) {
            if (jugadorActual == 1) {
                disparos(scanner, 1, tableroJ2, referenciaJ1);
                if (!verificarVictoria(tableroJ2)) {
                    jugadorActual = 2;
                } else {
                    fin = true;
                }
            } else {
                disparos(scanner, 2, tableroJ1, referenciaJ2);
                if (!verificarVictoria(tableroJ1)) {
                    jugadorActual = 1;
                } else {
                    fin = true;
                }
            }
        }
        
        

        scanner.close();
    }
}