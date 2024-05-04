
import pgzrun
import pygame as pg ,sys
from pygame.locals import *
import time


# khai báo các biến 
XO= 'x'
draw=False
winner=None
width=400
height=400
white=(255,255,255)
line_color=(10,10,10)

# tạo bảng 3x 3 tic tac toe

TTT=[None]*3,[None]*3,[None]*3

# khai báo màn hình 

pg.init()
fps=30
CLOCK= pg.time.Clock()
screen=pg.display.set_mode((width,height+100),0,32)
pg.display.set_caption(" game tic tac toe")

# tải hình ảnh

opeing= pg.image.load('tic tac opening.png')
x_img=pg.image.load('x.png')
o_img=pg.image.load('o.png')

# thay đổi kích thước hình 

opeing=pg.transform.scale(opeing,(width, height+100))
x_img=pg.transform.scale(x_img,(80,80))
o_img=pg.transform.scale(o_img,(80,80))

# set up game diễn ra
def game_opening():
    screen.blit(opeing,(0,0))
    pg.display.update()
    time.sleep(1)     # sau 1 giây mất hình ảnh  opening
    screen.fill(white)

    # chia làm 9 ô 
    # ve đường dọc
    pg.draw.line(screen,line_color,(width/3,0),(width/3,height),7)
    pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2,height),7)

    # ve đường NGANG
    pg.draw.line(screen,line_color,(0,height/3),(width,height/3),7)
    pg.draw.line(screen,line_color,(0,height/3*2),(width,height/3*2),7)
    draw_status()
# viết tình trạng , lượt ai chơi , ai thắng

def draw_status():
    global XO
    
    if winner is None:
        mesage=XO.upper() + "' s luot"
    else:
        mesage=winner.upper() + " chien thang"

    if draw:
        mesage= " alur vlog 2 ben hoa nhau"

    
    font= pg.font.Font(None,30)
    text=font.render(mesage,1,(255,255,255))

    # sao chép  di chuyển sang màn hình game
    screen.fill((0,0,0),(0 ,400,500,100))    # tô màn đen phía dưới màn hình thành hình chữ nhật 
    text_rect=text.get_rect(center=(width/2,500-50))   # chiều cao khung game là 500 , khu dưới cao 100 
    screen.blit(text,text_rect)
    pg.display.update()

# kiêm tra ai thắng 
def check_win():
    global TTT , winner , draw
    # kiem tra hang ngang
    for row in range(0,3):
        if ((TTT[row][0]==TTT[row][1]==TTT[row][2]) and (TTT[row][0]is not None)):
            winner=TTT[row][0]
            pg.draw.line(screen,(255,0,0),(0,(row+1)*height/3-height/6),\
                (width,(row+1)*height/3-height/6),4)
        

    # kiem  tra hang doc
    for col in range(0,3):
        if ((TTT[0][col]==TTT[1][col]==TTT[2][col])and (TTT[0][col] is not None)):
            winner=TTT[0][col]
            pg.draw.line(screen,(255,0,0),((col+1)*width/3-width/6,0),((col+1)*width/3-width/6,height),4)
        
    
# kiem tra hàng cheo
    if TTT[0][0]==TTT[1][1]==TTT[2][2] and TTT[0][0] is not None:
        winner=TTT[0][0]
        pg.draw.line(screen,(250,0,0),(50,50),(350,350),4)
    
# kiemtra hag cheo nguoc
    if TTT[0][2]==TTT[1][1]==TTT[2][0] and TTT[0][2] is not None:
        winner= TTT[0][2]
        pg.draw.line(screen,(255,0,0),(350,50),(50,350),4)       
    
#  sau 9 luot khong ai thang thi reset
    if all([all(row) for row in TTT]) and winner is None:
        draw=True

    draw_status()


# vẽ dấu x ,o
def drawXO(row,col):

    global TTT , XO
    if row==1:
        posx=30
    if row==2:
        posx=width/3 +30
    if row==3:
        posx=width/3*2 +30

    if col==1:
        posy=30
    if col==2:
        posy=height/3+30
    if col==3:
        posy=height/3*2 +30
    TTT[row-1][col-1]= XO 

    if (XO=='x'):
        screen.blit(x_img,(posy,posx))
        XO='o'
    elif (XO=='o'):
        screen.blit(o_img,(posy,posx))
        XO='x'
    pg.display.update()


# khai báo khi click chuột
def click_mouse():
    
    # lấy toạ độ x , khi click chuột
    x,y = pg.mouse.get_pos()
    # xác định số ô cột khi click chuột
    if (x<width/3):
        col=1
    elif (x<width/3*2):
        col=2
    elif(x<width):
        col=3
    else:
        col= None

    # xác định số hàng cột khi click chuột
    if (y< height/3):
        row =1 
    elif (y<height/3*2):
        row=2
    elif (y<height):
        row= 3
    else:
        row= None
    
    if (row and col and  TTT[row-1][col-1] is None):
        global XO
        drawXO(row,col)
        check_win()


# khai baso reset game để chơi lại 
def reset_game():
    global TTT , winner , XO, draw
    time.sleep(5)
    XO='x'
    draw= False
    winner=None
    game_opening()
    TTT=[[None]*3,[None]*3,[None]*3]


game_opening()
# để tắt màn hình cần vòng lặp while

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

pgzrun.go()
