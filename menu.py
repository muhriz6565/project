import pygame,time,pickle,io
import urllib.request
pygame.init()
class Anime:
    def __init__(self,title,showlink,cover,release_time):
        #self.showid=showid
        self.title=title
        self.showlink=showlink
        self.cover=cover
        self.release_time=release_time
        #self.res=input("Enter desired resolution: ")
display_width = 1000
display_height = 700
 
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bred=(255,0,0)
green=(0,200,0)
bgreen=(0,255,0)
 
block_color = (53,115,255)
 
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Main menu')
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def test(obj):
    print("SPAAAAAAASDASDASd")
    print(obj.title)

def main_menu():

    intro = True

    while intro:
        for event in pygame.event.get():
            
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Main Menu", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        button("Current Season",150,350,200,50,green,bgreen,this_season)
        button("Saved",500,350,100,50,green,bgreen,saved)
        button("Quit",47,554,100,50,red,bred,pygame.quit)
        pygame.display.update()
        clock.tick(15)

def this_season():
    while True:
        for event in pygame.event.get():    
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill((255,100,20))
        largeText=pygame.font.Font('freesansbold.ttf',80)
        TextSurf,TextRect=text_objects("Current Releases",largeText)
        TextRect.center=((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)
        with open("anime.pickle","rb") as f:
            anime=pickle.load(f)
            cx=1
            cy=1
            num_rows=(len(anime)//5)+1
            for i in range(0,len(anime)):
                #button(anime[i].title,cx*(display_width/8)-100,cy*(display_height/num_rows)-50,50,70,green,bgreen,test)
######################def button(msg,x,y,w,h,ic,ac,action=None):#################################################################################################
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if (cx*(display_width/8)-100)+50 > mouse[0] > (cx*(display_width/8)-100) and (cy*(display_height/num_rows)-50)+70 > mouse[1] > (cy*(display_height/num_rows)-50):
                    pygame.draw.rect(gameDisplay, bgreen,((cx*(display_width/8)-100),(cy*(display_height/num_rows)-50),50,70))
                    if click[0] == 1:
                        test(anime[i])
                else:
                    pygame.draw.rect(gameDisplay, green,((cx*(display_width/8)-100),(cy*(display_height/num_rows)-50),50,70))

                smallText = pygame.font.Font("freesansbold.ttf",10)
                textSurf, textRect = text_objects(anime[i].title, smallText)
                textRect.center = ( ((cx*(display_width/8)-100)+(50/2)), ((cy*(display_height/num_rows)-50)+(70/2)))
                gameDisplay.blit(textSurf, textRect)


###################################################################################################################
    
##                try:
##                    req=urllib.request.Request(url=anime[i].cover,
##                               headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
##                    image_file = io.BytesIO(urllib.request.urlopen(req).read())
##                    image = pygame.image.load(image_file)
##                    gameDisplay.blit(image, (cx*(display_width/8)-100,cy*(display_height/num_rows)-50))
##                except:
##                    print("fail")

                if cx==8:
                    cx=1
                    cy+=1.5
                else:
                    cx+=1
                ####numbe of rows is (i//5)+1

        button("Back",150,450,100,50,green,bgreen,main_menu)
        pygame.display.update()
        clock.tick(100)

def saved():
    while True:
        for event in pygame.event.get():    
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill((255,20,200))
        largeText=pygame.font.Font('freesansbold.ttf',80)
        TextSurf,TextRect=text_objects("Saved",largeText)
        TextRect.center=((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)

        button("Back",150,450,100,50,green,bgreen,main_menu)
        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action!=None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",10)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
main_menu()
