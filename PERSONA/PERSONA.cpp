#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Clase abstracta
class Persona {
protected:
    string nombre;
    string apellidoPat;
    string apellidoMat;
    float cal;
    string matri;

public:
    // Constructor
    Persona(string n, string ap, string am, float c, string m)
        : nombre(n), apellidoPat(ap), apellidoMat(am), cal(c), matri(m) {}

    // Método abstracto
    virtual void mostrar_info() const = 0;

    // Destructor virtual
    virtual ~Persona() {}
};

// Clase derivada
class Estudiante : public Persona {
public:
    // Constructor
    Estudiante(string n, string ap, string am, float c, string m)
        : Persona(n, ap, am, c, m) {}

    void mostrar_info() const override {
        cout << nombre << " " << apellidoPat << " " << apellidoMat
             << " " << cal << " " << matri << endl;
    }
};

int main() {
    vector<Persona*> students;

    students.push_back(new Estudiante("Jesus Alfonso", "Castro", "Sepulveda", 9.9, "24133450"));
    students.push_back(new Estudiante("Naomi", "Fong", "Burgueño", 9.9, "24125140"));

    for (const auto& student : students) {
        student->mostrar_info();
    }

    // Liberar memoria
    for (auto student : students) {
        delete student;
    }

    return 0;
}
