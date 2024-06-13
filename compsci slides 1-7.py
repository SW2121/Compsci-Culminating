import pygame
import sys
from pygame.locals import QUIT

pygame.init()
print("Welcome to our game!")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 139)

# Initialize the screen
size = (900, 550)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Click a box')
background_image = pygame.image.load("background.png").convert()

# Use a smaller font for the stories
font_small = pygame.font.Font(None, 14)

# Font for buttons
font_buttons = pygame.font.Font(None, 20)
font_welcome = pygame.font.Font(None, 50)
font_subtitle = pygame.font.Font(None, 30)

# Load images
image_story1 = pygame.image.load("james.png").convert_alpha()
image_story2 = pygame.image.load("betty.png").convert_alpha()
image_story3 = pygame.image.load("augustine.png").convert_alpha()
image_story1 = pygame.transform.scale(image_story1, (200, 400))
image_story2 = pygame.transform.scale(image_story2, (200, 400))
image_story3 = pygame.transform.scale(image_story3, (200, 350))

def gotoMainPage(screen):
    screen.blit(background_image, (0, 0))
    
    # Large blue welcome sign
    text_welcome = font_welcome.render('Welcome!!', True, BLUE)
    screen.blit(text_welcome, (350, 300))
    
    # Subheading
    text_subheading = font_subtitle.render('Cyber Security Game by Monisha P, Mila P, and Sophia W', True, WHITE)
    screen.blit(text_subheading, (180, 350))
    
    # Draw buttons for main page
    button_stories = pygame.draw.rect(screen, BLUE, [50, 100, 150, 100])
    button_quiz = pygame.draw.rect(screen, BLUE, [250, 100, 150, 100])
    button_test_password = pygame.draw.rect(screen, BLUE, [450, 100, 150, 100])
    button_retrieve_passphrase = pygame.draw.rect(screen, BLUE, [640, 100, 170, 100])
    
    # Text on buttons
    text_stories = font_buttons.render('Stories', True, WHITE)
    text_quiz = font_buttons.render('Quiz', True, WHITE)
    text_test_password = font_buttons.render('Test Password', True, WHITE)
    text_retrieve_passphrase = font_buttons.render('Retrieve Passphrase', True, WHITE)
    
    # Display everything
    screen.blit(text_stories, (65, 140))
    screen.blit(text_quiz, (290, 140))
    screen.blit(text_test_password, (460, 140))
    screen.blit(text_retrieve_passphrase, (645, 140))

def gotoStories(screen):
    screen.blit(background_image, (0, 0))
    
    # Draw buttons for stories
    button_story1 = pygame.draw.rect(screen, BLUE, [50, 100, 700, 100])
    button_story2 = pygame.draw.rect(screen, BLUE, [50, 250, 700, 100])
    button_story3 = pygame.draw.rect(screen, BLUE, [50, 400, 700, 100])
    
    # Text on buttons
    text_story1 = font_buttons.render('Story 1: James', True, WHITE)
    text_story2 = font_buttons.render('Story 2: Betty', True, WHITE)
    text_story3 = font_buttons.render('Story 3: Augustine', True, WHITE)
    
    # Display everything
    screen.blit(text_story1, (150, 115))  # Moved to the right
    screen.blit(text_story2, (150, 265))  # Moved to the right
    screen.blit(text_story3, (150, 415))  # Moved to the right

def displayStory(screen, story_text, image):
    screen.blit(background_image, (0, 0))
    
    # Display the image
    screen.blit(image, (50, 50))  # Adjust the position as needed

    # Draw the dark blue box for the text background
    pygame.draw.rect(screen, DARK_BLUE, [300, 50, 550, 500])
    
    # Display the story text
    lines = story_text.split('\n')
    y_offset = 60  # Start slightly below the top of the box
    for line in lines:
        text_line = font_small.render(line, True, WHITE)
        screen.blit(text_line, (310, y_offset))  # Move text to the right
        y_offset += 20  # Adjust line spacing if needed
    
    # Back button
    button_back = pygame.draw.rect(screen, BLUE, [50, 500, 150, 50])
    text_back = font_buttons.render('Back', True, WHITE)
    screen.blit(text_back, (75, 510))
    
    # Home button in bottom right corner
    button_home = pygame.draw.rect(screen, BLUE, [700, 500, 150, 50])
    text_home = font_buttons.render('Home', True, WHITE)
    screen.blit(text_home, (725, 510))

def gotoQuiz(screen):
    screen.blit(background_image, (0, 0))

def gotoTestPassword(screen):
    screen.blit(background_image, (0, 0))

def gotoRetrievePassphrase(screen):
    screen.blit(background_image, (0, 0))

# Story texts
story1_text = """James quickly ran to his computer after a long day at school! As he opens his computer,
he reads “WINNER!!!”. Excitedly, he opens the email to find a link along with the message “Congratulations,
you won an Iphone 13, click on this link to collect your prize”. At first James was suspicious, he had
learned about phishing at school. However, how could he miss out on getting a NEW and FREE phone?
After all, he had begged his parents for a phone for months. Without further thought, he clicked the
link, and FLICK, in a heartbeat his screen had turned black. James started to panic, this couldn’t be
happening to him! He called for his parents who immediately shut down the computer. They realized that
the link had downloaded malicious software that stole all his information from the computer. They
immediately took over and called tech support for instructions on what to do next. James parents’ were
disappointed in him, after all James knew better. His teacher had always stated “Never click on a link from
an unknown email, NEVER”. However, this was an important lesson for James, he realized the importance of
cybersecurity and how a small mistake can put you at a great risk online. James was determined to stay safe
online from this moment forward.

He researched cyber security and ways he could stay safe online, here is what he found:

Phishing: A cyberattack that discloses a victim’s information after targeting them through false emails,
messages, etc.

Suspicious emails: Email is from an unknown sender, is unexpected, and the offer seems too good to be true.

Malware: Designed to damage or disable computers and steal victim’s information.

Post attack action plan: Disconnect from the internet and call tech support.

Preventative measures: Download antiviruses, use two-step authentication, and update software.
If sent an email, ensure that it is sent from a trustable source, hover over the url to check its validity,
check for suspicious spelling errors."""

story2_text = """Betty sits at a new café in town, sipping coffee and sampling new desserts.
She wants to post some of her snaps on Instagram, so she goes into her phone settings where she notices
a pop-up for free Wi-Fi nearby. Hoping to save data, Betty is about to press on it for connection when
suddenly, she recalls an article she read recently about the unsettling risks associated with public
Internet access. Nervous but intrigued, she decides to research the topic back home. Betty later finds
that hackers can easily intercept public Wi-Fi services, potentially leaving her social media accounts
compromised and private information stolen. They are dangerous for 3 main reasons: Public Wi-Fi often
lacks encryption, making it easy for hackers to intercept data; Hackers can position themselves between
the user and the connection point to steal information (Man-in-the-Middle Attacks); Can also be used to
spread malware. She then reads about the benefits of using a Virtual Private Network (VPN), which can
provide a safe network connection. Some major benefits include: VPNs encrypt data, making it difficult
for anyone to intercept or read it; Can mask your IP address, enhancing your online anonymity; Help bypass
regional restrictions on certain websites and services.

The next time Betty returns to the café, she makes sure to download a reputable VPN that allows her to
quickly browse the internet securely, avoiding the potential problems of relying on untrustworthy public
networks. As she enjoys her tea and peace of mind, Betty knows it’s a lesson in digital security that she
won’t forget."""

story3_text = """Augustine spends her evenings immersed in her favorite social media platforms, navigating
through feeds and connecting with friends. One evening, as Augustine scrolled through her Instagram feed in
her room, she received a friend request from someone she didn't recognize. Intrigued by the possibility of
making a new friend, she accepted the request without much thought. As Augustine explored her new friend's
profile, she noticed some red flags – vague information, no shared mutual friends, and an insistence on
engaging in personal conversations right away. Feeling a little suspicious, Augustine hesitated to respond
to their messages, remembering the warnings about phishing scams and social engineering tactics she had
learned about in her computer science class. Seeking advice, Augustine turned to her best friend, Rachel,
who shared her concerns. Together, they analyzed the situation and recognized the potential risks of
engaging with someone who seemed eager to gather personal information. Rachel reminded Augustine about the
importance of privacy settings, two-factor authentication, and being cautious about sharing sensitive details
online. With Rachel's help, Augustine decided to take control of the situation. She adjusted her privacy
settings to limit what information strangers could access, enabled two-factor authentication for added
security, and reported the suspicious account to the platform administrators. From that day forward, Augustine
remained vigilant and cautious when interacting with new people online. She understood the importance of
protecting her personal information and staying informed about potential online threats. Through this
experience, Augustine learned that digital security was an essential aspect of her online presence,
ensuring she could enjoy the benefits of social media while staying safe from potential risks."""

# Initial page
pageNumber = 'main'

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            
            if pageNumber == 'main':
                if 50 <= mouse_pos[0] <= 200 and 100 <= mouse_pos[1] <= 200:
                    pageNumber = 'stories'
                elif 250 <= mouse_pos[0] <= 400 and 100 <= mouse_pos[1] <= 200:
                    pageNumber = 'quiz'
                elif 450 <= mouse_pos[0] <= 600 and 100 <= mouse_pos[1] <= 200:
                    pageNumber = 'test_password'
                elif 640 <= mouse_pos[0] <= 810 and 100 <= mouse_pos[1] <= 200:
                    pageNumber = 'retrieve_passphrase'
            elif pageNumber == 'stories':
                if 50 <= mouse_pos[0] <= 750 and 100 <= mouse_pos[1] <= 200:
                    pageNumber = 'story1'
                elif 50 <= mouse_pos[0] <= 750 and 250 <= mouse_pos[1] <= 350:
                    pageNumber = 'story2'
                elif 50 <= mouse_pos[0] <= 750 and 400 <= mouse_pos[1] <= 500:
                    pageNumber = 'story3'
            elif pageNumber in ['story1', 'story2', 'story3']:
                if 50 <= mouse_pos[0] <= 200 and 500 <= mouse_pos[1] <= 550:
                    pageNumber = 'stories'
                elif 700 <= mouse_pos[0] <= 850 and 500 <= mouse_pos[1] <= 550:
                    pageNumber = 'main'
                    
    # Render the appropriate page
    if pageNumber == 'main':
        gotoMainPage(screen)
    elif pageNumber == 'stories':
        gotoStories(screen)
    elif pageNumber == 'story1':
        displayStory(screen, story1_text, image_story1)
    elif pageNumber == 'story2':
        displayStory(screen, story2_text, image_story2)
    elif pageNumber == 'story3':
        displayStory(screen, story3_text, image_story3)
    elif pageNumber == 'quiz':
        gotoQuiz(screen)
    elif pageNumber == 'test_password':
        gotoTestPassword(screen)
    elif pageNumber == 'retrieve_passphrase':
        gotoRetrievePassphrase(screen)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
