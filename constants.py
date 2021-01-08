import pygame

WIDTH = HEIGHT = 600
RESOLUTION = (WIDTH, HEIGHT)

ROWS = COLS = 8

SQUARE_SIZE = WIDTH // ROWS

IMAGE_WIDTH = IMAGE_HEIGHT = 60
PIECE_PADDING = (SQUARE_SIZE - IMAGE_WIDTH) // 2

CIRCLE_PADDING = SQUARE_SIZE // 2

# rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAROON = (222, 184, 135)
GREEN = (0, 255, 0)

# images
BLACK_PAWN = pygame.image.load('assets/pieces/black/pawn.png')
BLACK_ROOK = pygame.image.load('assets/pieces/black/rook.png')
BLACK_KNIGHT = pygame.image.load('assets/pieces/black/knight.png')
BLACK_BISHOP = pygame.image.load('assets/pieces/black/bishop.png')
BLACK_KING = pygame.image.load('assets/pieces/black/king.png')
BLACK_QUEEN = pygame.image.load('assets/pieces/black/queen.png')

WHITE_PAWN = pygame.image.load('assets/pieces/white/pawn.png')
WHITE_ROOK = pygame.image.load('assets/pieces/white/rook.png')
WHITE_KNIGHT = pygame.image.load('assets/pieces/white/knight.png')
WHITE_BISHOP = pygame.image.load('assets/pieces/white/bishop.png')
WHITE_KING = pygame.image.load('assets/pieces/white/king.png')
WHITE_QUEEN = pygame.image.load('assets/pieces/white/queen.png')
