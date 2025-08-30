import java.util.ArrayList;
import java.util.List;

abstract class Persona{
    protected String nombre;
    protected String apellidoPat;
    protected String apellidoMat;
    protected double cal;
    protected String matri;

    public Persona(String nombre, String apellidoPat, String apellidoMat, double cal, String matri){
        this.nombre = nombre;
        this.apellidoPat = apellidoPat;
        this.apellidoMat = apellidoMat;
        this.cal = cal;
        this.matri = matri;
    }
    public abstract String mostrarInfo();
}

class Estudiante extends Persona{
    public Estudiante(String nombre, String apellidoPat, String apellidoMat, double cal, String matri){
        super(nombre, apellidoPat, apellidoMat, cal, matri);
    }
    @Override
     public String mostrarInfo() {
        return nombre + " " + apellidoPat + " " + apellidoMat + " " + cal + " " + matri;
    }
}

public class PERSONA {
    public static void main(String[] args) {
        // Crear lista de estudiantes (usando ArrayList en lugar de array)
        List<Estudiante> students = new ArrayList<>();
        
        // Agregar estudiantes
        students.add(new Estudiante("Jesus Alfonso", "Castro", "Sepulveda", 9.9, "24133450"));
        students.add(new Estudiante("Naomi", "Fong", "Burgueño", 9.9, "24125140"));
        
        // Imprimir información
        for (Estudiante estudiante : students) {
            System.out.println(estudiante.mostrarInfo());
        }
    }
}
