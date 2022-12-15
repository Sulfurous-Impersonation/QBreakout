import pygame

from . import globals, resources

def draw_statevector_grid(screen):
    font = resources.Font()
    basis_states = [
        '|000>',
        '|001>',
        '|010>',
        '|011>',
        '|100>',
        '|101>',
        '|110>',
        '|111>'
    ]
    statevector_height = int(round(globals.FIELD_HEIGHT / len(basis_states)))

    for i in range(len(basis_states)):
        text = font.vector_font.render(basis_states[i], 1, globals.WHITE)
        screen.blit(text, (globals.WINDOW_WIDTH - text.get_width(),
                            i*statevector_height + text.get_height()))

def draw_score(screen, classical_score, quantum_score):
    font = resources.Font()

    text = font.player_font.render("LIVES", 1, globals.GRAY)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH*0.7, globals.WIDTH_UNIT*2))
    screen.blit(text, text_pos)

    text = font.score_font.render(str(globals.WIN_SCORE - classical_score), 1, globals.GRAY)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH*0.7, globals.WIDTH_UNIT*8))
    screen.blit(text, text_pos)

    text = font.player_font.render("SCORE", 1, globals.GRAY)
    text_pos = text.get_rect(center=(screen.get_width() - globals.WINDOW_WIDTH*0.7, globals.WIDTH_UNIT*2))
    screen.blit(text, text_pos)

    text = font.score_font.render(str(quantum_score), 1, globals.GRAY)
    text_pos = text.get_rect(center=(screen.get_width() - globals.WINDOW_WIDTH*0.7, globals.WIDTH_UNIT*8))
    screen.blit(text, text_pos)

def draw_wall(screen, wall):
    pygame.draw.rect(screen, globals.WHITE, wall.rect)

def draw_blocks(screen, blocks):
    for i in blocks:
        pygame.draw.rect(screen, i.color, i)
        #print(i)
