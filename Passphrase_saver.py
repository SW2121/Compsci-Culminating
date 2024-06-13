import pygame
import sys
from pygame.locals import QUIT
pygame.init()

# BACKGROUND
screen = pygame.display.set_mode((640, 480))
background = pygame.image.load("background.png").convert()

# TEXT
my_font = pygame.font.SysFont('comicsansms', 20)
my_font2 = pygame.font.SysFont('rockwell', 12)
button_font = pygame.font.SysFont('comicsansms', 20)  # Smaller font for button text
my_font.set_bold(True)
my_font.set_underline(True)
blah = "WHAT IS A PASSPHRASE?"
another = "A passphrase is a password made from a series of random  words. \n A passphrase is a strong password as  it is harder to guess and \n hack into, but  is easy for the creator to remember. Passwords are \n often only 6-12  characters while passphrases can span characters!\n The longer the passphrase, the more secure it is. You can \n choose to add spaces or capitalize different  letters in your \n passphrase to ensure that  it is near  impossible to hack!"
label = my_font.render(blah, False, (173, 160, 230))

another_lines = another.split('\n')
labels2 = [my_font2.render(line, False, (255, 255, 255)) for line in another_lines]

def gotoPage1(screen, background):
    screen.blit(background, (0, 0))
    screen.blit(label, (100, 100))
    for i, line in enumerate(labels2):
        screen.blit(line, (120, 160 + i * 30))

    # Draw button
    pygame.draw.rect(screen, (30, 144, 255), [220, 360, 200, 60], 0)  # Lowered the button
    button_text = button_font.render("Click to enter \n passphrases", True, (255, 255, 255))
    text_rect = button_text.get_rect(center=(320, 390))  # Adjusted to match the new button position
    screen.blit(button_text, text_rect)
    pygame.display.flip()

def gotoPage2(screen, background):

# BACKGROUND
    screen = pygame.display.set_mode((640, 480))
    background = pygame.image.load("background.png").convert()

    # TEXT
    my_font = pygame.font.SysFont('comicsansms', 30)
    my_font2 = pygame.font.SysFont('rockwell', 16)
    my_font.set_bold(True)
    my_font.set_underline(True)
    blah = "ENTER PASSPHRASE"
    label = my_font.render(blah, False, (173, 216, 230))

    field_surf = pygame.Surface((300, 50)).convert()
    field_surf.fill((255, 255, 255))

    input_font = pygame.font.SysFont("helvetica", 20)
    field_value = ""
    field = input_font.render(field_value, True, (0, 0, 0))

    button_font = pygame.font.SysFont("helvetica", 20)

    clock = pygame.time.Clock()

    def save_to_file(text, filename="passphrase.txt"):
        with open(filename, 'a') as file:
            file.write(text + "\n")

    def load_saved_passphrases(filename="passphrase.txt"):
        with open(filename, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]

    show_saved_phrases = False

    while True:
        clock.tick(30)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:  # when enter is pressed, save text to file
                    save_to_file(field_value)  # Save to file
                    field_value = ""  # Clear the input field after saving
                elif ev.key == pygame.K_BACKSPACE and len(field_value) > 0:
                    field_value = field_value[:-1]  # cut off last character
                elif (ev.unicode.isalnum() or ev.key == pygame.K_SPACE) and len(field_value) < 20:
                    field_value += ev.unicode  # adds character value of key
                field = input_font.render(field_value, True, (0, 0, 0))
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:  # Left mouse button clicked
                    mouse_pos = pygame.mouse.get_pos()
                    if 400 <= mouse_pos[0] <= 600 and 300 <= mouse_pos[1] <= 360:
                        show_saved_phrases = True

        # Draw everything on the screen
        screen.blit(background, (0, 0))
        screen.blit(label, (100, 100))
        screen.blit(field_surf, (40, 195))  # Draw the input field background
        screen.blit(field, (50, 210))  # Draw the input text relative to field_surf

        if show_saved_phrases:
            saved_phrases = load_saved_passphrases()
            # Draw white background rectangle
            pygame.draw.rect(screen, (255, 255, 255), [50, 270, 300, 150])

            y_offset = 290  # Starting y position for the first saved phrase
            for phrase in saved_phrases:
                saved_text = my_font2.render(phrase, True, (0, 0, 0))
                screen.blit(saved_text, (60, y_offset))
                y_offset += 20

        # Draw "see saved passphrases" button
        pygame.draw.rect(screen, (30, 144, 255), [400, 300, 200, 60], 0)
        button_text = button_font.render("see saved passphrases", True, (255, 255, 255))
        text_rect = button_text.get_rect(center=(500, 330))
        screen.blit(button_text, text_rect)

        # Draw "save passphrase" button
        pygame.draw.rect(screen, (30, 144, 255), [400, 170, 200, 60], 0)
        button_text = button_font.render("Click 'enter' to\nsave passphrases", True, (255, 255, 255))
        text_rect = button_text.get_rect(center=(500, 200))
        screen.blit(button_text, text_rect)

        pygame.display.flip()
        
        pygame.display.flip()
#######################################################
pageNumber = 1

clock = pygame.time.Clock()
while True:
    if pageNumber == 1:
        gotoPage1(screen, background)
    elif pageNumber == 2:
        gotoPage2(screen, background)

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 220 <= x <= 420 and 350 <= y <= 410 and pageNumber == 1:  # Updated for new button position
                pageNumber = 2

    pygame.display.update()
    
 