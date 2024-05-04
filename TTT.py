import pgzrun
import pygame as pg ,sys
from pygame.locals import *
import time
import random

#khai báo biến
XO= 'x'
draw=False
winner=None
width=400
height=400
white=(255,255,255)
line_color=(10,10,10)

#tạo bảng 3x3 TTT
TTT = ([None]*3,[None]*3,[None]*3)

#khai báo màn hình
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen=pg.display.set_mode((width,height+100),0,32)
pg.display.set_caption(" Game Tic-tac-toe")

#tải hình ảnh
opening= pg.image.load('tic tac opening.png')
x_img=pg.image.load('x.png')
o_img=pg.image.load('o.png')

#thay đổi kích thước hình
opening=pg.transform.scale(opening,(width, height+100))
x_img=pg.transform.scale(x_img,(80,80))
o_img=pg.transform.scale(o_img,(80,80))

#set up game
def game_opening():
    screen.blit(opening,(0,0))
    pg.display.update()
    time.sleep(2)     # sau 1 giây mất hình ảnh  opening
    screen.fill(white)
    # chia làm 9 ô 
    # ve đường dọc
    pg.draw.line(screen,line_color,(width/3,0),(width/3,height),7)
    pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2,height),7)
    
    

    # ve đường NGANG
    pg.draw.line(screen,line_color,(0,height/3),(width,height/3),7)
    pg.draw.line(screen,line_color,(0,height/3*2),(width,height/3*2),7)
    draw_status()

#viết tình trạng
def draw_status():
    global XO
    
    if winner is None:
        mesage=XO.upper() + "' s luot"
    else:
        mesage=winner.upper() + " chien thang"

    if draw == True:
        mesage= " 2 ben hoa nhau"

    
    font= pg.font.Font(None,30)
    text=font.render(mesage,1,(255,255,255))

    # sao chép  di chuyển sang màn hình game
    screen.fill((0,0,0),(0 ,400,404,100))    # tô màn đen phía dưới màn hình thành hình chữ nhật 
    text_rect=text.get_rect(center=(width/2,450))   # chiều cao khung game là 500 , khu dưới cao 100 
    screen.blit(text,text_rect)
    pg.display.update()

#kiểm tra ai thắng
def check_win():
    global TTT , winner , draw
    # kiểm tra hàng ngang
    for row in range(0,3):
        if ((TTT[row][0]==TTT[row][1]==TTT[row][2]) and (TTT[row][0]is not None)):
            winner=TTT[row][0]
            pg.draw.line(screen,(255,0,0),(0,(row+1)*height/3-height/6),(width,(row+1)*height/3-height/6),4)
        

    # kiểm  tra hàng dọc
    for col in range(0,3):
        if ((TTT[0][col]==TTT[1][col]==TTT[2][col])and (TTT[0][col] is not None)):
            winner=TTT[0][col]
            pg.draw.line(screen,(255,0,0),((col+1)*width/3-width/6,0),((col+1)*width/3-width/6,height),4)
        
    
    # kiểm tra hàng chéo
    if TTT[0][0]==TTT[1][1]==TTT[2][2] and TTT[0][0] is not None:
        winner=TTT[0][0]
        pg.draw.line(screen,(250,0,0),(50,50),(350,350),4)
        
    
    # kiểm tra hàng chéo ngược
    if TTT[0][2]==TTT[1][1]==TTT[2][0] and TTT[0][2] is not None:
        winner= TTT[0][2]
        pg.draw.line(screen,(255,0,0),(350,50),(50,350),4)  
    
    #  sau 9 lượt không ai thắng thì reset
    if all([all(row) for row in TTT]) and winner is None:
        draw=True
    draw_status()
    if winner =='x' or winner=='o' or draw==True:
        return 1
        reset_game()
    else: return 0

#vẽ X
def drawX(row,col):
    global TTT, XO
    #xét hàng
    if row==1:
        posa=30
    if row==2:
        posa=width/3 +30
    if row==3:
        posa=width/3*2 +30
    #xét cột
    if col==1:
        posb=30
    if col==2:
        posb=height/3+30
    if col==3:
        posb=height/3*2 +30
    screen.blit(x_img,(posb,posa))
    XO='x'
    TTT[row-1][col-1] = 'x'
    pg.display.update()
    posb=None
    posa=None
    
# nước đi tốt nhất cho O
def best_move():
    global TTT

    #ưu tiên đánh vào ô TTT[1][1]    
    if(TTT[1][1] is None):
        drawO(2,2)
        a=3
    else: a=0

    #kiểm tra hàng ngang cho o
    if(a==0):
        for row in range(0,3,1):
            if(TTT[row][0]==TTT[row][1] and TTT[row][2]is None and TTT[row][0]=='o'):
                drawO(row+1,3)
                a=2
                break
            elif(TTT[row][0]==TTT[row][2] and TTT[row][1]is None and TTT[row][0]=='o'):
                drawO(row+1,2)
                a=2
                break
            elif(TTT[row][1]==TTT[row][2] and TTT[row][0]is None and TTT[row][1]=='o'):
                drawO(row+1,1)
                a=2
                break
            else: a=0
            
    #kiểm tra hàng dọc cho o
    if(a==0):
        for col in range(0,3,1):
            if(TTT[0][col]==TTT[1][col] and TTT[2][col]is None and TTT[0][col]=='o'):
                drawO(3,col+1)
                a=2
                break
            elif(TTT[0][col]==TTT[2][col] and TTT[1][col]is None and TTT[0][col]=='o'):
                drawO(2,col+1)
                a=2
                break
            elif(TTT[1][col]==TTT[2][col] and TTT[0][col]is None and TTT[1][col]=='o'):
                drawO(1,col+1)
                a=2
                break
            else: a=0

    #kiểm tra hàng chéo cho o
    if(a==0):
        if(TTT[0][0]==TTT[1][1] and TTT[2][2]is None and TTT[0][0]=='o'):
            drawO(3,3)
            a=2
        elif(TTT[0][0]==TTT[2][2] and TTT[1][1]is None and TTT[0][0]=='o'):
            drawO(2,2)
            a=2
        elif(TTT[1][1]==TTT[2][2] and TTT[0][0]is None and TTT[1][1]=='o'):
            drawO(1,1)
            a=2
        else: a=0
    
    #kiểm tra hàng chéo ngược cho o
    if(a==0):
        if(TTT[0][2]==TTT[1][1] and TTT[2][0]is None and TTT[1][1]=='o'):
            drawO(3,1)
            a=2
        elif(TTT[0][2]==TTT[2][0] and TTT[1][1]is None and TTT[0][2]=='o'):
            drawO(2,2)
            a=2
        elif(TTT[1][1]==TTT[2][0] and TTT[0][2]is None and TTT[1][1]=='o'):
            drawO(1,3)
            a=2
        else: a=0



    #kiểm tra hàng ngang cho x
    if(a==0):
        for row in range(0,3,1):
            if(TTT[row][0]==TTT[row][1] and TTT[row][2]is None and TTT[row][0]=='x'):
                drawO(row+1,3)
                a=1
                break
            elif(TTT[row][0]==TTT[row][2] and TTT[row][1]is None and TTT[row][0]=='x'):
                drawO(row+1,2)
                a=1
                break
            elif(TTT[row][1]==TTT[row][2] and TTT[row][0]is None and TTT[row][1]=='x'):
                drawO(row+1,1)
                a=1
                break
            else: a=0
                
    #kiểm tra hàng dọc cho x
    if(a==0):
        for col in range(0,3,1):
            if(TTT[0][col]==TTT[1][col] and TTT[2][col]is None and TTT[0][col]=='x'):
                drawO(3,col+1)
                a=1
                break
            elif(TTT[0][col]==TTT[2][col] and TTT[1][col]is None and TTT[0][col]=='x'):
                drawO(2,col+1)
                a=1
                break
            elif(TTT[1][col]==TTT[2][col] and TTT[0][col]is None and TTT[1][col]=='x'):
                drawO(1,col+1)
                a=1
                break
            else: a=0

    #kiểm tra hàng chéo cho x
    if(a==0):
        if(TTT[0][0]==TTT[1][1] and TTT[2][2]is None and TTT[0][0]=='x'):
            drawO(3,3)
            a=1
        elif(TTT[0][0]==TTT[2][2] and TTT[1][1]is None and TTT[0][0]=='x'):
            drawO(2,2)
            a=1
        elif(TTT[1][1]==TTT[2][2] and TTT[0][0]is None and TTT[1][1]=='x'):
            drawO(1,1)
            a=1
        else: a=0
        
    #kiểm tra hàng chéo ngược cho x
    if(a==0):
        if(TTT[0][2]==TTT[1][1] and TTT[2][0]is None and TTT[1][1]=='x'):
            drawO(3,1)
            a=1
        elif(TTT[0][2]==TTT[2][0] and TTT[1][1]is None and TTT[0][2]=='x'):
            drawO(2,2)
            a=1
        elif(TTT[1][1]==TTT[2][0] and TTT[0][2]is None and TTT[1][1]=='x'):
            drawO(1,3)
            a=1
        else: a=0

    #random
    if(a==0):
        randomO()

#random O
def randomO():
    global TTT
    row = random.randint(1,3)
    col = random.randint(1,3)
    while TTT[row-1][col-1] is not None:
        row = random.randint(1,3)
        col = random.randint(1,3)
    drawO(row,col)

#vẽ O
def drawO(row,col):
    global TTT
    #xét hàng
    if row==1:
        posc=30
    if row==2:
        posc=width/3 +30
    if row==3:
        posc=width/3*2 +30
    #xét cột
    if col==1:
        posd=30
    if col==2:
        posd=height/3+30
    if col==3:
        posd=height/3*2 +30
    screen.blit(o_img,(posd,posc))
    XO='o'
    TTT[row-1][col-1] = 'o'
    pg.display.update()
    posd=None
    posc=None

#Khai báo khi click chuột
def click_mouse():
    # lấy toạ độ x , khi click chuột
    a,b = pg.mouse.get_pos()
    # xác định số cột khi click chuột
    if (a<width/3):
        col=1
    elif (a<width/3*2):
        col=2
    elif(a<width):
        col=3
    else:
        col= None

    # xác định số hàng khi click chuột
    if (b<height/3):
        row =1 
    elif (b<height/3*2):
        row=2
    elif (b<height):
        row=3
    else:
        row=None
    
    if (row and col and  TTT[row-1][col-1] is None):
        global XO
        drawX(row,col)
        if check_win()==0:
            best_move()
        check_win()

#reset game
def reset_game():
    global TTT , winner , XO, draw
    time.sleep(3)
    XO='x'
    draw= False
    winner=None
    game_opening()
    TTT=[[None]*3,[None]*3,[None]*3]

game_opening()

#tắt màn hình
while (True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type==MOUSEBUTTONDOWN:
            click_mouse()
            if (winner or draw):
                reset_game()     
    pg.display.update()
    CLOCK.tick(fps)

pg.quit()
sys.exit()
