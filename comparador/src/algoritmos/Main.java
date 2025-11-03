import javax.swing.JFrame;

public class Main {
public static void main(String[] args) {
		JFrame window = new JFrame();
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		window.setResizable(false);
		window.setTitle("COMPARADOR DE ALGORITMOS");
		
		GrafficPanel grafficPanel= new GrafficPanel();
		window.add(grafficPanel);
		
		window.pack();
		
		window.setLocationRelativeTo(null);
		window.setVisible(true);
		
		new Thread(() -> {
            while (true) {
                grafficPanel.actualizar();
                grafficPanel.repaint();
                
                try {
                    Thread.sleep(16); // 
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }).start();
}
}
