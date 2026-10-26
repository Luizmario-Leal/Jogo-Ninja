import pgzrun
import random
from pygame import Rect

WIDTH = 800
HEIGHT = 600

white = (255, 255, 255)

bg = Actor("fundo")

player = Actor("ninja-direita")
player.x = 400
player.y = 550

coin = Actor("moeda")
coin.x = random.randint(20, 780)
coin.y = 0

shuriken = Actor("shuriken")
shuriken.x = random.randint(20, 780)
shuriken.y = 0

bomb = Actor("bomba")
bomb.x = random.randint(20, 780)
bomb.y = 0

score = 1
lives = 3
game_over = False
som = False
menu_principal = True
music_on = True

sounds.backgraund_music.set_volume(0.2)
sounds.backgraund_music.play()

def on_mouse_down(pos):
    global menu_principal, music_on, game_over, score, lives

    if game_over and Rect(300, 325, 200, 50).collidepoint(pos):
        menu_principal = True
        game_over = False
        score = 1
        lives = 3
        return

    if menu_principal:
        area_jogar = Rect(300, 190, 200, 70)
        area_musica = Rect(300, 260, 200, 50)
        area_sair = Rect(300, 310, 200, 50)

        if area_jogar.collidepoint(pos):
            menu_principal = False

        elif area_musica.collidepoint(pos):
            if music_on:
                sounds.backgraund_music.stop()
                music_on = False
            else:
                sounds.backgraund_music.set_volume(0.2)
                sounds.backgraund_music.play()
                music_on = True

        elif area_sair.collidepoint(pos):
            quit()

def update():
    global score, lives, game_over, som

    if menu_principal or game_over:
        return

    #Ninja#
    if keyboard.left:
        player.x -= 5
        player.image = "ninja-esquerda"
    if keyboard.right:
        player.x += 5
        player.image = "ninja-direita"

    if player.x < 60:
        player.x = 60
    if player.x > 740:
        player.x = 740

    #Moeda#
    coin.y += 4 + score / 5

    if coin.y > 600:
        coin.x = random.randint(20, 780)
        coin.y = 0

    if coin.colliderect(player):
        coin.x = random.randint(20, 780)
        coin.y = 0
        score +=1
        sounds.collet.set_volume(0.1)
        sounds.collet.play()

    #Shuriken#
    shuriken.y += 4

    if shuriken.y > 600:
        shuriken.x = random.randint(20, 780)
        shuriken.y = 0

    if shuriken.colliderect(player):
        shuriken.x = random.randint(20, 780)
        shuriken.y = 0
        score -= 1
        sounds.lose.set_volume(0.2)
        sounds.lose.play()

    #bomb#
    bomb.y += 5
    
    if bomb.y > 600:
        bomb.x = random.randint(20, 780)
        bomb.y = 0
    
    if bomb.colliderect(player):
        bomb.x = random.randint(20, 780)
        bomb.y = 0
        lives -= 1
        sounds.explosion.set_volume(0.1)
        sounds.explosion.play()

    if lives <= 0:
        game_over = True
        coin.y = 0
        bomb.y= 0
        shuriken.y = 0
        if som == False:
            sounds.lose.set_volume(0.2)
            sounds.lose.play()
            som = True


def draw():
    bg.draw()

    if menu_principal:
        # Botão JOGAR
        screen.draw.text("JOGAR", center=(400, 225), color=white, fontname="publicpixel", fontsize=30)

        # Botão de música
        if music_on:
            texto_musica = "MUSICA-ON"
        else:
            texto_musica = "MUSICA-OFF"

        screen.draw.text(texto_musica, center=(400, 285), color=white, fontname="publicpixel", fontsize=18)
        screen.draw.text("SAIR", center=(400, 345), color=white, fontname="publicpixel", fontsize=18)

        return

    if game_over:
        screen.draw.text("FIM DO JOGO", center=(400, 225), color=(white ), fontname="publicpixel", fontsize=30)
        screen.draw.text("PONTUACAO FINAL: " + str(score), center=(400, 285), color=(white ), fontname="publicpixel", fontsize=15)
        screen.draw.text("MENU", center=(400, 350), color=white, fontname="publicpixel", fontsize=15)
    else:
        player.draw()
        coin.draw()
        shuriken.draw()
        bomb.draw()
        screen.draw.text("Pontuacao: " + str(score), (15, 10), color=(white ), fontname="publicpixel", fontsize=15)
        screen.draw.text("Vidas: " + str(lives), (650, 10), color=(white ), fontname="publicpixel", fontsize=15)
        
pgzrun.go()