const chai = require('chai');
const sinon = require('sinon');
const sinonChai = require('sinon-chai');

chai.use(sinonChai);

const expect = chai.expect;
const TicTacToe = require('../src/tic-tac-toe.js');

describe('Tic-Tac-Toe', () => {
  describe('#getCurrentPlayerSymbol', () => {
    it('Должен возвращать корректный символ игрока', () => {
      let game;

      game = new TicTacToe();
      expect(game.getCurrentPlayerSymbol()).to.equal('x')
      game.nextTurn(0, 1)
      expect(game.getCurrentPlayerSymbol()).to.equal('o')
      game.nextTurn(0, 1)
      expect(game.getCurrentPlayerSymbol()).to.equal('o')
      game.nextTurn(-1, -1)
      expect(game.getCurrentPlayerSymbol()).to.equal('o')
      game.nextTurn(1, 0)
      expect(game.getCurrentPlayerSymbol()).to.equal('x')
    });
  });
  describe('#getNumberRepresentation', () => {
    it('Должен возвращать корректное числовое представление хода', () => {
      let game;

      game = new TicTacToe();
      expect(game.getNumberRepresentation(0, 0)).to.equal(1)
      expect(game.getNumberRepresentation(0, 1)).to.equal(2)
      expect(game.getNumberRepresentation(2, 2)).to.equal(256)

      expect(game.getNumberRepresentation(-1, 0)).to.equal(0)
      expect(game.getNumberRepresentation(3, 0)).to.equal(0)
    });
  });
  describe('#isTurnValid', () => {
    it('Должен возвращать верную корректность хода(числового)', () => {
      let game;

      game = new TicTacToe();
      expect(!!game.isTurnValid(1)).to.equal(true)
      expect(!!game.isTurnValid(5)).to.equal(true)
      expect(!!game.isTurnValid(511)).to.equal(true)
      game.nextTurn(0, 0)
      expect(!!game.isTurnValid(1)).to.equal(false)
      expect(!!game.isTurnValid(0)).to.equal(false)
      expect(!!game.isTurnValid(-1)).to.equal(false)
      expect(!!game.isTurnValid(512)).to.equal(false)
    });
  });
  describe('#makeTurn', () => {
    it('Должен корректно обновлять состояние при валидном ходе', () => {
      let game;

      game = new TicTacToe();
      expect(game.getCurrentPlayerSymbol()).to.equal('x')
      expect(game.turnCount).to.equal(0)
      expect(game.fieldState['x']).to.equal(0)
      expect(game.fieldState['empty']).to.equal(511)
      game.nextTurn(0, 0)

      expect(game.getCurrentPlayerSymbol()).to.equal('o')
      expect(game.turnCount).to.equal(1)
      expect(game.fieldState['x']).to.equal(1)
      expect(game.fieldState['empty']).to.equal(510)

      game.nextTurn(0, 0)
      expect(game.getCurrentPlayerSymbol()).to.equal('o')
      expect(game.turnCount).to.equal(1)
      expect(game.fieldState['x']).to.equal(1)
      expect(game.fieldState['empty']).to.equal(510)
    });
  });
  describe('#nextTurn', () => {
    it('Совершает ход, если он корректный', () => {
      let game;
      game = new TicTacToe();

      const sandbox = sinon.createSandbox();
      sandbox.spy(game, 'makeTurn');

      game.nextTurn(0, 1)
      expect(game.makeTurn).to.have.been.calledOnce
      game.nextTurn(0, 1)
      expect(game.makeTurn).to.have.been.calledOnce
    });
  });
  describe('#getFieldValue', () => {
    it('Возвращает элемент находящийся в ячейке или null если пустой', () => {
      let game;

      game = new TicTacToe();
      expect(game.getFieldValue(0, 0)).to.equal(null)
      game.nextTurn(0, 0)
      game.nextTurn(0, 1)
      expect(game.getFieldValue(0, 0)).to.equal('x')
      expect(game.getFieldValue(0, 1)).to.equal('o')
    });
  });
  describe('#isFinished', () => {
    it('Возвращает True если игра закончена', () => {
      let game;

      game = new TicTacToe();
      game.nextTurn(1, 0);
      game.nextTurn(2, 2);
      game.nextTurn(0, 2);
      game.nextTurn(1, 1);
      game.nextTurn(1, 2);
      game.nextTurn(2, 0);
      game.nextTurn(0, 0);
      game.nextTurn(0, 1);
      expect(game.isFinished()).to.equal(false);

      game.nextTurn(2, 1);
      expect(game.isFinished()).to.equal(true);

      game = new TicTacToe();
      expect(game.isFinished()).to.equal(false);
      game.nextTurn(2, 2)
      game.nextTurn(1, 1)
      game.nextTurn(0, 2)
      game.nextTurn(0, 0)
      game.nextTurn(0, 1)
      game.nextTurn(2, 1)
      game.nextTurn(1, 2)
      expect(game.isFinished()).to.equal(true)
    });
  });
  describe('#getWinner', () => {
    it('Возвращает победителя(x или o), либо null в случае ничьей или если еще нет победителя', () => {
      let game;

      game = new TicTacToe();
      game.nextTurn(1, 0);
      game.nextTurn(2, 2);
      game.nextTurn(0, 2);
      game.nextTurn(1, 1);
      game.nextTurn(1, 2);
      game.nextTurn(2, 0);
      game.nextTurn(0, 0);
      game.nextTurn(0, 1);
      expect(game.getWinner()).to.equal(null);

      game.nextTurn(2, 1);
      expect(game.getWinner()).to.equal(null);

      game = new TicTacToe();
      game.nextTurn(1, 0)
      game.nextTurn(1, 2)
      game.nextTurn(2, 1)
      game.nextTurn(1, 1)
      game.nextTurn(0, 1)
      game.nextTurn(2, 0)
      game.nextTurn(2, 2)
      game.nextTurn(1, 1)
      game.nextTurn(0, 2)
      expect(game.getWinner()).to.equal('o')

      game = new TicTacToe();
      game.nextTurn(2, 2)
      game.nextTurn(1, 1)
      game.nextTurn(0, 2)
      game.nextTurn(0, 0)
      game.nextTurn(0, 1)
      game.nextTurn(2, 1)
      game.nextTurn(1, 2)
      expect(game.getWinner()).to.equal('x')
    });
  });
  describe('#noMoreTurns', () => {
    it('Возвращает "True" если больше нет ходов(все клетки заняты)', () => {
      let game;

      game = new TicTacToe();
      game.nextTurn(1, 0);
      expect(game.noMoreTurns()).to.equal(false);
      game.nextTurn(2, 2);
      game.nextTurn(0, 2);
      game.nextTurn(1, 1);
      game.nextTurn(1, 2);
      game.nextTurn(2, 0);
      game.nextTurn(0, 0);
      game.nextTurn(0, 1);
      expect(game.noMoreTurns()).to.equal(false);
      game.nextTurn(2, 1);
      expect(game.noMoreTurns()).to.equal(true);
    });
  });
  describe('#isDraw', () => {
    it('Возвращает "True" если игра закончилась ничьей', () => {
      let game;

      game = new TicTacToe();
      game.nextTurn(1, 0);
      expect(game.isDraw()).to.equal(false);
      game.nextTurn(2, 2);
      game.nextTurn(0, 2);
      game.nextTurn(1, 1);
      game.nextTurn(1, 2);
      game.nextTurn(2, 0);
      game.nextTurn(0, 0);
      game.nextTurn(0, 1);
      expect(game.isDraw()).to.equal(false);
      game.nextTurn(2, 1);
      expect(game.isDraw()).to.equal(true);
    });
  });

});