import pygame
pygame.init()
W, H = 332, 541
sc = pygame.display.set_mode((W, H))
bg = pygame.image.load("week7/images/spotify-music-player.jpg")
base_img = pygame.image.load("week7/images/skrippi.jpg")
white_surf = pygame.Surface((230, 60))
white_surf.fill("white")
myfont = pygame.font.Font("week7/fonts/Lato-Black.ttf", 25)
music_name = myfont.render('house with normal phenomena', False, 'black')
myfont = pygame.font.Font("week7/fonts/Lato-Black.ttf", 15)
skrippi = myfont.render('Skryptonite', False, 'black')
sound1 = pygame.mixer.Sound('week7/music/konyak.mp3')
sound2 = pygame.mixer.Sound('week7/music/ostavetonam.mp3')
sound3 = pygame.mixer.Sound('week7/music/tansuisama.mp3')
sound4 = pygame.mixer.Sound('week7/music/priton.mp3')
sound5 = pygame.mixer.Sound('week7/music/sny.mp3')
sound6 = pygame.mixer.Sound('week7/music/vecherinka.mp3')
music = [sound1, sound2, sound3, sound4, sound5, sound6]
music[0].play()
i = 0
while True:
    sc.fill("white")
    sc.blit(bg, (0, 0))
    sc.blit(base_img, (29, 22))
    sc.blit(white_surf, (17, 390))
    white_surf.blit(music_name, (0, 0))
    white_surf.blit(skrippi, (0, 30))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                music[i].stop()
                if i==5:
                    i = 0
                else:
                    i += 1
                music[i].play()
            elif event.key == pygame.K_LEFT:
                music[i].stop()
                if i==0:
                    i = 5
                else:
                    i -= 1
                music[i].play()
            elif event.key == pygame.K_SPACE:
                music[i].stop()
            elif event.key == pygame.K_TAB:
                music[i].play()
        elif event.type == pygame.QUIT:
            exit()
    pygame.display.update()