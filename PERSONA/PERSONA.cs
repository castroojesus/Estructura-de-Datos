using System;
using System.Collections.Generic;

// Clase abstracta Persona
public abstract class Persona
{
    protected string nombre;
    protected string apellidoPat;
    protected string apellidoMat;
    protected double cal;
    protected string matri;
    
    // Constructor
    public Persona(string nombre, string apellidoPat, string apellidoMat, double cal, string matri)
    {
        this.nombre = nombre;
        this.apellidoPat = apellidoPat;
        this.apellidoMat = apellidoMat;
        this.cal = cal;
        this.matri = matri;
    }
    
    // Método abstracto
    public abstract string MostrarInfo();
}

// Clase concreta Estudiante
public class Estudiante : Persona
{
    public Estudiante(string nombre, string apellidoPat, string apellidoMat, double cal, string matri) 
        : base(nombre, apellidoPat, apellidoMat, cal, matri)
    {
    }
    
    public override string MostrarInfo()
    {
        return $"{nombre} {apellidoPat} {apellidoMat} {cal} {matri}";
    }
}

// Clase principal
public class Program
{
    public static void Main(string[] args)
    {
        // Crear lista de estudiantes
        List<Estudiante> students = new List<Estudiante>();
        
        // Agregar estudiantes
        students.Add(new Estudiante("Jesus Alfonso", "Castro", "Sepulveda", 9.9, "24133450"));
        students.Add(new Estudiante("Naomi", "Fong", "Burgueño", 9.9, "24125140"));
        
        // Imprimir información
        foreach (Estudiante estudiante in students)
        {
            Console.WriteLine(estudiante.MostrarInfo());
        }
    }
}
