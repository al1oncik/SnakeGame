import pygame
from object import Snake,Apple

class Game:
    pygame.init()
    def __init__(self):
        self.win_width = 800
        self.win_height = 600
        self.win = pygame.display.set_mode((
                    self.win_width,
                    self.win_height
        ))
        pygame.display.set_caption("Snake game")

        self.game_over = False

        self.snake = Snake()
        self.apple = Apple()
        
        self.apple.randpos()

        self.clock = pygame.time.Clock()

    
    def render(self,text,size,color,pos):
        font = pygame.font.SysFont("comicsansms",size)
        message = font.render(text,True,color)
        self.win.blit(message,[pos[0],pos[1]])

    
    def draw(self):
        self.win.fill((0,0,0))# set background color
        
        # draw the snake
        for tail in self.snake.tails:
            pygame.draw.rect(
                            self.win,
                            (0,255,0),# green color
                            (
                                tail[0],# x
                                tail[1],# y
                                self.snake.size,
                                self.snake.size
                            ))
        # draw the apple
        pygame.draw.rect(
                            self.win,
                            (255,0,0),
                            (
                                self.apple.x,
                                self.apple.y,
                                self.apple.size,
                                self.apple.size
                            )
        )

        if self.game_over:
            self.render("GAME OVER",80,(255,0,0),[250,100])
            self.render("Press r to replay. Press q to quit",30,(255,0,0),[265,160])
        
        self.render(f"Score: {self.snake.lenght}",50,(255,255,255),[0,0])
        pygame.display.update()
        self.clock.tick(15)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                
            if self.game_over:
                self.snake.change_x = 0
                self.snake.change_y = 0
                if pygame.key.get_pressed()[pygame.K_r]:
                    self.game_over = False
                    self.snake.lenght = 1
                    self.snake.x = 400 
                    self.snake.y = 300
                    self.snake.tails = [self.snake.head]
                if pygame.key.get_pressed()[pygame.K_q]:
                    exit()
                
            if not self.game_over:
                # keyboard events
                if pygame.key.get_pressed()[pygame.K_w] and self.snake.change_y <= 0:
                    self.snake.change_y = -self.snake.size
                    self.snake.change_x = 0

                if pygame.key.get_pressed()[pygame.K_s] and self.snake.change_y >= 0:
                    self.snake.change_y = self.snake.size
                    self.snake.change_x = 0

                if pygame.key.get_pressed()[pygame.K_a] and self.snake.change_x <= 0:
                    self.snake.change_x = -self.snake.size
                    self.snake.change_y = 0

                if pygame.key.get_pressed()[pygame.K_d] and self.snake.change_x >= 0:
                    self.snake.change_x = self.snake.size
                    self.snake.change_y = 0

                #moving snake
                self.snake.x += self.snake.change_x
                self.snake.y += self.snake.change_y

                self.snake.head = []
                self.snake.head.append(self.snake.x)
                self.snake.head.append(self.snake.y)
                self.snake.tails.append(self.snake.head)

                # moving snake tail
                if len(self.snake.tails) > self.snake.lenght:
                    del self.snake.tails[0]
            
            #teleportation walls
            if self.snake.x < 0:
                self.snake.x += self.win_width
            
            if self.snake.x > self.win_width:
                self.snake.x -= self.win_width
            
            if self.snake.y < 0:
                self.snake.y += self.win_height
           
            if self.snake.y > self.win_height:
                self.snake.y -= self.win_height

            # check if snake eat the apple
            if self.snake.x == self.apple.x and self.snake.y == self.apple.y:
                self.apple.randpos()
                self.snake.lenght += 1
            
            # check if snake head touch the tail
            for i in self.snake.tails[:-1]:
                if i == self.snake.head:
                    self.game_over = True
                    
            self.draw()


game = Game()
game.run()
