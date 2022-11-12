print("-"*90)
print("                PRINT  A  NAME  USING  LETTER  IMAGES                                            ")
print("-"*90)

import pygame
from pygame import mixer
name =input("\nENTER YOUR NAME :")

pygame.init()

clrs =(0,0,0)
w =len(name) * 390 + 100
win =pygame.display.set_mode((w,500))

# SET THE PYGAME WINDOW NAME
pygame.display.set_caption("MY NAME")
t={ }
t['a']=pygame.image.load('A IMAGE.png')
t['b']=pygame.image.load('B IMAGE.png')
t['c']=pygame.image.load('C IMAGE.png')
t['d']=pygame.image.load('D IMAGE.png')
t['e']=pygame.image.load('E IMAGE.png')
t['f']=pygame.image.load('F IMAGE.png')
t['g']=pygame.image.load('G IMAGE.png')
t['h']=pygame.image.load('H IMAGE.png')
t['i']=pygame.image.load('I IMAGE.png')
t['j']=pygame.image.load('J IMAGE.png')
t['k']=pygame.image.load('K IMAGE.png')
t['l']=pygame.image.load('L IMAGE.png')
t['m']=pygame.image.load('M IMAGE.png')
t['n']=pygame.image.load('N IMAGE.png')
t['o']=pygame.image.load('O IMAGE.png')
t['p']=pygame.image.load('P IMAGE.png')
t['q']=pygame.image.load('Q IMAGE.png')
t['r']=pygame.image.load('R IMAGE.png')
t['s']=pygame.image.load('S IMAGE.png')
t['t']=pygame.image.load('T IMAGE.png')
t['u']=pygame.image.load('U IMAGE.png')
t['v']=pygame.image.load('V IMAGE.png')
t['w']=pygame.image.load('W IMAGE.png')
t['x']=pygame.image.load('X IMAGE.png')
t['y']=pygame.image.load('Y IMAGE.png')
t['z']=pygame.image.load('Z IMAGE.png')

img =[]
for ch in name.lower():
    img.append(t[ch])
mixer.init()
mixer.music.load('happybirthday.mp3')
mixer.music.set_volume(0.5)
mixer.music.play()

while True:

    win.fill(clrs)
    x = 90
    for i in img:

            win.blit(i,(x,50))
            x += 350

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    pygame.display.update()

print("-"*90)
print("DAY -66 COMPLETED :)")
