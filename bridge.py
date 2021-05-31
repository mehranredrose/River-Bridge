#AD Project 1 by Mehran RedRose


import pygame
from pygame.locals import *
from sys import exit

import math

pygame.init()
screen = pygame.display.set_mode((640,480))
font = pygame.font.Font("Montserrat-Regular.ttf", 25)


def degreesToRadians(deg):#turns degree to radians for creating circles
    return deg/180.0 * math.pi


def drawCircleArc(screen,color,center,radius,startDeg,endDeg,thickness):#create circle with favorite color and location and thickness
    (x,y) = center
    rect = (x-radius,y-radius,radius*2,radius*2)
    startRad = degreesToRadians(startDeg)
    endRad = degreesToRadians(endDeg)
   
    pygame.draw.arc(screen,color,rect,startRad,endRad,thickness)
    



def truedigit(): #gets only digits not strings
    number = input("\n\n\nEnter ur numbers one by one (only one digit and between 1 - 5) : ")
    while not number.isdigit():
        print ('\n Ur input is not a Number ! Please Try again !\n')
        number = input("Enter a number: ")
    number=int(number)
    return number

def cities():   #get number of random citties by user but not repeated or out of range
    numbers = []        
    while len(numbers)<5:
        number = truedigit()
        reset=False
        if not 1 <= number <= 5:
            print('\n Only numbers between 1 and 5 are accepted, try again\n')
        else:
            if  numbers != []: 
                for x in numbers:
                    if number == x:
                        print('\n u Enter This number before , Please Don\'t Enter repeated Number !\n')
                        reset=True
            if reset==True:
                continue
            else:
                numbers.append(number)
    return numbers
            
a=cities()
n1=str(a[0])
n2=str(a[1])
n3=str(a[2])
n4=str(a[3])
n5=str(a[4])

def findcitties(h):#find citties that are chosen ones :))))
    t=0
    c=[]
    d=[]
    for i in range(0,4):
        if(a[i]==5):
            continue
        for j in range (i+1,5):
            b = []
            b.append(a[i])
            count=1
            first=i
            second=j

            while second!=5:
                if a[first]<a[second]:
                    if b[-1]<a[second]:
                        b.append(a[second])
                        count+=1
                first=second
                second+=1

            if t==count:
                d.append(b)
            if t<count: 
                t=count         
                c.append(b)
           
    if c!= []:    
        print(c[-1])
        finalcitties=c[-1]
        if d!=[]:
            if t==len(d[-1]):
                print('other ways are : ',d[-1])
    else:
        print('only one of citties can attach and that can be any of citties I prefer 5')
        finalcitties=[5]
    return finalcitties

linescitties=findcitties(a)
#returns x of circle in row 1
def row1(k):
    switcher={
                1:'75',
                2:'200',
                3:'325',
                4:'450',
                5:'575'
             }
    return switcher.get(k)
#returns x of circle in row 2
def row2(k):
    switcher={
                0:'75',
                1:'200',
                2:'325',
                3:'450',
                4:'575'
             }
    return switcher.get(k)
#values of color in rgb
white = (255,255,255);
red = (255,0,0);
green = (0,255,0);
blue = (0,0,255);
darkBlue = (0,0,128);
black = (0,0,0);
pink = (255,200,200);

#the main() function :))))
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(white);#turn the screen to white


     #writing the numbers in circles row 1
    one = font.render('1', True, black, white)
    textRect1 = one.get_rect()
    textRect1.center = (75,50)
    screen.blit(one, textRect1)

    two = font.render('2', True, black, white)
    textRect2 = two.get_rect()
    textRect2.center = (200,50)
    screen.blit(two, textRect2)

    three = font.render('3', True, black, white)
    textRect3 = three.get_rect()
    textRect3.center = (325,50)
    screen.blit(three, textRect3)

    four = font.render('4', True, black, white)
    textRect4 = four.get_rect()
    textRect4.center = (450,50)
    screen.blit(four, textRect4)

    five = font.render('5', True, black, white)
    textRect5 = five.get_rect()
    textRect5.center = (575,50)
    screen.blit(five, textRect5)
    
    #input citties  number  in circles row 2
    one = font.render(n1, True, black, white)
    textRect1 = one.get_rect()
    textRect1.center = (75,250)
    screen.blit(one, textRect1)

    two = font.render(n2, True, black, white)
    textRect2 = two.get_rect()
    textRect2.center = (200,250)
    screen.blit(two, textRect2)

    three = font.render(n3, True, black, white)
    textRect3 = three.get_rect()
    textRect3.center = (325,250)
    screen.blit(three, textRect3)

    four = font.render(n4, True, black, white)
    textRect4 = four.get_rect()
    textRect4.center = (450,250)
    screen.blit(four, textRect4)

    five = font.render(n5, True, black, white)
    textRect5 = five.get_rect()
    textRect5.center = (575,250)
    screen.blit(five, textRect5)

    #creating the circles in row 1
    drawCircleArc(screen,green,(75,50),50,0,360,3)
    drawCircleArc(screen,red,(200,50),50,0,360,3)
    drawCircleArc(screen,blue,(325,50),50,0,360,3)
    drawCircleArc(screen,black,(450,50),50,0,360,3)
    drawCircleArc(screen,pink,(575,50),50,0,360,3)

    #creating the circles in row 2
    drawCircleArc(screen,green,(75,250),50,0,360,3)
    drawCircleArc(screen,red,(200,250),50,0,360,3)
    drawCircleArc(screen,blue,(325,250),50,0,360,3)
    drawCircleArc(screen,black,(450,250),50,0,360,3)
    drawCircleArc(screen,pink,(575,250),50,0,360,3)


    #creating the river
    pygame.draw.line(screen,blue, (0, 125), (640, 125),10)
    pygame.draw.line(screen,blue, (0, 175), (640, 175),10)

    for i in range(0,5): # creating the bridges
        for j in linescitties:
            if a[i]==j:
                pygame.draw.line(screen,black, (int(row1(j)),100), (int(row2(i)),200),8)

    pygame.display.flip()
    

    pygame.display.update()
