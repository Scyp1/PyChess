from chess_board import *
from piece import Piece
from constants import RESOLUTION, BLACK, WHITE, SQUARE_SIZE


class Game:
	"""A chess game"""

	def __init__(self):
		pygame.init()
		self.window = pygame.display.set_mode(RESOLUTION)
		pygame.display.set_caption('Chess Game')

		self.chessBoard = ChessBoard()

		self.run = True
		self.turn = 'white'
		self.turnKing = self.chessBoard.king(self.turn)

	def popup(self, title, message):
		"""Show the end popup"""
		popup = pygame.display.set_mode((500, 300))
		pygame.display.set_caption(title)

		font = pygame.font.Font('assets/fonts/Roboto/Roboto-Light.ttf', 20)
		text = font.render(message, True, BLACK, WHITE)
		textRect = text.get_rect()
		textRect.center = (250, 150)

		run = True

		while run:
			popup.fill(WHITE)
			popup.blit(text, textRect)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

			pygame.display.update()

	def start(self):
		"""Start a chess game"""
		while self.run:

			for event in pygame.event.get():

				# If the user want to leave, stop the game
				if event.type == pygame.QUIT:
					self.run = False

				# If the user clicked, check where he clicked
				elif event.type == pygame.MOUSEBUTTONUP:

					# Get the clicked place on the chess board and on the possibles moves board
					mousePosition = pygame.mouse.get_pos()
					boardCoord = (mousePosition[0] // SQUARE_SIZE, mousePosition[1] // SQUARE_SIZE)

					place = self.chessBoard.mainChessBoard[boardCoord[1]][boardCoord[0]]
					possibleMove = self.chessBoard.possiblesMovesBoard[boardCoord[1]][boardCoord[0]]

					# If the user clicked on a piece, show the possibles moves of this piece
					if isinstance(place, Piece):
						piece = place

						if piece.color == self.turn:
							# Change the piece selected on the chess board
							self.chessBoard.pieceSelected = boardCoord

							# Reset the possibles moves board
							self.chessBoard.resetPossiblesMovesBoard()

							# Get the possibles moves of the clicked piece
							possiblesMoves = piece.getPossiblesMoves(self.chessBoard.mainChessBoard)

							# Add the possibles moves on the possibles moves board
							for move in possiblesMoves:
								self.chessBoard.possiblesMovesBoard[move[1]][move[0]] = 1

					# Else, if the user clicked on a possible move, move the piece selected to this possible move's place
					# But first, check if the king of the player who has the turn is in check after his move
					if possibleMove == 1:
						# Move the piece
						self.chessBoard.movePiece(self.chessBoard.mainChessBoard, self.chessBoard.mainChessBoard[self.chessBoard.pieceSelected[1]][self.chessBoard.pieceSelected[0]], boardCoord)

						# If the king of the player who has the turn is check, reverse the move just above
						if self.chessBoard.isCheck(self.chessBoard.mainChessBoard, self.turnKing):
							print('Your king is check !')
							self.chessBoard.movePiece(self.chessBoard.mainChessBoard, self.chessBoard.mainChessBoard[boardCoord[1]][boardCoord[0]], self.chessBoard.pieceSelected)
						else:
							# Reset the possibles moves board
							self.chessBoard.resetPossiblesMovesBoard()

							# Swap the turn
							if self.turn == 'white':
								self.turn = 'black'
							else:
								self.turn = 'white'

							# Update the turn king (the king of the player who plays)
							self.turnKing = self.chessBoard.king(self.turn)

							# If the turnking is checkmate, stop the game
							if self.chessBoard.isCheckMate(self.turnKing):
								if self.turn == 'white':
									winner = 'black'
								else:
									winner = 'white'

								self.run = False
								self.popup('Game finished', f'{winner.capitalize()} player won the game !')

					# Else (the user clicked on a blank case), clean the possibles moves board and the piece selected
					if not isinstance(place, Piece) and possibleMove != 1:
						self.chessBoard.pieceSelected = ()
						self.chessBoard.resetPossiblesMovesBoard()

			# Update the user's screen
			self.chessBoard.drawBoards(self.window)
			pygame.display.update()
