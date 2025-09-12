#include <iostream>
using namespace std;


int main()
{
		
	string name1, name2;
	char answer='S';
	
	while (answer == 'S' || answer == 's') {

		char GATO[3][3];
		char k = '1';
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				GATO[i][j] = k;
				k++;
			}
		}
		
		int fila, columna;
		int turno = 0;
		bool ganador = false;
		int jugadas;
		char jugadaAct;

		cout << "Jugador 1 ingrese su nombre: ";
		cin >> name1;
		cout << "Jugador 2 ingrese su nombre: ";
		cin >> name2;

		while (turno < 9 && !ganador) {
			cout << "\nTablero actual:" << endl;
			for (int i = 0; i < 3; i++) {
				cout << "     " << GATO[i][0] << "     |      " << GATO[i][1] << "      |     " << GATO[i][2] << "     " << endl;
				if (i < 2) {
					cout << "-------------------------------------" << endl;
				}
			}
			if (turno % 2 == 0) {
				cout << name1 << " (X), ingresa tu jugada (1-9): ";
				jugadaAct = 'X';
			}
			else {
				cout << name2 << " (O), ingresa tu jugada (1-9): ";
				jugadaAct = 'O';
			}
			cin >> jugadas;

			if (jugadas < 1 || jugadas > 9) {
				cout << "Jugada invalida. Intenta de nuevo." << endl;
				continue;
			}

			fila = (jugadas - 1) / 3;
			columna = (jugadas - 1) % 3;

			if (GATO[fila][columna] == 'X' || GATO[fila][columna] == 'O') {
				cout << "Esta casilla ya esta ocupada intenta de nuevo" << endl;
				continue;
			}

			GATO[fila][columna] = jugadaAct;
			turno++;

			for (int i = 0;i < 3;i++) {
				if (GATO[i][0] == GATO[i][1] && GATO[i][1] == GATO[i][2]) {
					ganador = true;
				}
			}
			for (int i = 0;i < 3;i++) {
				if (GATO[0][i] == GATO[1][i] && GATO[1][i] == GATO[2][i]) {
					ganador = true;
				}
			}
			if (GATO[0][0] == GATO[1][1] && GATO[1][1] == GATO[2][2] || GATO[0][2] == GATO[1][1] && GATO[1][1] == GATO[2][0]) {
				ganador = true;
			}


		}

		cout << "\nTablero final:" << endl;
		for (int i = 0; i < 3; i++) {
			cout << "     " << GATO[i][0] << "     |      " << GATO[i][1] << "      |     " << GATO[i][2] << "     " << endl;
			if (i < 2) {
				cout << "-------------------------------------" << endl;
			}
		}

		if (ganador) {
			if ((turno - 1) % 2 == 0) {
				cout << "FELICIDADES " << name1 << "!!. Ganaste" << endl;
			}
			else {
				cout << "FELICIDADES " << name2 << "!!. Ganaste" << endl;
			}
		}
		else {
			cout << "Empate, que mal :( " << endl;
		}
		cout << "Desea jugar nuevamente? " << endl;
		cin >> answer;
	}
	cout << "¡Gracias por jugar!" << endl;
	return 0;
}
