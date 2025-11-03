import java.awt.event.KeyEvent;

public class KeyHandler {
public boolean onePressed, twoPressed, threePressed, fourPressed, fivePressed,spacePressed,gPressed;

	
	public void keyTyped(KeyEvent e) {
		
		
	}

	
	public void keyPressed(KeyEvent e) {
		int code=e.getKeyCode();
		if(code==KeyEvent.VK_1) {
			onePressed=true;
		}
		if(code==KeyEvent.VK_2) {
			twoPressed=true;
		}
		if(code==KeyEvent.VK_3) {
			threePressed=true;
		}
		if(code==KeyEvent.VK_4) {
			fourPressed=true;
		}
		if(code==KeyEvent.VK_5) {
			fivePressed=true;
		}
		if (code == KeyEvent.VK_SPACE) {
            spacePressed = true;
        }
		if (code == KeyEvent.VK_G) {
            gPressed = true;
        }
	}

	
	public void keyReleased(KeyEvent e) {
		int code=e.getKeyCode();
		if(code==KeyEvent.VK_1) {
			onePressed=false;
		}
		if(code==KeyEvent.VK_2) {
			twoPressed=false;
		}
		if(code==KeyEvent.VK_3) {
			threePressed=false;
		}
		if(code==KeyEvent.VK_4) {
			fourPressed=false;
		}
		if(code==KeyEvent.VK_5) {
			fivePressed=false;
		}
		if (code == KeyEvent.VK_SPACE) {
            spacePressed = false;
        }
		
		if (code == KeyEvent.VK_G) {
            gPressed = false;
        }
	}
}
