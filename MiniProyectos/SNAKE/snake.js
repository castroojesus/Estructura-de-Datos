
let board, scoreBoard, startButton, gameOverSign;
const boardSize = 10;
const gameSpeed=100;

/*posicion exacta del nodo de la serpiente*/
class SnakeNode{
    constructor(row, col){
        this.row=row;
        this.col=col;
        this.next=null;
    }
}

/*serpiente como lista enlazada*/
class Snake{
    constructor(){
        this.head=null; /*cabeza*/
        this.tail=null; /*cola*/
        this.length=0; /*longitud*/
    }
    
}



const directions = {
    ArrowUp: -10,
    ArrowDown: 10,
    ArrowLeft: -1,
    ArrowRight: 1,
};

const SquareTypes = {
emptySquare: 0,
foodSquare: 2,
snakeSquare: 1
};

let snake;
let score;
let direction;
let boardSquares;
let emptySquares;
let moveInterval;

const createBoard = () => {

    boardSquares.forEach((row, rowIndex) => {
        row.forEach((column, columnIndex) => {
            const squareValue=`${rowIndex}${columnIndex}`;
            const squareElement=document.createElement('div');
            squareElement.setAttribute('class','square emptySquare');
            squareElement.setAttribute('id',squareValue);
            board.appendChild(squareElement);
            emptySquares.push(squareValue);

        })
    })
}

const setGame = () => {
    snake = ['00','01','02','03'];
    score=snake.length;
    direction='ArrowRight';
    boardSquares = Array.from(Array(boardSize), () => new Array(boardSize).fill(SquareTypes.emptySquare));
    console.log(boardSquares);
    board.innerHTML = '';
    emptySquares = [];
    createBoard();
}

const startGame = () => {
    setGame();
    
}


document.addEventListener('DOMContentLoaded', () => {
    board = document.getElementById('board');
    scoreBoard = document.getElementById('scoreBoard');
    startButton = document.getElementById('start');
    gameOverSign = document.getElementById('gameOver');

    startButton.addEventListener('click', startGame);
});
