import pygame
import random

#init pygame
pygame.init()

#open windows 
root = pygame.display.set_mode((800, 600))

#set caption, icon, ...
pygame.display.set_caption('snake')
# icon = pygame.image.load(r'C:\Users\hoang\Desktop\hello\imgs\snake.png')
# pygame.display.set_icon(icon)

#various variable
full_white = (255, 255, 255)
full_black = (0, 0, 0)
full_red = (255, 0, 0)
player_x = 300
player_y = 300
motion_x = 0
motion_y = 0
text_x = 10
text_y = 10
score = 0
font = pygame.font.Font('freesansbold.ttf', 32) 
food_x = round(random.randrange(0, 800 - 10) / 10.0) * 10.0
food_y = round(random.randrange(0, 600 - 10) / 10.0) * 10.0
clock = pygame.time.Clock()

#func 
def Score(score):
    score_font = font.render("Score:" + str(score), True, full_black)
    root.blit(score_font, (10, 10))


#thân chương trình
running = True
while running:
    #thiết lập màn hình
    root.fill(full_white)
    
    
    if (player_x == food_x) and (player_y == food_y):
            score += 1       
            food_x = round(random.randrange(0, 800 - 10) / 10.0) * 10.0
            food_y = round(random.randrange(0, 600 - 10) / 10.0) * 10.0


    #bắt sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (player_x >= 800 ) or (player_x < 0) or (player_y <= 0) or (player_y >= 600):
            running = False
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_w):
                motion_x = 0
                motion_y = -10        
            elif( event.key == pygame.K_s):
                motion_x = 0
                motion_y = 10        
            elif (event.key == pygame.K_a):
                motion_x = -10
                motion_y = 0        
            elif (event.key == pygame.K_d):
                motion_x = 10
                motion_y = 0
        
    
    Score(score)
    player_x += motion_x
    player_y += motion_y
    
    pygame.draw.rect(root,full_red,[food_x, food_y, 10, 10])
    pygame.draw.rect(root,full_black,[player_x, player_y, 10, 10])

    pygame.display.update()
    
    clock.tick(10)


 
pygame.quit()
quit()
