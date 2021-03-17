import pygame
import random

pygame.init()

progress = 0

into = True

black = [0, 0, 0]
white = [255, 255, 255]
intoWhite = [249, 244, 244]
green = [0, 255, 0]

screenWidth = 600
screenHeigth = 450
size = [screenWidth, screenHeigth]

font = pygame.font.SysFont("Comic Sans MS", 25)

intoPic = pygame.image.load("images/Can You Surive Pic.png")
cory = "audio/Cory in the House - Opening Sequence.mp3"
coryPic = pygame.image.load("images/CoryBaxterFull.png")
coryMusicBool = False
coryPicBool = False
basic = "audio/basic song.mp3"
shrekPicBool = False
shrekMusicBool = False
shrek = "audio/Shrek's Fairytale Freestyle.mp3"
shrekPic = pygame.image.load("images/shrek.png")

clock = pygame.time.Clock()
clock.tick(10)

count = 0
escPressed = False

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Loading...')

escMessageText = "Press Esc to cancel"
escMessage = font.render(escMessageText, False, white)
escMessageText_2 = "You Can't Leave"
escMessage_2 = font.render(escMessageText_2, False, white)


def textobjecte(text, color, size):
    if size == "small":
        textsuraface = font.render(text, True, color)

        return textsuraface, textsuraface.get_rect()


def loading(progress):
    text = ""

    if progress < 101:
        text = font.render("loading: " + str(int(progress)) + "%", True, green)

    screen.blit(text, (300, 100))


def message_to_screen(msg, color, y_displace, size="small"):
    textsurf, textrect = textobjecte(msg, color, size)
    textrect.center = (screenWidth/2), (screenHeigth/2) + y_displace

    screen.blit(textsurf, textrect)


def playcory():
    pygame.mixer.music.load(cory)
    pygame.mixer.music.play(-1)


def playshrek():
    pygame.mixer.music.load(shrek)
    pygame.mixer.music.play(-1)


def basicsong():
    pygame.mixer.music.load(basic)
    pygame.mixer.music.play(-1)


basicsong()

while into == True:
    pygame.event.pump()
    screen.fill(intoWhite)
    screen.blit(intoPic, (75, 0))
    intoKey = pygame.key.get_pressed()
    pygame.display.flip()
    if intoKey[pygame.K_SPACE]:
        into = False


while progress/2 < 100:
    timeCount = random.randint(1, 10000)
    increase = random.randint(1, 10)
    progress += increase/10000
    screen.fill(black)
    pygame.event.pump()
    pygame.draw.rect(screen, white, [300, 50, 200, 50])
    pygame.draw.rect(screen, black, [301, 51, 198, 48])

    if (progress/2) > 100:
        pygame.draw.rect(screen, white, [302, 52, 196, 46])
    else:
        pygame.draw.rect(screen, white, [302, 52, progress, 46])

    if coryMusicBool == True:
        pygame.mixer.music.stop()
        playcory()
        coryMusicBool = False
    if coryPicBool== True:
        screen.blit(coryPic, (0, 0))

    if shrekMusicBool == True:
        pygame.mixer.music.stop()
        playshrek()
        shrekMusicBool = False
    if shrekPicBool == True:
        screen.blit(shrekPic, (100, 0))

    if escPressed == False:
        screen.blit(escMessage, (50, 50))

    if escPressed == True:
        screen.blit(escMessage_2, (50, 50))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.mixer.music.stop()
        progress = 0
        escPressed = True

    keys2 = pygame.key.get_pressed()
    if keys2[pygame.K_c]:
        coryMusicBool = True
        coryPicBool = True

    keys3 = pygame.key.get_pressed()
    if keys3[pygame.K_s]:
        shrekPicBool = True
        shrekMusicBool = True

    if progress/2 >= 100:
        progress = 200

    loading(progress/2)
    pygame.display.flip()