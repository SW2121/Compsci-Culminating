import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("backgrounds.jpg").convert()
pygame.display.set_caption('Quiz Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Font
font = pygame.font.SysFont('rockwell', 20)

# Quiz Data
questions = [
    [
        "Which of the following is a preventative measure that can be taken?",
        ["1. Two step authentication", "2. Downloading Antiviruses", "3. Restarting your computer daily", "4. Update software often"],
        0
    ],
    [
        "An email is suspicious if:",
        ["1. Does not have a subject", "2. From an unknown sender", "3. Written informally", "4. Has more than one recipient"],
        1
    ],
    [
        "Why are public WiFis dangerous?",
        ["1. Lacks encryption", "2. Easy for hackers to intercept data", "3. Used to spread malware", "4. All of the above"],
        3
    ],
    [
        "What is the name of an attack where a hacker positions themselves\nin between the user and the WiFi service?",
        ["1. Monkey-In-Middle attack", "2. DDOS attack", "3. Man-In-Middle Attack", "4. Ransomware attack"],
        2
    ],
    [
        "Which of the following actions can enhance social media privacy?",
        ["1. Sharing personal information freely", "2. Using two-factor authentication", "3. Accepting friend requests from unknown users", "4. Using the same password\nfor multiple accounts"],
        1
    ],
    [
        "What is a potential risk of not\nmanaging your social media privacy settings?",
        ["1. Increased engagement with friends and family", "2. Higher chances of getting popular online", "3. Exposure of personal information to strangers", "4. Better control over your online reputation"],
        2
    ]
]

current_question = 0
selected_option = -1
feedback = ""

def draw_button(text, x, y, w, h, color):
    pygame.draw.rect(screen, color, (x, y, w, h))
    button_text = font.render(text, True, BLACK)
    screen.blit(button_text, (x + 10, y + 10))

def draw_question():
    screen.blit(background, (0, 0))
    question_data = questions[current_question]

    question_text = font.render(question_data[0], True, WHITE)
    screen.blit(question_text, (20, 50))

    y_offset = 150
    for i in range(len(question_data[1])):
        option = question_data[1][i]
        color = WHITE
        if selected_option != -1:
            if i == selected_option:
                color = GREEN if i == question_data[2] else RED
        option_text = font.render(option, True, color)
        screen.blit(option_text, (20, y_offset))
        y_offset += 50

    if feedback:
        feedback_text = font.render(feedback, True, WHITE)
        screen.blit(feedback_text, (20, 400))

    draw_button("Press e", 650, 500, 200, 50, BLUE)
    draw_button("Go back", 20, 500, 200, 50, BLUE)

    # Load and render file content
    file_content = load_saved_passphrases("storecounter.txt")
    file_content_text = font.render("Correct Answers: " + str(file_content), True, WHITE)
    screen.blit(file_content_text, (20, 550))

def check_answer(selected):
    global feedback
    if selected == questions[current_question][2]:
        feedback = "Correct!"
        save_to_file("1", "storecounter.txt")  # Save "1" for each correct answer
    else:
        feedback = "Wrong!"

def save_to_file(text, filename="storecounter.txt"):
    file = open(filename, 'a')
    file.write(text + "\n")

def load_saved_passphrases(filename="storecounter.txt"):
    file = open(filename, 'r')
    lines = file.readlines()
    return len(lines)  # Count number of lines (each line represents a correct answer)

def clear_file(filename="storecounter.txt"):
    file = open(filename, 'a')
    file.write("")

def next_question():
    global current_question, selected_option, feedback
    current_question += 1
    if current_question >= len(questions):
        current_question = 0
    selected_option = -1
    feedback = ""

def return_question():
    global current_question, selected_option, feedback
    current_question -= 1
    if current_question < 0:
        current_question = len(questions) - 1
    selected_option = -1
    feedback = ""

# Main game loop
running = True
clear_file("storecounter.txt")  # Reset the counter at the start of the game

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 150 < y < 350:
                selected_option = (y - 150) // 50
                check_answer(selected_option)
            elif 20 <= x <= 120 and 500 <= y <= 550:
                return_question()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                next_question()

    draw_question()
    pygame.display.flip()

pygame.quit()
sys.exit()


