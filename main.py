import pygame, sys
from pygame.locals import *
import random

pygame.init()


WIDTH = 800
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ROCK PAPER SCISSORS")
clock = pygame.time.Clock()

def setBg():
    bg = pygame.image.load("./img/BG.png")
    screen.blit(bg, (0,0))

def setTitle():
    title = pygame.image.load("./img/title.png").convert_alpha()
    title_rect = title.get_rect(center=(int(WIDTH/2),50))
    screen.blit(title, title_rect)




def check_winner():
    if player_choice.value == "rock" and bot_choice.value == "rock":
        print("draw")
    elif player_choice.value == "rock" and bot_choice.value == "paper":
        print("lose")
    elif player_choice.value == "rock" and bot_choice.value == "scissors":
        print("win")

    if player_choice.value == "paper" and bot_choice.value == "rock":
        print("win")
    elif player_choice.value == "paper" and bot_choice.value == "paper":
        print("draw")
    elif player_choice.value == "paper" and bot_choice.value == "scissors":
        print("lose")

    if player_choice.value == "scissors" and bot_choice.value == "rock":
        print("lose")
    elif player_choice.value == "scissors" and bot_choice.value == "paper":
        print("win")
    elif player_choice.value == "scissors" and bot_choice.value == "scissors":
        print("draw")

    bot_choice.image = pygame.image.load(f"./img/{bot_choice.value}.png").convert_alpha()
    bot_choice.image = pygame.transform.rotate(bot_choice.image, 180)
    bot_choice.value = random.choice(["rock", "paper", "scissors"])





class Button(pygame.sprite.Sprite):
    def __init__(self, image, x, y, value):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.value = value
        self.bounce = "top"
        self.pos_y = self.rect.y

        # VALUES
        # 1 - ROCK
        # 2 - PAPER 
        # 3 - SCISSORS

    def animate_bounce(self):
        if self.bounce == "top":
            self.rect.y -= 2
            if self.rect.y <= self.pos_y - 10:
                self.bounce = "bottom"

        if self.bounce == "bottom":
            self.rect.y += 2
            if self.rect.y >= self.pos_y:
                self.bounce = "top"
    def update(self):
        player_choice.set_value(self.value)
        bot_choice.image = pygame.image.load("./img/hidden.png").convert_alpha()
        bot_choice.value = random.choice(["rock", "paper", "scissors"])





class Choice(pygame.sprite.Sprite):
    def __init__(self, x, y, bot=False):
        pygame.sprite.Sprite.__init__(self)
        self.value = random.choice(["rock", "paper", "scissors"])
        self.image = pygame.image.load(f"./img/{self.value}.png").convert_alpha()
        self.bot = bot
        self.bounce = "top"
        self.bot_bounce = "bottom"

        if self.bot:
            self.image = pygame.image.load("./img/hidden.png").convert_alpha()

        self.rect = self.image.get_rect(center=(x, y))
        self.pos_y = self.rect.y

    def set_value(self, value):
        if self.bot == False:
            self.value = value
            self.image = pygame.image.load(f'./img/{value}.png').convert_alpha()


    def update(self):
        if self.bot:
            if self.bot_bounce == "top":
                self.rect.y -= 1
                if self.rect.y <= self.pos_y - 5:
                   self.bot_bounce = "bottom"

            if self.bot_bounce == "bottom":
                self.rect.y += 1
                if self.rect.y >= self.pos_y:
                    self.bot_bounce = "top"

        else:

            if self.bounce == "top":
                self.rect.y -= 1
                if self.rect.y <= self.pos_y - 5:
                   self.bounce = "bottom"

            if self.bounce == "bottom":
                self.rect.y += 1
                if self.rect.y >= self.pos_y:
                    self.bounce = "top"


        #self.image = pygame.transform.scale()









    





# BUTTONS
rock_button = Button("./img/btn-rock.png", int((WIDTH/2)-175), HEIGHT-75, "rock")
paper_button = Button("./img/btn-paper.png", 400, HEIGHT-85, "paper")
scissors_button = Button("./img/btn-scissors.png", int((WIDTH/2)+175), HEIGHT-85, "scissors")

button_group = pygame.sprite.Group()
button_group.add(rock_button)
button_group.add(paper_button)
button_group.add(scissors_button)

# CHOICE
player_choice = Choice(int(WIDTH/2), 290)
bot_choice = Choice(int(WIDTH/2), 150, True)

player_choice_group = pygame.sprite.GroupSingle()
player_choice_group.add(player_choice)

bot_choice_group = pygame.sprite.GroupSingle()
bot_choice_group.add(bot_choice)

# BTN FIGHT
btn_figth = pygame.image.load("./img/btn_fight.png").convert_alpha()
btn_fight_rect = btn_figth.get_rect(center=(int(WIDTH/2), 400))

while True:
    setBg()
    setTitle()

    button_group.draw(screen)
    bot_choice_group.draw(screen)
    player_choice_group.draw(screen)

    player_choice.update()
    bot_choice.update()

    screen.blit(btn_figth, btn_fight_rect)

    if rock_button.rect.collidepoint(pygame.mouse.get_pos()):
        rock_button.animate_bounce()
    if paper_button.rect.collidepoint(pygame.mouse.get_pos()):
        paper_button.animate_bounce()
    if scissors_button.rect.collidepoint(pygame.mouse.get_pos()):
        scissors_button.animate_bounce()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if rock_button.rect.collidepoint(event.pos):
                rock_button.update()
            elif paper_button.rect.collidepoint(event.pos):
                paper_button.update()
            elif scissors_button.rect.collidepoint(event.pos):
                scissors_button.update()

            if btn_fight_rect.collidepoint(event.pos):
                check_winner()




    clock.tick(FPS)
    pygame.display.update()


