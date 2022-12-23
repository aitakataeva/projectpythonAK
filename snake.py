from __future__ import barry_as_FLUFL
import pygame
import sys
import random 


pygame.init()


SIZE_BLOCK = 20
FRAME_COLOR = (200, 255, 255)
WHITE = (100, 255, 100)
BLUE = (0, 255, 0)
RED = (224, 0, 0)
HEADER_COLOR = (200, 255, 255)
SNAKE_COLOR = (255, 255, 0)
COUNT_BLOCKS = 20
HEADER_MARGIN = 70
MARGIN = 1
size = [SIZE_BLOCK*COUNT_BLOCKS + 2*SIZE_BLOCK + MARGIN*COUNT_BLOCKS, 
        SIZE_BLOCK*COUNT_BLOCKS + 2*SIZE_BLOCK + MARGIN*COUNT_BLOCKS + HEADER_MARGIN]


screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 36)


"""function responsible for snake coordinates"""
class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #a function that the determines where the snake is located
    def is_inside(self):
        return 0<=self.x<COUNT_BLOCKS and 0<=self.y<COUNT_BLOCKS
    
    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y



def get_randon_empty_block():
    x = random.randint(0, COUNT_BLOCKS-1)
    y = random.randint(0, COUNT_BLOCKS-1)
    empty_block = SnakeBlock(x, y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, COUNT_BLOCKS-1)
        empty_block.y = random.randint(0, COUNT_BLOCKS-1)
    return empty_block


#function responsible for rendering the playing field
def draw_block(color, row, column):
    pygame.draw.rect(screen,color,[SIZE_BLOCK + column*SIZE_BLOCK + MARGIN*(column+1), 
                                       HEADER_MARGIN + SIZE_BLOCK + row*SIZE_BLOCK + MARGIN*(row+1),
                                       SIZE_BLOCK,SIZE_BLOCK])


snake_blocks = [SnakeBlock(9,8), SnakeBlock(9,9), SnakeBlock(9,10)]   #snake start coordinates
apple = get_randon_empty_block()
d_row = 0
buf_row = 0
d_col = 1
buf_col = 1
total = 0
speed = 1


def controle(event):
    buf_r = buf_row
    buf_c = buf_col
    """function to close the window"""
    if event.type == pygame.QUIT:
        print('exit')
        pygame.quit()
        sys.exit()
        #function responsible for the movement of the snake
    elif event.type == pygame.KEYDOWN:       
        
        if event.key == pygame.K_UP and d_col != 0:
            buf_r = -1
            buf_c = 0
        elif event.key == pygame.K_DOWN and d_col != 0:
            buf_r= 1
            buf_c = 0
        elif event.key == pygame.K_LEFT and d_row != 0:
            buf_r = 0
            buf_c = -1
        elif event.key == pygame.K_RIGHT and d_row != 0:
            buf_r = 0
            buf_c = 1
    return([buf_r,buf_c])



if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            lst = controle(event)
            buf_row = lst[0]
            buf_col = lst[1]
 
        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

        #text that will appear on the screen
        text_total = courier.render(f"Total: {total}", 0, WHITE)
        text_speed = courier.render(f"Speed: {speed}", 0, WHITE)
        #location method
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
        screen.blit(text_speed, (SIZE_BLOCK+250, SIZE_BLOCK))

        #function responsible for rendering the playing field
        for row in range(COUNT_BLOCKS):      
            for column in range(COUNT_BLOCKS):
                if (row + column)%2 == 0:
                    color = BLUE
                else:
                    color = WHITE

                draw_block(color, row, column)
    
        head = snake_blocks[-1]
        if not head.is_inside():     #the function responsible for the end of the 
                                 #game when the snake collides with the boundaries of the playing field
            print('crash')
            pygame.quit()
            sys.exit()

        draw_block(RED, apple.x, apple.y)
        for block in snake_blocks:
            draw_block(SNAKE_COLOR, block.x, block.y)

        """the method applies whatever you draw on the screen"""
        pygame.display.flip()

        #the function responsible for eating an apple by a snake
        if apple == head:
            total+=1
            speed = total//5 + 1
            snake_blocks.append(apple)
            apple = get_randon_empty_block()

        d_row = buf_row
        d_col = buf_col
        new_head = SnakeBlock(head.x + d_row, head.y + d_col)

        #function responsible for the end of the game when the snake collides with its body
        if new_head in snake_blocks:
            print('crash yourself')
            pygame.quit()
            sys.exit()

        snake_blocks.append(new_head)
        snake_blocks.pop(0)

        timer.tick(3+speed)

