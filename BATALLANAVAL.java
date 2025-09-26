//PRIMERA REVISION 26/09/25


import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class BATALLANAVAL {
    
    final static int TamTableros = 20; //constante del tamaño de las filas
    
    
    static class Posicion {  //clase para calcular las coordenadas de los barcos
        int x, y;  
        
        public Posicion() {}
        public Posicion(int x, int y) {
            this.x = x; //atributo para las cordenadas de las filas
            this.y = y; //atributo para las coordenadas de las columnas
        }
    }

    static class Tablero { //clase para poder darle un tablero para poner las posiciones a cada jugador
        char[][] TABLERO = new char[TamTableros][10]; //matriz tablero que mide 20x10
        List<Barco> barcos = new ArrayList<>(); //hago una lista para manejar el control de los barcos que se van agregando
        int CantBarcos = 0; //contador de cuantos barcos se van agregando
        
        //funcion para Inicializar tablero
        public void IniciaTab() { 
            for(int i = 0; i < TamTableros; i++) {
                for(int j = 0; j < 10; j++) {
                    TABLERO[i][j] = '~';
                }
            }
            barcos.clear(); //cada juego nuevo me limpia la lista de barcos
            CantBarcos = 0; //y me reinicia el contador
        }
        
       //funcion para verificar que los barcos se hayan agregado los barcos correctamente
        public boolean agregarBarco(Barco barco) {
            //verificar si los barcos estan fuera de los limites o que no se sobrepongan entre si
            for (Posicion pos : barco.posiciones) {
                if (pos.x < 0 || pos.x >= TamTableros || pos.y < 0 || pos.y >= 10) {
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
        
        // funcion para mostrar el tablero en vez de escribirlo varias veces con ciclos
        public void mostrarTableroCompleto() {
            System.out.println("\n  0 1 2 3 4 5 6 7 8 9");
            
            for (int i = 0; i < TamTableros; i++) {
                System.out.print(i + " ");
                for (int j = 0; j < 10; j++) {
                    System.out.print(TABLERO[i][j] + " ");
                }
                System.out.println();
                
                if (i == 9) {
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
        Object estructura; //el tipo de estructura que tiene para la rotacion
        List<Posicion> posiciones; //lista de posiciones para ir agregando en donde quedan los barcos
        
        public Barco(String nombre, int tamaño) {
            this.nombre = nombre;
            this.tamaño = tamaño;
            this.esHorizontal = true;
            this.posiciones = new ArrayList<>();
            this.estructura = new char[tamaño];
            
        }
        
        
        public List<Posicion> getPosiciones() {
            return this.posiciones;
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
        
        
        //funcion para rotar la orientacion y estructura del barco
        public void rotar() {
            if (this.esHorizontal) { //si es horizontal
                char[] vector = (char[]) this.estructura; //declaro variable temporal para trabajar con la estructura
                char[][] matriz = new char[this.tamaño][1]; //la modifico a matriz para poder mover los elementos en columna
                for (int i = 0; i < this.tamaño; i++) {
                    matriz[i][0] = vector[i];
                }
                this.estructura = matriz;
            } else {
                char[][] matriz = (char[][]) this.estructura;
                char[] vector = new char[this.tamaño];
                for (int i = 0; i < this.tamaño; i++) {
                    vector[i] = matriz[i][0];
                }
                this.estructura = vector;
            }
            this.esHorizontal = !this.esHorizontal;
            if (this.start != null) {
                calcularPosiciones();
            }
        }
    }
    
    
    //funcion para mostrarle al jugador el barco que tiene que agregar, tamaño que necesita, que lea los inputs y calcules las posiciones
    public static void ColocarBarco(Scanner scanner, Barco[] barcos, int jugador, Tablero tablero) {
        System.out.print("\n=== JUGADOR " + jugador + " ===  ->  Coloca tus barcos: ");
        
        for (int i = 0; i < barcos.length; i++) {
            Barco barco = barcos[i];
            boolean colocado = false;
            
            while (!colocado) {
                System.out.print("\nJUGADOR " + jugador + " Ingresa FILA (0-19) para " + barco.nombre + " ("+barco.tamaño+") Casillas: ");
                int fila = scanner.nextInt();
                System.out.print("JUGADOR " + jugador + " Ingresa COLUMNA (0-9) para " + barco.nombre + " ("+barco.tamaño+") Casillas:");
                int columna = scanner.nextInt();
                scanner.nextLine();
                
                
                if (jugador == 1 && fila < 10) {
                    System.out.println("Jugador 1 solo puede colocar barcos a partir de la fila 10. Intenta de nuevo.");
                    continue; 
                }
                
                if (jugador == 2 && fila >= 10) {
                    System.out.println("Jugador 2 solo puede colocar barcos hasta la fila 9. Intenta de nuevo.");
                    continue; 
                }
                
                barco.start = new Posicion(fila, columna);
                
                
               
                
                System.out.println("Quieres mantener el barco horizontal o vertical? H)HORIZONTAL y V)VERTICAL: ");
                String answer = scanner.next();
                answer=answer.toUpperCase().trim();
                
                if ((answer.equals("V") && barco.esHorizontal) || (answer.equals("H") && !barco.esHorizontal)) {
                    barco.rotar();
                }
                
                barco.calcularPosiciones();
                
                if (tablero.agregarBarco(barco)) {
                	
                    colocado = true;
                    System.out.println(barco.nombre + " rotado correctamente.");
                    System.out.print("Así queda tu tablero: ");
                    tablero.mostrarTableroCompleto(); 
                } else {
                    System.out.println("Posición inválida o ocupada, intenta de nuevo.");
                }
                
                
               
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

        
        
        scanner.close();
    }
}	