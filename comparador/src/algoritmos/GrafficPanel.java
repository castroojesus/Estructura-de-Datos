import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;

import javax.swing.JPanel;

public class GrafficPanel extends JPanel{
	
	final int originalTileSize=16;
	final int scale=3;
	
	final int tileSize=originalTileSize*scale;
	final int maxScreenCol=16;
	final int maxScreenRow=12;
	final int ScreenWidth=tileSize*maxScreenCol;
	final int ScreenHeight=tileSize*maxScreenRow;
	
	KeyHandler keyH= new KeyHandler();
	private String pantallaActual = "menu";
	private Font fuenteNormal, fuenteTitulo;
	private java.util.Map<String, Double> tiemposResultados;
	private int tamañoArrayActual;
	
	public GrafficPanel() {
		this.setPreferredSize(new Dimension(ScreenWidth,ScreenHeight));
		this.setBackground(Color.black);
		this.setDoubleBuffered(true);
		this.addKeyListener(keyH);
		this.setFocusable(true);
		
		fuenteNormal = new Font("Arial", Font.PLAIN, 22);
        fuenteTitulo = new Font("Arial", Font.BOLD, 24);
	}
	
	@Override
	public void paintComponent(Graphics g) {
        super.paintComponent(g);
        
        if (pantallaActual.equals("menu")) {
            dibujarMenu(g);
        } else if (pantallaActual.equals("resultados")) {
            dibujarResultados(g);
        }
    }
	
	private void dibujarResultados(Graphics g) {
        g.setColor(Color.black);
        g.fillRect(0, 0, ScreenWidth, ScreenHeight);
        
        g.setFont(fuenteTitulo);
        g.setColor(Color.green);
        g.drawString("RESULTADOS PARA AARREGLO DE "+tamañoArrayActual+" ELEMENTOS", 80, 50);
        
        if (tiemposResultados != null) {
            java.util.List<java.util.Map.Entry<String, Double>> algoritmosOrdenados = 
                new java.util.ArrayList<>(tiemposResultados.entrySet());
            algoritmosOrdenados.sort(java.util.Map.Entry.comparingByValue());
            
            g.setFont(fuenteNormal);
            int yPos = 150;
            for (int i = 0; i < algoritmosOrdenados.size(); i++) {
                java.util.Map.Entry<String, Double> entry = algoritmosOrdenados.get(i);
                g.setColor(i == 0 ? Color.green : Color.yellow);
                g.drawString(String.format("%s: %.4f ms", entry.getKey(), entry.getValue()), 250, yPos);
                
                yPos += 25;
            }
        }
        
        g.setColor(Color.white);
        g.drawString("Presione G para abrir gráfica de barras", 180, 450);
        g.drawString("Presione ESPACIO para volver al menú", 180, 480);
	}
    
    private void dibujarMenu(Graphics g) {
        // Fondo
        g.setColor(Color.black);
        g.fillRect(0, 0, ScreenWidth, ScreenHeight);
        
        // Título
        g.setFont(fuenteTitulo);
        g.setColor(Color.green);
        g.drawString("SELECCIONE EL TAMAÑO DEL ARREGLO", 150, 100);
        
        // Opciones
        g.setFont(fuenteNormal);
        g.setColor(Color.yellow);
        
        String[] opciones = {
            "1. Arreglo de 100",
            "2. Arreglo de 1000", 
            "3. Arreglo de 10000",
            "4. Arreglo de 100000",
            "5. Salir"
        };
        
        for (int i = 0; i < opciones.length; i++) {
            g.drawString(opciones[i], 200, 200 + i * 50);
        }
    }
    
    public void actualizar() {
        if (keyH.onePressed) {
        	 tiemposResultados = Algoritmos100.ejecutarAlgoritmo();
             pantallaActual = "resultados";
             tamañoArrayActual=100;
             keyH.onePressed = false;
             }
        if (keyH.twoPressed) {
        	tiemposResultados = Algoritmos1000.ejecutarAlgoritmo();
            pantallaActual = "resultados";
            tamañoArrayActual=1000;
            keyH.onePressed = false;
        }
        if (keyH.threePressed) {
        	tiemposResultados = Algoritmos10000.ejecutarAlgoritmo();
            pantallaActual = "resultados";
            tamañoArrayActual=10000;
            keyH.onePressed = false;
        }
        if (keyH.fourPressed) {
        	tiemposResultados = Algoritmos100000.ejecutarAlgoritmo();
            pantallaActual = "resultados";
            tamañoArrayActual=100000;
            keyH.onePressed = false;
        }
        if (keyH.fivePressed) {
            System.exit(0);
        }
        
        if (pantallaActual.equals("resultados") && keyH.gPressed) {
            if (tiemposResultados != null && !tiemposResultados.isEmpty()) {
                new ChartWindow(tiemposResultados);
            }
            keyH.gPressed = false;
        }
        
            // Volver al menú
            if (pantallaActual.equals("resultados") && keyH.spacePressed) {
                pantallaActual = "menu";
                keyH.spacePressed = false;
            }
                repaint();
            }
        
        // Ventana de gráfica simple incluida aquí para evitar errores de clase no encontrada
        public static class ChartWindow extends javax.swing.JFrame {
            private java.util.Map<String, Double> data;
            public ChartWindow(java.util.Map<String, Double> data) {
                super("Gráfica de tiempos");
                this.data = data;
                setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);
                setSize(600, 400);
                setLocationRelativeTo(null);
                add(new javax.swing.JPanel() {
                    @Override
                    protected void paintComponent(java.awt.Graphics g) {
                        super.paintComponent(g);
                        if (data == null || data.isEmpty()) {
                            g.setColor(java.awt.Color.WHITE);
                            g.drawString("No hay datos para mostrar", 20, 20);
                            return;
                        }
                        int width = getWidth();
                        int height = getHeight();
                        int padding = 40;
                        int barWidth = Math.max(10, (width - padding * 2) / Math.max(1, data.size()));
                        double max = java.util.Collections.max(data.values());
                        int x = padding;
                        int i = 0;
                        for (java.util.Map.Entry<String, Double> entry : data.entrySet()) {
                            double value = entry.getValue();
                            int barHeight = (int) ((height - padding * 2) * (value / (max == 0 ? 1 : max)));
                            int y = height - padding - barHeight;
                            g.setColor(i == 0 ? java.awt.Color.GREEN : java.awt.Color.YELLOW);
                            g.fillRect(x, y, barWidth - 10, barHeight);
                            g.setColor(java.awt.Color.WHITE);
                            g.drawString(entry.getKey(), x + 2, height - padding + 15);
                            g.drawString(String.format("%.4f ms", value), x + 2, Math.max(10, y - 5));
                            x += barWidth;
                            i++;
                        }
                    }
                });
                setVisible(true);
            }
        }
    }




