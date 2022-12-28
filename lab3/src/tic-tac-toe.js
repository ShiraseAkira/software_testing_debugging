class TicTacToe {
    constructor() {
        this.turnCount = 0;
        this.playerSymbols = ['x', 'o'];
        this.fieldState = {
            x: 0,
            o: 0,
            empty: 511
        };
        this.winValues = [7, 56, 448, 73, 146, 292, 273, 84];
    }

    getCurrentPlayerSymbol() {
        return this.playerSymbols[this.turnCount % this.playerSymbols.length];
    }

    getNumberRepresentation(rowIndex, columnIndex) {
        if (rowIndex < 0
            || rowIndex > 2
            || columnIndex < 0
            || columnIndex >2) {
                return 0;
            }

        return Math.pow(2, (rowIndex * 3 + columnIndex));
    }

    isTurnValid(turn) {
        return (turn > 0 && turn < 512)
                ? this.fieldState.empty & turn
                : false;
    }

    makeTurn(turn) {
        const currentPlayer = this.getCurrentPlayerSymbol();
        this.fieldState[currentPlayer] = this.fieldState[currentPlayer] | turn;
        this.fieldState.empty = this.fieldState.empty & ~turn;
        this.turnCount++;
    }

    nextTurn(rowIndex, columnIndex) {
        const turn = this.getNumberRepresentation(rowIndex, columnIndex);
        if (this.isTurnValid(turn)) {
            this.makeTurn(turn);
        }
    }

    isFinished() {
        return !!(this.getWinner() || this.isDraw());
    }

    getWinner() {
        for (let i = 0; i < this.winValues.length; i ++) {
            if ((this.winValues[i] & this.fieldState.x) == this.winValues[i]) {
                return 'x'
            } else if ((this.winValues[i] & this.fieldState.o) == this.winValues[i]) {
                return 'o'                
            }
        }
        return null;
    }

    noMoreTurns() {
        return !(this.fieldState.empty);
    }

    isDraw() {
        return !this.getWinner() && this.noMoreTurns();
    }

    getFieldValue(rowIndex, colIndex) {
        const field = this.getNumberRepresentation(rowIndex, colIndex);
        if (this.fieldState.empty & field) {
            return null;
        } else if (this.fieldState.x & field) {
            return 'x';
        } else {
            return 'o';
        }
    }
}

const game = new TicTacToe();
console.log(game.getNumberRepresentation(2,2));

module.exports = TicTacToe;
