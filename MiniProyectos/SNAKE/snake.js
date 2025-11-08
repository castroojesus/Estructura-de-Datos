let board, scoreBoard, startButton, gameOverSign;
const boardSize = 20;
const gameSpeed=100;
let speedOverTime; // Velocidad inicial
let initialLength = 0; // tamaño original de la serpiente
let lastMilestone = 0; // último múltiplo de 15 procesado



let tiempoFinal;
let tiempoInicio;
let timeInterval;

let ranking = JSON.parse(localStorage.getItem('snakeRanking')) || [];

const showRanking = () => {
    const tiempoTotal = ((tiempoFinal - tiempoInicio) / 1000).toFixed(2);
    
    const name = prompt(`¡Game Over!\nPuntuación: ${score}\nTiempo: ${tiempoTotal}s\n\nIngresa tu nombre:`) || 'Anónimo';
    
    // Guardar en ranking
    ranking.push({
        name: name,
        score: score,
        time: parseFloat(tiempoTotal),
        date: new Date().toLocaleDateString()
    });
    
    // Ordenar ranking
    ranking.sort((a, b) => {
        if (b.score !== a.score) return b.score - a.score;
        return b.time - a.time;
    });
    
    ranking = ranking.slice(0, 5);
    localStorage.setItem('snakeRanking', JSON.stringify(ranking));
    
    // Mostrar ranking en el div
    const rankingHTML = `
        <h3 style="text-align:center; color:#0ff; margin-bottom:15px;">🏆 RANKING 🏆</h3>
        <div style="max-height:300px; overflow-y:auto;">
            ${ranking.map((player, index) => `
                <div class="ranking-item">
                    <span>${index + 1}. ${player.name}</span>
                    <span>${player.score} pts - ${player.time}s</span>
                </div>
            `).join('')}
            ${ranking.length === 0 ? '<div style="text-align:center; color:#888;">No hay datos</div>' : ''}
        </div>
        <button id="closeRanking">Cerrar</button>
    `;
    
    const rankingDiv = document.getElementById('ranking');
    rankingDiv.innerHTML = rankingHTML;
    rankingDiv.style.display = 'block';
    
    // Evento para cerrar
    document.getElementById('closeRanking').addEventListener('click', () => {
        rankingDiv.style.display = 'none';
    });
};

/*posicion exacta del nodo de la serpiente*/
class SnakeNode{
    constructor(coords){
        this.value=coords;
        this.next=null;
    }
}

/*serpiente como lista enlazada*/
class Snake{
    constructor(){
        this.head; /*cabeza*/
        this.tail; /*cola*/
        this.length=0; /*longitud*/
    }
    addNode(coords){
        const newNode=new SnakeNode(coords); /*declaro un nodo nuevo*/
        if(!this.head){
            this.head=this.tail=newNode;
        }else{
            newNode.next=this.head;
            this.head=newNode;
        }
        this.length++;
    }
    removeTail(){
        if(!this.head) return;
        if(this.head===this.tail){
            this.head=this.tail=null;
            this.length=0;
            return;
        }
        
        let currentNode=this.head;
        while(currentNode.next!==this.tail){
            currentNode=currentNode.next;
        }
        currentNode.next=null;
        this.tail=currentNode;
        this.length--;
    }

    getPositions(){
        const positions=[];
        let currentNode=this.head;
        while(currentNode){
            positions.push(currentNode.value);
            currentNode=currentNode.next;
        }
        return positions;
    }
    
}



const directions = {
    ArrowUp: -20,
    ArrowDown: 20,
    ArrowLeft: -1,
    ArrowRight: 1,
};

const SquareTypes = {
emptySquare: 0,
foodSquare: 2,
snakeSquare: 1,
trapSquare: 3,
};

let snake;
let score;
let direction;
let boardSquares;
let emptySquares;
let moveInterval;
let speedTimer = null;

const createBoard = () => {

    boardSquares.forEach((row, rowIndex) => {
        row.forEach((column, columnIndex) => {
            const squareValue=`${rowIndex}-${columnIndex}`;
            const squareElement=document.createElement('div');
            squareElement.setAttribute('class','square emptySquare');
            squareElement.setAttribute('id',squareValue);
            board.appendChild(squareElement);
            emptySquares.push(squareValue);

        })
    })
}

const drawSnake = () => {
    document.querySelectorAll('.snakeSquare').forEach(square => {
        square.classList.remove('snakeSquare');
        
    });
    const snakePositions=snake.getPositions();
    snakePositions.forEach(position => {
        const squareElement=document.getElementById(position);
        if(squareElement){
            squareElement.classList.add('snakeSquare');
        }
    });
}

const setGame = () => {
    snake = new Snake();
    ['0-0','0-1','0-2','0-3','0-5'].forEach(pos => snake.addNode(pos));
    score=5;
    // Guardamos el tamaño inicial de la serpiente para poder restaurarlo cada 15 puntos
    initialLength = snake.length;
    direction='ArrowRight';
    boardSquares = Array.from(Array(boardSize), () => new Array(boardSize).fill(SquareTypes.emptySquare));
    console.log(boardSquares);
    board.innerHTML = '';
    emptySquares = [];
    createBoard();
    
    
}

updateScore = () => {
    scoreBoard.innerText = score;
}

updateTime = () => {
    const tiempoActual = performance.now();
    const tiempoTranscurrido = ((tiempoActual - tiempoInicio) / 1000).toFixed(2);
    time.innerText = tiempoTranscurrido + "s";
}
createRandomFood = () => {
const randomEmptySquare= emptySquares[Math.floor(Math.random() * emptySquares.length)];
drawSquare(randomEmptySquare, 'foodSquare');
}

createRandomTrap = (numberOfTraps) => {
    const availableSquares = emptySquares.filter(square => {
        const [row, col] = square.split('-').map(Number);
        return boardSquares[row][col] !== SquareTypes.foodSquare;
    });

    
    
    if (availableSquares.length === 0) return;
    for (let i = 0; i < numberOfTraps; i++) {
        const randomIndex = Math.floor(Math.random() * availableSquares.length);
        const randomSquare = availableSquares[randomIndex];
        drawSquare(randomSquare, 'trapSquare');
        availableSquares.splice(randomIndex, 1);
    }
    
}
    
const minSpeed = 50;           // velocidad límite (ms)
const speedStep = 50;          // cuánto reducimos (ms) cada 30s

const setDirection = newDirection => {
    direction = newDirection;
}

function increaseSpeed() {
    // Solo actuamos cuando alcanzamos un nuevo múltiplo de 15
    if (score > 0 && score % 15 === 0 && score !== lastMilestone) {
        // Reducir velocidad respetando el mínimo
        if (speedOverTime > minSpeed) {
            speedOverTime = Math.max(minSpeed, speedOverTime - speedStep);
            if (moveInterval) {
                clearInterval(moveInterval);
                moveInterval = setInterval(moveSnake, speedOverTime);
            }
            console.log('Aumenta velocidad, nuevo intervalo:', speedOverTime);
        }

        // Reiniciar el tamaño de la serpiente pero MANTENER EL SCORE
        const currentScore = score; // Guardamos el score actual
        
        // Restaurar el tamaño original de la serpiente (eliminar nodos de la cola)
        while (snake.length > initialLength) {
            const tailPos = snake.tail && snake.tail.value;
            snake.removeTail();
            if (tailPos) drawSquare(tailPos, 'emptySquare');
        }
        
        // RESTAURAR EL SCORE ORIGINAL (no usar snake.length)
        score = currentScore;
        updateScore();

        // Marcar este múltiplo como procesado para no repetir la acción
        lastMilestone = score;
    }
}






const moveSnake = () => {
   const headPosition = snake.head.value;
    const [row, col] = headPosition.split('-').map(Number);

    
    
    let newRow = row;
    let newCol = col;
    
    switch(direction) {
        case 'ArrowUp':
            newRow = (row - 1 +boardSize) %boardSize
            break;
        case 'ArrowDown':
            newRow = (row + 1) %boardSize
            break;
        case 'ArrowLeft':
            newCol = (col - 1+boardSize) %boardSize
            break;
        case 'ArrowRight':
            newCol = (col + 1) %boardSize
            break;
    }
    
    const newPosition = `${newRow}-${newCol}`;
    
    // Verificar colisiones
    if (checkCollision(newPosition)) {
        gameOver();
        return;
    }
    
    const ateFood = boardSquares[newRow][newCol] === SquareTypes.foodSquare;
    const hitTrap = boardSquares[newRow][newCol] === SquareTypes.trapSquare;
    
    // Mover la serpiente
    snake.addNode(newPosition);
    
    if (ateFood) {
        
        score ++;
        updateScore();
        createRandomFood();
        increaseSpeed(); // Aumentar velocidad cada 30 segundos
    } else {
        
        const tailPosition = snake.tail.value;
        snake.removeTail();
        drawSquare(tailPosition, 'emptySquare');
    }

    let activateTrap;

    if (hitTrap) {
        const tailPosition = snake.tail.value;
        snake.removeTail();
        drawSquare(tailPosition, 'emptySquare');
        score = snake.length;
        activateTrap++;
        updateScore();
        createRandomTrap(1);
    }

    if(score <= 0){
        gameOver();
        return;
    }

    
    
    drawSquare(newPosition, 'snakeSquare');
    drawSnake();
}

const checkCollision = (position) => {
    let currentNode = snake.head.next; 
    
    while (currentNode) {
        if (currentNode.value === position) {
            
            return true; 
        }
        currentNode = currentNode.next;
    }
    return false; 
}



const gameOver = () => {
    if (moveInterval) { clearInterval(moveInterval); moveInterval = null; }
    if (speedTimer) { clearInterval(speedTimer); speedTimer = null; }
    if (timeInterval) { clearInterval(timeInterval); timeInterval = null; }
    tiempoFinal = performance.now();
    
    
    const tiempoTotal = ((tiempoFinal - tiempoInicio) / 1000).toFixed(2);
    time.innerText = tiempoTotal + "s";
    gameOverSign.style.display = 'block';
    startButton.disabled = false;
    document.removeEventListener('keydown', changeDirection);

    setTimeout(showRanking, 500);
    
}

const changeDirection = event => {
    switch(event.code){
        case 'ArrowUp':
            direction !== 'ArrowDown' && setDirection(event.code);
            break;
        case 'ArrowDown':
            direction !== 'ArrowUp' && setDirection(event.code);
            break;
        case 'ArrowLeft':
            direction !== 'ArrowRight' && setDirection(event.code);
            break;
        case 'ArrowRight':
            direction !== 'ArrowLeft' && setDirection(event.code);
            break;
    }
}


const startGame = () => {
    if (moveInterval) { clearInterval(moveInterval); moveInterval = null; }
    if (speedTimer) { clearInterval(speedTimer); speedTimer = null; }
    speedOverTime = gameSpeed * 2; // Reiniciar velocidad al comenzar
    tiempoInicio = performance.now();
    activateTrap = 0;
    setGame();
    startButton.disabled = true;
    gameOverSign.style.display = 'none';
    drawSnake();
    updateScore();
    updateTime();
    createRandomFood();
    createRandomTrap(3);
    document.addEventListener('keydown', changeDirection);
    
    moveInterval = setInterval(moveSnake, speedOverTime);
    timeInterval = setInterval(updateTime, 100);
    
    
}

const drawSquare = (square, type) => {
    const [row, col] = square.split('-').map(Number);
    boardSquares[row][col] = SquareTypes[type];
    const squareElement = document.getElementById(square);
    squareElement.setAttribute('class', `square ${type}`);
    if (type === 'emptySquare') {
        emptySquares.push(square);
    } else {
        if(emptySquares.indexOf(square) !== -1){
            emptySquares.splice(emptySquares.indexOf(square), 1);
        }

}
}


document.addEventListener('DOMContentLoaded', () => {
    board = document.getElementById('board');
    scoreBoard = document.getElementById('scoreBoard');
    startButton = document.getElementById('start');
    gameOverSign = document.getElementById('gameOver');
    time =document.getElementById('timeBoard');

    startButton.addEventListener('click', startGame);
});
