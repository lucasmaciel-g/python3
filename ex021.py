import pygame
pygame.mixer.init()
a = input('Digite seu nome: ')
pygame.mixer.music.load('calma.mp3')
print('Aproveite a musica de hoje, {}! :)'.format(a))
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): #aqui estou falando para ele ficar sem encerrar o programa enquanto a musica tiver sendo tocada#
    pygame.time.Clock().tick(10) #nessa linha o clock serve para inserir um funcao de verificar a cada 10 milissegundos se o while continua#

#pygame.event.wait() -- outra forma de deixar o programa rodando até finalizar a musica#