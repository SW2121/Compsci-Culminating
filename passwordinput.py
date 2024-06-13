import pygame
import pygame.freetype

# Initialize Pygame
pygame.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

# Create screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Password Strength Checker")

# Load background image
background = pygame.image.load("backgrounds.jpg").convert()

# Font
font = pygame.freetype.SysFont(None, FONT_SIZE)

def calculate_time_to_hack(password):
    length = len(password)
    if 1 <= length <= 8:
        return "2 minutes"
    elif 8 < length <= 12:
        return "2 months"
    elif 12 < length <= 18:
        return "2 years"
    elif length > 18:
        return "infinity"
    return "unknown"

def main():
    clock = pygame.time.Clock()
    input_box = pygame.Rect(300, 250, 200, 50)
    active = False
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    password = ''
    time_to_hack = ''

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        time_to_hack = calculate_time_to_hack(password)
                    elif event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode
        
        # Draw background first
        screen.blit(background, (0, 0))

        # Render the current password
        txt_surface, _ = font.render(password, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 10))
        
        # Render the time to hack
        if time_to_hack:
            time_surface, _ = font.render(f"Time to Guess: {time_to_hack}", BLACK)
            screen.blit(time_surface, (300, 350))
        
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()

