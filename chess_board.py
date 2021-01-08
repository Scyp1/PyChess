import pygame

from piece import *
from constants import *


class ChessBoard:
    """
    A chess board who will store :
     - the main chess board (2D List), where all the pieces are stored
     - the test chess board (2D List), that the chess board object use to check if one of the king
       is check
     - the possibles moves board, where the possibles moves of the selected piece are stored, just for
       the drawing of the chess board
    """

    def __init__(self):
        self.mainChessBoard = [[None for _ in range(ROWS)] for _ in range(COLS)]
        self.possiblesMovesBoard = [[None for _ in range(ROWS)] for _ in range(COLS)]
        self.testChessBoard = [[None for _ in range(ROWS)] for _ in range(COLS)]
        self.pieceSelected = ()

        self.initChessBoard()

    def __repr__(self):
        """
        Used for debugging
        @return: string
        @rtype: None
        """
        stringToReturn = ''

        for row in self.mainChessBoard:
            stringToReturn += str(row) + '\n'

        return stringToReturn

    def updateTestChessBoard(self):
        """
        Update the test chess board
        @return: None
        @rtype: None
        """
        for row in range(ROWS):
            for col in range(COLS):
                self.testChessBoard[col][row] = self.mainChessBoard[col][row]

    def resetPossiblesMovesBoard(self):
        """
        Reset the possibles moves board
        @return: None
        @rtype: None
        """
        self.possiblesMovesBoard = [[None for _ in range(ROWS)] for _ in range(COLS)]

    def initChessBoard(self):
        """
        Initialize the chess board
        @return: None
        @rtype: None
        """

        # Pawns
        for x in range(8):
            for y in [1, 6]:
                if y == 1:
                    self.mainChessBoard[y][x] = Pawn(x, y, 'black', 1)
                else:
                    self.mainChessBoard[y][x] = Pawn(x, y, 'white', -1)

        # Rooks
        self.mainChessBoard[0][7] = Rook(7, 0, 'black')
        self.mainChessBoard[0][0] = Rook(0, 0, 'black')
        self.mainChessBoard[7][0] = Rook(0, 7, 'white')
        self.mainChessBoard[7][7] = Rook(7, 7, 'white')

        # Knights
        self.mainChessBoard[0][1] = Knight(1, 0, 'black')
        self.mainChessBoard[0][6] = Knight(6, 0, 'black')
        self.mainChessBoard[7][1] = Knight(1, 7, 'white')
        self.mainChessBoard[7][6] = Knight(6, 7, 'white')

        # Bishops
        self.mainChessBoard[0][2] = Bishop(2, 0, 'black')
        self.mainChessBoard[0][5] = Bishop(5, 0, 'black')
        self.mainChessBoard[7][2] = Bishop(2, 7, 'white')
        self.mainChessBoard[7][5] = Bishop(5, 7, 'white')

        # Kings
        self.mainChessBoard[0][4] = King(4, 0, 'black')
        self.mainChessBoard[7][4] = King(4, 7, 'white')

        # Kings
        self.mainChessBoard[0][3] = Queen(3, 0, 'black')
        self.mainChessBoard[7][3] = Queen(3, 7, 'white')

    def movePiece(self, board, piece, pos2):
        """
        Move a piece from a position 1 to a position 2
        @param board: chessBoard.mainChessBoard or ChessBoard.testChessBoard
        @type board: List
        @param piece: the piece to move
        @type piece: Piece
        @param pos2: the new position of the piece after the move
        @type pos2: tuple
        @return: None
        @rtype: None
        """

        # Get the piece's initial position
        pos1 = piece.pos

        # Update the piece coord
        piece.updateCoords(pos2[0], pos2[1])

        # Delete the old piece of his old position and replace it to his new position on the board
        board[pos1[1]][pos1[0]] = None
        board[pos2[1]][pos2[0]] = piece

    def king(self, color):
        """
        Return the king object of the color asked in the chessboard
        @param color: the color of the king
        @type color: str
        @return: the king object
        @rtype: King
        """

        for row in self.mainChessBoard:
            for piece in row:
                if isinstance(piece, King):
                    if piece.color == color:
                        return piece

        print('There is no king in the chessboard')

    def isCheck(self, board, king):
        """
        Verify if the king is check
        @param board: ChessBoard.mainChessBoard or ChessBoard.testChessBoard
        @type board: List
        @param king: the king we need to check
        @type king: King
        @return: if the king is check
        @rtype: bool
        """

        # For each piece of the opponents, check if the king is not in the possibles moves of this piece
        for row in range(ROWS):
            for col in range(COLS):
                place = board[col][row]

                if isinstance(place, Piece):
                    piece = place

                    if piece.color != king.color:
                        possiblesMoves = piece.getPossiblesMoves(board)

                        for move in possiblesMoves:
                            if move == king.pos:
                                return True

        return False

    def isCheckMate(self, king):
        """
        Verify if teh king is checkmate
        @param king: the king we need to check
        @type king: King
        @return: if the king is checkmate
        @rtype: bool
        """

        self.updateTestChessBoard()

        # First, check if the king is check. If not, don't need to calculate the king is checkmate
        if self.isCheck(self.mainChessBoard, king):

            # For each piece
            for row in range(ROWS):
                for col in range(COLS):
                    place = self.mainChessBoard[col][row]

                    if isinstance(place, Piece):
                        piece = place

                        # If the piece has in the same color than the king
                        if piece.color == king.color:

                            # Get the possibles moves of this piece
                            possiblesMoves = piece.getPossiblesMoves(self.mainChessBoard)
                            initialPosition = piece.pos

                            # For each move, move the piece into the test chess board and check if the
                            # king is check. If not, the king isn't checkmate
                            for move in possiblesMoves:
                                # Move the piece

                                self.movePiece(self.testChessBoard, piece, move)

                                # If the king isn't check
                                if not self.isCheck(self.testChessBoard, king):
                                    # Update the piece's coords in his initial position
                                    piece.updateCoords(initialPosition[0], initialPosition[1])
                                    return False

                                # If not, update the test chess board and Update the piece's coords in his
                                # initial position
                                self.updateTestChessBoard()
                                piece.updateCoords(initialPosition[0], initialPosition[1])

                            # And finally, if the piece cannot save the king, do like just above and check
                            # if another piece can save the king
                            self.updateTestChessBoard()
                            piece.updateCoords(initialPosition[0], initialPosition[1])

            return True
        else:
            return False

    def drawSquares(self, window):
        """
        Draw the squares
        @param window: the window where we draw the squares
        @type window: pygame window
        @return: None
        @rtype: None
        """

        window.fill(MAROON)

        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def drawPiece(self, window, image, coord):
        """
        Draw a piece on a window
        @param window: the window where we draw the piece
        @type window: pygame window
        @param image: the image of the piece
        @type image: pygame image
        @param coord: the coord of the piece on a chessboard
        @type coord: tuple
        @return: None
        @rtype: None
        """

        row = coord[0]
        column = coord[1]

        window.blit(image, (row * SQUARE_SIZE + PIECE_PADDING, column * SQUARE_SIZE + PIECE_PADDING))

    def drawBoards(self, window):
        """
        Draw the two boards : the chess board and the possibles moves board
        @param window: the window where we draw the 2 boards
        @type window: pygame window
        @return: None
        @rtype: None
        """

        # Draw squares
        self.drawSquares(window)

        # Draw pieces
        for row in range(ROWS):
            for column in range(COLS):
                element = self.mainChessBoard[column][row]

                if isinstance(element, Piece):
                    if element.color == 'white':
                        if isinstance(element, Pawn):
                            self.drawPiece(window, WHITE_PAWN, (row, column))
                        elif isinstance(element, Rook):
                            self.drawPiece(window, WHITE_ROOK, (row, column))
                        elif isinstance(element, Knight):
                            self.drawPiece(window, WHITE_KNIGHT, (row, column))
                        elif isinstance(element, Bishop):
                            self.drawPiece(window, WHITE_BISHOP, (row, column))
                        elif isinstance(element, Queen):
                            self.drawPiece(window, WHITE_QUEEN, (row, column))
                        elif isinstance(element, King):
                            self.drawPiece(window, WHITE_KING, (row, column))

                    elif element.color == 'black':
                        if isinstance(element, Pawn):
                            self.drawPiece(window, BLACK_PAWN, (row, column))
                        elif isinstance(element, Rook):
                            self.drawPiece(window, BLACK_ROOK, (row, column))
                        elif isinstance(element, Knight):
                            self.drawPiece(window, BLACK_KNIGHT, (row, column))
                        elif isinstance(element, Bishop):
                            self.drawPiece(window, BLACK_BISHOP, (row, column))
                        elif isinstance(element, Queen):
                            self.drawPiece(window, BLACK_QUEEN, (row, column))
                        elif isinstance(element, King):
                            self.drawPiece(window, BLACK_KING, (row, column))

        # Draw possibles moves
        for row in range(ROWS):
            for column in range(COLS):
                element = self.possiblesMovesBoard[column][row]

                if element == 1:
                    pygame.draw.circle(window, GREEN,
                                       (row * SQUARE_SIZE + CIRCLE_PADDING, column * SQUARE_SIZE + CIRCLE_PADDING), 15)
