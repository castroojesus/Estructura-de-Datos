package algoritmos;

import java.awt.*;
import java.awt.geom.AffineTransform;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class ChartWindow extends JFrame {
 private java.util.Map<String, Double> tiempos;
    private ChartPanel chartPanel;
    
    public ChartWindow(java.util.Map<String, Double> tiempos) {
        this.tiempos = tiempos;
        
        setTitle("GRÁFICA DE TIEMPOS DE ALGORITMOS");
        setSize(1000, 600);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(true);
        
        chartPanel = new ChartPanel(tiempos);
        add(chartPanel);
        
        setVisible(true);
    }
}

class ChartPanel extends JPanel {
    private java.util.Map<String, Double> tiempos;
    int MARGIN_TOP_GRAPH = 100;    // mueve la grafica para abajo o arriba (si aumento va para abajo)
    int MARGIN_LEFT_GRAPH = 80;    // mueve grafica a izquierda o derecha, si aumento va a la derecha
    int CHART_HEIGHT_GRAPH = 300;  // que tan larga es la grafica, numero grande mas larga
    int CHART_WIDTH_GRAPH = 200; 
    private final int BAR_WIDTH = 45;
    private final int BAR_SPACING = 15;
    
    public ChartPanel(java.util.Map<String, Double> tiempos) {
        this.tiempos = tiempos;
        setBackground(Color.WHITE);
        setPreferredSize(new Dimension(800, 600));
    }
    
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        
        if (tiempos == null || tiempos.isEmpty()) {
            g.setColor(Color.RED);
            g.setFont(new Font("Arial", Font.BOLD, 20));
            g.drawString("No hay datos para mostrar", 250, 300);
            return;
        }
        
        dibujarGrafica(g);
        dibujarLeyenda(g);
        dibujarTitulo(g);
    }
    
    private void dibujarTitulo(Graphics g) {
        g.setColor(Color.BLACK);
        g.setFont(new Font("Arial", Font.BOLD, 24));
        g.drawString("COMPARACIÓN DE TIEMPOS DE ALGORITMOS", 150, 40);
        
        g.setFont(new Font("Arial", Font.PLAIN, 16));
        g.drawString("Tiempos de ejecución en milisegundos", 250, 70);
    }
    
    private void dibujarGrafica(Graphics g) {
        // Encontrar el tiempo máximo para escalar
        double maxTiempo = tiempos.values().stream().max(Double::compare).orElse(1.0);
        if (maxTiempo == 0) maxTiempo = 1.0;
        
        g.setColor(Color.BLACK);
        g.drawLine(MARGIN_LEFT_GRAPH, MARGIN_TOP_GRAPH, MARGIN_LEFT_GRAPH, MARGIN_TOP_GRAPH + CHART_HEIGHT_GRAPH); // Eje Y
        g.drawLine(MARGIN_LEFT_GRAPH, MARGIN_TOP_GRAPH + CHART_HEIGHT_GRAPH, 
                  MARGIN_LEFT_GRAPH + CHART_WIDTH_GRAPH, MARGIN_TOP_GRAPH + CHART_HEIGHT_GRAPH); // Eje X
        
        // Dibujar barras
        java.util.List<java.util.Map.Entry<String, Double>> algoritmosOrdenados = 
            new java.util.ArrayList<>(tiempos.entrySet());
        algoritmosOrdenados.sort(java.util.Map.Entry.comparingByValue());
        
        int x = MARGIN_LEFT_GRAPH + 20;
        
        for (int i = 0; i < algoritmosOrdenados.size(); i++) {
            java.util.Map.Entry<String, Double> entry = algoritmosOrdenados.get(i);
            double tiempo = entry.getValue();
            
            // Calcular altura de la barra (escalada)
            int barHeight = (int) ((tiempo / maxTiempo) * CHART_HEIGHT_GRAPH);
            if (barHeight > CHART_HEIGHT_GRAPH) barHeight = CHART_HEIGHT_GRAPH;
            if (barHeight < 1) barHeight = 1;
            
            // Color de la barra
            Color barColor = getColorForAlgorithm(i);
            
            // Dibujar barra
            g.setColor(barColor);
            g.fillRect(x, MARGIN_TOP_GRAPH + CHART_HEIGHT_GRAPH - barHeight, BAR_WIDTH, barHeight);
            
            // Borde de la barra
            g.setColor(Color.BLACK);
            g.drawRect(x, MARGIN_TOP_GRAPH + CHART_HEIGHT_GRAPH - barHeight, BAR_WIDTH, barHeight);
            
            // Nombre del algoritmo
            String algoName = getShortName(entry.getKey());
            g.setFont(new Font("Arial", Font.BOLD, 12));
            
            // Rotar texto para mejor visualización
            Graphics2D g2d = (Graphics2D) g;
            Font originalFont = g2d.getFont();
            
            // Dibujar nombre rotado
            g2d.rotate(-Math.PI / 2, x + BAR_WIDTH/2, MARGIN_TOP_GRAPH + CHART_HEIGHT_GRAPH + 50);
            g2d.drawString(algoName, x + BAR_WIDTH/2 - 15, MARGIN_TOP_GRAPH + CHART_HEIGHT_GRAPH + 50);
            g2d.rotate(Math.PI / 2, x + BAR_WIDTH/2, MARGIN_TOP_GRAPH + CHART_HEIGHT_GRAPH + 50);
            
            // Valor del tiempo
            g2d.setFont(new Font("Arial", Font.BOLD, 11));
            String tiempoStr = String.format("%.2f ms", tiempo);
            int textWidth = g2d.getFontMetrics().stringWidth(tiempoStr);
            g2d.drawString(tiempoStr, x + (BAR_WIDTH - textWidth)/2, MARGIN_TOP_GRAPH + CHART_HEIGHT_GRAPH - barHeight - 5);
            
            g2d.setFont(originalFont);
            
            x += BAR_WIDTH + BAR_SPACING;
        }
        Graphics2D g2d = (Graphics2D) g;
        // Etiquetas de ejes
        g.setColor(Color.BLACK);
        g.setFont(new Font("Arial", Font.BOLD, 14));
        
        g2d.setFont(new Font("Arial", Font.BOLD, 16));
        AffineTransform originalTransform = g2d.getTransform();
        
        // Rotar 90 grados en sentido antihorario (-90°)
        g2d.rotate(-Math.PI / 2, MARGIN_LEFT_GRAPH - 50, MARGIN_TOP_GRAPH + CHART_HEIGHT_GRAPH / 2);
        g2d.drawString("TIEMPO (milisegundos)", MARGIN_LEFT_GRAPH - 120, MARGIN_TOP_GRAPH + CHART_HEIGHT_GRAPH / 2);
        g2d.setTransform(originalTransform);
        // Eje X
        g.drawString("Algoritmos de Ordenamiento", MARGIN_LEFT_GRAPH + CHART_WIDTH_GRAPH / 2 - (-80), MARGIN_TOP_GRAPH + CHART_HEIGHT_GRAPH + 110);
        
        // Escala del eje Y
        g.setFont(new Font("Arial", Font.PLAIN, 12));
        for (int i = 0; i <= 5; i++) {
            double valor = maxTiempo * i / 5;
            int y = MARGIN_TOP_GRAPH + CHART_HEIGHT_GRAPH - (CHART_HEIGHT_GRAPH * i / 5);
            g.drawString(String.format("%.1f", valor), MARGIN_LEFT_GRAPH - 35, y + 5);
            g.drawLine(MARGIN_LEFT_GRAPH - 5, y, MARGIN_LEFT_GRAPH, y);
        }
    }
    
    private void dibujarLeyenda(Graphics g) {
        int leyendaX = MARGIN_LEFT_GRAPH + CHART_WIDTH_GRAPH + 400;
        int leyendaY = MARGIN_TOP_GRAPH;
        
        g.setColor(Color.BLACK);
        g.setFont(new Font("Arial", Font.BOLD, 16));
        g.drawString("LEYENDA", leyendaX, leyendaY);
        
        g.setFont(new Font("Arial", Font.PLAIN, 14));
        leyendaY += 30;
        
        java.util.List<java.util.Map.Entry<String, Double>> algoritmosOrdenados = 
            new java.util.ArrayList<>(tiempos.entrySet());
        algoritmosOrdenados.sort(java.util.Map.Entry.comparingByValue());
        
        for (int i = 0; i < algoritmosOrdenados.size(); i++) {
            java.util.Map.Entry<String, Double> entry = algoritmosOrdenados.get(i);
            Color colorBarra = getColorForAlgorithm(i);
            
            // Cuadro de color
            g.setColor(colorBarra);
            g.fillRect(leyendaX, leyendaY, 15, 15);
            g.setColor(Color.BLACK);
            g.drawRect(leyendaX, leyendaY, 15, 15);
            
            // Nombre y tiempo
            g.drawString(entry.getKey(), leyendaX + 20, leyendaY + 12);
            
            // Tiempo alineado a la derecha
            String tiempoStr = String.format("%.4f ms", entry.getValue());
            int tiempoWidth = g.getFontMetrics().stringWidth(tiempoStr);
            g.drawString(tiempoStr, leyendaX + 220 - tiempoWidth, leyendaY + 12);
            
            leyendaY += 25;
        }
        
        // Estadísticas
        leyendaY += 20;
        g.setFont(new Font("Arial", Font.BOLD, 16));
        g.drawString("ESTADÍSTICAS:", leyendaX, leyendaY);
        
        g.setFont(new Font("Arial", Font.PLAIN, 14));
        leyendaY += 25;
        
        double max = algoritmosOrdenados.get(algoritmosOrdenados.size() - 1).getValue();
        double min = algoritmosOrdenados.get(0).getValue();
        String masRapido = algoritmosOrdenados.get(0).getKey();
        String masLento = algoritmosOrdenados.get(algoritmosOrdenados.size() - 1).getKey();
        
        g.drawString("Más rápido: " + masRapido, leyendaX, leyendaY);
        leyendaY += 20;
        g.drawString("Más lento: " + masLento, leyendaX, leyendaY);
        leyendaY += 20;
        g.drawString(String.format("Rango: %.4f ms", max - min), leyendaX, leyendaY);
    }
    
    private Color getColorForAlgorithm(int index) {
        Color[] colors = {
            new Color(70, 130, 180),    // Steel Blue
            new Color(220, 20, 60),     // Crimson
            new Color(34, 139, 34),     // Forest Green
            new Color(255, 140, 0),     // Dark Orange
            new Color(148, 0, 211),     // Dark Violet
            new Color(255, 215, 0),     // Gold
            new Color(0, 191, 255),     // Deep Sky Blue
            new Color(255, 0, 255),     // Magenta
            new Color(165, 42, 42)      // Brown
        };
        return colors[index % colors.length];
    }
    
    private String getShortName(String fullName) {
        switch(fullName) {
            case "Selection Sort": return "SELECTION";
            case "Bubble Sort": return "BUBBLE";
            case "Insertion Sort": return "INSERTION";
            case "Quick Sort": return "QUICK";
            case "Merge Sort": return "MERGE";
            case "Heap Sort": return "HEAP";
            case "Shell Sort": return "SHELL";
            case "Radix Sort": return "RADIX";
            case "Bucket Sort": return "BUCKET";
            default: return fullName.length() > 8 ? fullName.substring(0, 8).toUpperCase() : fullName.toUpperCase();
        }
    }
}
