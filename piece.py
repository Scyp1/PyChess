class Piece:
	"""
	Template class for each piece
	Each piece has:
		- his coord (x, y) and a pos (a tuple with x and y into it)
		- his color
		- his updateCoords() method
		- his getPossiblesMoves() method
	"""

	def __init__(self, x, y, color):
		self.pos = (x, y)
		self.x = x
		self.y = y

		self.color = color

	def updateCoords(self, x, y):
		"""
		Update the piece's coords
		@param x: the new x coord of the piece
		@type x: int
		@param y: the new y coord of the piece
		@type y: int
		@return: None
		@rtype: None
		"""

		self.x = x
		self.y = y
		self.pos = (x, y)

	def getPossiblesMoves(self, chessBoard):
		"""
		Return the possibles moves of the piece
		@param chessBoard: the chessboard where the piece is
		@type chessBoard: List
		@return: the list of all the position where the piece can go
		@rtype: List
		"""

		return []


class Pawn(Piece):
	def __init__(self, x, y, color, direction):
		super().__init__(x, y, color)
		self.direction = direction
		self.firstMove = True

	def __repr__(self):
		"""Used for debugging"""
		return 'Pawn'

	def updateCoords(self, x, y):
		self.x = x
		self.y = y
		self.pos = (x, y)

		if self.firstMove:
			self.firstMove = False

	def getPossiblesMoves(self, chessBoard):
		possiblesMoves = []

		possiblePosition = (self.x, self.y + self.direction)
		possiblesEnemiesPositions = [(self.x - 1, self.y + self.direction), (self.x + 1, self.y + self.direction)]
		firstMovePosition = (self.x, self.y + self.direction * 2)

		# If the pawn can do his first move, check two case away
		if self.firstMove:
			# Check if the position is in the board
			if 7 >= firstMovePosition[0] >= 0 and 7 >= firstMovePosition[1] >= 0:
				place = chessBoard[firstMovePosition[1]][firstMovePosition[0]]

				if isinstance(place, Piece):
					piece = place

					if piece.color != self.color:
						possiblesMoves.append(firstMovePosition)
				else:
					possiblesMoves.append(firstMovePosition)

		# Again, check if the position is in the board
		if 7 >= possiblePosition[0] >= 0 and 7 >= possiblePosition[1] >= 0:
			place = chessBoard[possiblePosition[1]][possiblePosition[0]]

			if isinstance(place, Piece):
				piece = place

				if piece.color != self.color:
					possiblesMoves.append(possiblePosition)
			else:
				possiblesMoves.append(possiblePosition)

		# Check if an enemy piece is in the possibles moves that the pawn can do
		# when there is an enemy piece
		for possibleEnemyPosition in possiblesEnemiesPositions:
			# Check if the move is in the board
			if 7 >= possibleEnemyPosition[0] >= 0 and 7 >= possibleEnemyPosition[1] >= 0:
				place = chessBoard[possibleEnemyPosition[1]][possibleEnemyPosition[0]]

				if isinstance(place, Piece):
					piece = place

					if piece.color != self.color:
						possiblesMoves.append(possibleEnemyPosition)

		return possiblesMoves


class Rook(Piece):
	def __init__(self, *args, **kwargs):
		"""

		@rtype: object
		"""
		super().__init__(*args, **kwargs)

	def __repr__(self):
		"""Used for debugging"""
		return 'Rook'

	def getPossiblesMoves(self, chessBoard):
		possiblesMoves = []
		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

		# For each direction
		for direction in directions:
			n = 1
			while True:
				# Calculate the new position
				position = (self.x + direction[0] * n, self.y + direction[1] * n)

				# Check if the position is in the board
				if 7 >= position[0] >= 0 and 7 >= position[1] >= 0:
					place = chessBoard[position[1]][position[0]]

					# If the position is a piece, stop; but if it's an enemy piece, add it to the possibles moves
					if isinstance(place, Piece):
						piece = place

						if piece.color == self.color:
							break
						else:
							possiblesMoves.append(position)
							break
					# Else, continue to find new positions
					else:
						possiblesMoves.append(position)
				else:
					# If the position is not in the board, stop finding positions
					# in this direction
					break

				n += 1

		return possiblesMoves


class Knight(Piece):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def __repr__(self):
		"""Used for debugging"""
		return 'Knight'

	def getPossiblesMoves(self, chessBoard):
		possiblesMoves = []
		possiblesPlaces = [(2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

		# For each possible move, check if the piece can do the move; if yes, add it to the possibles moves list
		for place in possiblesPlaces:
			# Calculate the new position
			position = (self.x + place[0], self.y + place[1])

			# Check if the position is in the board
			if 7 >= position[0] >= 0 and  7 >= position[1] >= 0:
				place = chessBoard[position[1]][position[0]]

				# If the position is a piece, stop; but if it's an enemy piece, add it to the possibles moves
				if isinstance(place, Piece):
					piece = place

					if piece.color == self.color:
						continue
					else:
						possiblesMoves.append(position)
						continue
				# Else, continue to find new positions
				else:
					possiblesMoves.append(position)

		return possiblesMoves


class Bishop(Piece):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def __repr__(self):
		"""Used for debugging"""
		return 'Bishop'

	def getPossiblesMoves(self, chessBoard):
		possiblesMoves = []
		directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

		# For each direction
		for direction in directions:
			n = 1
			while True:
				# Find the new position
				position = (self.x + direction[0] * n, self.y + direction[1] * n)

				# Check if the position is in the board
				if 7 >= position[0] >= 0 and  7 >= position[1] >= 0:
					place = chessBoard[position[1]][position[0]]

					# If the position is a piece, stop; but if it's an enemy piece,
					# add it to the possibles moves then stop
					if isinstance(place, Piece):
						piece = place

						if piece.color == self.color:
							break
						else:
							possiblesMoves.append(position)
							break
					# Else, continue to find new positions
					else:
						possiblesMoves.append(position)
				else:
					break

				n += 1

		return possiblesMoves


class King(Piece):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def __repr__(self):
		"""Used for debugging"""
		return 'King'

	def getPossiblesMoves(self, chessBoard):
		possiblesMoves = []
		possiblesPlaces = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

		# For each possible move
		for position in possiblesPlaces:

			# Calculate the position
			position = (self.x + position[0], self.y + position[1])

			# Check if the position is in the board
			if 7 >= position[0] >= 0 and 7 >= position[1] >= 0:
				place = chessBoard[position[1]][position[0]]

				# If the position is a piece, stop; but if it's an enemy piece, add it to the possibles moves
				if isinstance(place, Piece):
					piece = place

					if piece.color != self.color:
						possiblesMoves.append(position)

				# Else, continue to find new positions
				else:
					possiblesMoves.append(position)

		return possiblesMoves


class Queen(Piece):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def __repr__(self):
		"""Used for debugging"""
		return 'Queen'

	def getPossiblesMoves(self, chessBoard):
		rookPlaceholder = Rook(self.x, self.y, self.color)
		bishopPlaceholder = Bishop(self.x, self.y, self.color)

		firstPossiblesMoves = rookPlaceholder.getPossiblesMoves(chessBoard)
		secondPossiblesMoves = bishopPlaceholder.getPossiblesMoves(chessBoard)

		del rookPlaceholder
		del bishopPlaceholder

		return firstPossiblesMoves + secondPossiblesMoves
