import pygame



pygame.init()


#SETTING UP THE WINDOW AND IMAGE
win = pygame.display.set_mode((500, 500))
win.fill((255, 255, 255))
pygame.display.set_caption("Tic Tac Toe")
Image = pygame.image.load('/Users/anthonyvalle/Downloads/206-2066258_free-transparent-background-tumblr-theme-cool-tumblr-transparent.png.jpeg')


#SETTING UP ALL THE FONTS AND TEXTS
pygame.font.init()
Font = pygame.font.Font('/Users/anthonyvalle/Downloads/chicken_pie/CHICKEN Pie Height.ttf', 50)
Font2 = pygame.font.Font('/Users/anthonyvalle/Downloads/chicken_pie/CHICKEN Pie Height.ttf', 35)
X_Symbol = Font.render('X',False,(0,0,0))
O_Symbol = Font.render('O',False,(0,0,0))
Win_Text = Font.render('WINNER!!!',False,(0,0,0))
Tie_Text = Font.render('Tie',False,(0,0,0))
Clear_Text = Font2.render('Clear',False,(0,0,0))



#DRAWING THE SQUARES INWHICH THE Xs AND Os WILL BE DRAWN ON
first = pygame.draw.rect(win, (255,255,255), (100,100,100,100),1)
second = pygame.draw.rect(win, (255,255,255), (200,100,100,100),1)
third = pygame.draw.rect(win, (255,255,255), (300,100,100,100),1)
fourth = pygame.draw.rect(win, (255,255,255), (100,200,100,100),1)
fifth = pygame.draw.rect(win, (255,255,255), (200,200,100,100),1)
sixth = pygame.draw.rect(win, (255,255,255), (300,200,100,100),1)
seven = pygame.draw.rect(win, (255,255,255), (100,300,100,100),1)
eight = pygame.draw.rect(win, (255,255,255), (200,300,100,100),1)
nine = pygame.draw.rect(win, (255,255,255), (300,300,100,100),1)


#MAKING THE IMAGE THE BACKROUND
win.blit(Image,(-160,-40))


#MAKING THE CLEAR/RESTART BUTTON APPEAR ON THE SCREEN
Restart_Button_Border = pygame.draw.rect(win, (0,0,0), (95,445,310,55))
Restart_Button = pygame.draw.rect(win, (200,200,200), (100,450,300,50))
win.blit(Clear_Text,(200,450))


#DRAWING THE TICTACTOE LINES
pygame.draw.line(win, (0,0,0),(200,100),(200,400),(5))
pygame.draw.line(win, (0,0,0),(300,100),(300,400),(5))
pygame.draw.line(win, (0,0,0),(100,200),(400,200),(5))
pygame.draw.line(win, (0,0,0),(100,300),(400,300),(5))


#FUNCTIONS THAT HELP DRAW WINNING LINES
#THESE FUNCIONS ARE FOR PLAYER X
def cross1():
    return(board[1]=='X' and board[4]=='X' and board[7]=='X')
def cross2():
    return(board[2]=='X' and board[5]=='X' and board[8]=='X')
def cross3():
    return(board[3]=='X' and board[6]=='X' and board[9]=='X')
def cross4():
    return(board[1]=='X' and board[2]=='X' and board[3]=='X')
def cross5():
    return(board[4]=='X' and board[5]=='X' and board[6]=='X')
def cross6():
    return(board[7]=='X' and board[8]=='X' and board[9]=='X')
def diagonal1():
    return(board[1]=='X' and board[5]=='X' and board[9]=='X')
def diagonal2():
    return(board[3]=='X' and board[5]=='X' and board[7]=='X')


#SAME AS FUNCTION SHOWN ABOVE EXCEPT FOR PLAYER O
def cross1_O():
    return(board[1]=='Y' and board[4]=='Y' and board[7]=='Y')
def cross2_O():
    return(board[2]=='Y' and board[5]=='Y' and board[8]=='Y')
def cross3_O():
    return(board[3]=='Y' and board[6]=='Y' and board[9]=='Y')
def cross4_O():
    return(board[1]=='Y' and board[2]=='Y' and board[3]=='Y')
def cross5_O():
    return(board[4]=='Y' and board[5]=='Y' and board[6]=='Y')
def cross6_O():
    return(board[7]=='Y' and board[8]=='Y' and board[9]=='Y')
def diagonal1_O():
    return(board[1]=='Y' and board[5]=='Y' and board[9]=='Y')
def diagonal2_O():
    return(board[3]=='Y' and board[5]=='Y' and board[7]=='Y')



#THIS IS THE FUNCTION THAT DETERMINES WHETHER SOMEONE WON
def CheckIfWin():
        return((board[1]=='X' and board[2]=='X' and board[3]=='X')or
        (board[1]=='Y' and board[2]=='Y' and board[3]=='Y')or
        (board[4]=='X' and board[5]=='X' and board[6]=='X')or 
        (board[4]=='Y' and board[5]=='Y' and board[6]=='Y')or
        (board[7]=='X' and board[8]=='X' and board[9]=='X')or
        (board[7]=='Y' and board[8]=='Y' and board[9]=='Y')or
        (board[1]=='X' and board[4]=='X' and board[7]=='X')or
        (board[1]=='Y' and board[4]=='Y' and board[7]=='Y')or
        (board[2]=='X' and board[5]=='X' and board[8]=='X')or
        (board[2]=='Y' and board[5]=='Y' and board[8]=='Y')or
        (board[3]=='X' and board[6]=='X' and board[9]=='X')or
        (board[3]=='Y' and board[6]=='Y' and board[9]=='Y')or
        (board[1]=='X' and board[5]=='X' and board[9]=='X')or
        (board[1]=='Y' and board[5]=='Y' and board[9]=='Y')or
        (board[3]=='X' and board[5]=='X' and board[7]=='X')or
        (board[3]=='Y' and board[5]=='Y' and board[7]=='Y'))


#THIS IS THE 'BOARD' BEHIND THE ACTUAL PYGAME SCREEN, SIMILAR TO THE BACKEND OF A WEBSITE
#THIS WILL HELP US DETERMINE WHETHER SOMEONE WON, AND WHAT POSITIOS ARE ALREADY TAKEN
board = ['#','1','2','3','4','5','6','7','8','9']


#THIS IS THE FUNCTION THAT WILL HELP US DETERMINE IF THERE IS A TIE AS THERE IS ONLY ONE POSSIBLE WAY
#TO GET A TIE AND THATS AFTER THERE IS NO WINNERS IN 9 TOTAL MOVES
def CheckifTie():
	return(Tie==9)


#TIE IS SET TO 0 AND AFTER EACH TURN '1' WILL BE ADDED TO IT
Tie = 0


#THIS BOOLEAN WILL HELP US IN DETREMING WHAT POSITIONS ARE TAKEN AS EACH LETTER IS ASSIGNED TO ONE SQUARE
#AFTER EACH TURN ONE OF THESE LETTERS WILL BE FALSE THEREFORE IT NOT ABLE TO BE DRAWN ON AGAIN UNLESS BOARD IS CLEAREDD
a=b=c=d=e=f=g=h=i=True


#'TURN' DETERMINES WHOS TURN IT IS
#AS PLAYERS CYCLE, TURN SWITCHES FROM HAVING A VALUE OF '0' AND '1' TO MAKE SURE X OR O DOSENT GO TWICE
Turn = 0


#RUN IS TRUE THEREFORE PYGAME IS RUNNING
run = True
while run:


	#FOR LOOP TO CAPTURE EVENTS
    for event in pygame.event.get():


    	#IF STATEMENT TO CLOSE THE GAME
        if event.type == pygame.QUIT:
            run = False


        #IF STATEMENT THAT CAPTURES THE MOUSE GETTING CLICKED
        if event.type == pygame.MOUSEBUTTONDOWN:


        	#'pos' IS SET EQUAL TO THE POSITION INWHICH THE MOUSE WAS CLICKED TO SEE IF IT CLICKED OVER A TICTACTOE QUADRANT OR A BUTTON
        	pos = pygame.mouse.get_pos()


        	#IF STATEMENT THAT BASIICALLY STATES THAT IF THE 'Clear' BUTTON WAS PRESSED, THAN COMPLETE THESE ACTIONS:
        	if Restart_Button.collidepoint(pos):
        		
        		win.blit(Image,(-160,-40)) #PASTES THE IMAGE OVER WHAT's CURRENTLY ON THE SCREEN

        		pygame.draw.line(win, (0,0,0),(200,100),(200,400),(5)) #DRAWS THE TICTACTOE LINES OVER THE IMAGE
        		pygame.draw.line(win, (0,0,0),(300,100),(300,400),(5))
        		pygame.draw.line(win, (0,0,0),(100,200),(400,200),(5))
        		pygame.draw.line(win, (0,0,0),(100,300),(400,300),(5))

        		Restart_Button_Border = pygame.draw.rect(win, (0,0,0), (95,445,310,55)) #DRAW THE 'Clear' BUTTON'S BORDER OVER THE IMAGE

        		Restart_Button = pygame.draw.rect(win, (200,200,200), (100,450,300,50)) #DRAW THE ACTUAL 'Clear' BUTTON OVER THE IMAGE

        		win.blit(Clear_Text,(200,450)) #WRITES 'Clear' OVER THE CLEAR/RESTART BUTTON
        		
        		a=b=c=d=e=f=g=h=i=True #MAKES ALL POSTIONS UNTAKEN

        		Turn = 0 #RESETS WHOEVER'S TURN IT IS TO X's TURN

        		Tie = 0 #RESETS TIE VALUE AS GAME HAS RESTARTED
        		

        	#IF STATEMENT THAT BASIICALLY STATES THAT IF ONE OF THE TICTACTOE QUADRANTS ARE PRESSED, THAN COMPLETE THESE ACTIONS:
        	#THE QUADRANTS ARE SPECIFIED BY 'first' ALL THE WAY TO 'ninth'
        	if first.collidepoint(pos) and a:


        		#IF STATEMENT THAT DETECTS WHOSE TURN IT IS
        		#TURN '0' IS FOR X's PLAYER
        		if Turn == 0:

        			win.blit(X_Symbol,(133,113)) #PRINTS THE 'X' IN THE QUADRANT THAT WAS CLICKED

        			Turn = 1 # MAKE ITS THE OTHER PLAYER's TURN (O)

        			board[1] = 'X' #MARKS THE BACKEND BOARD WHICH HELPS IN DETECTING WHETHER SOMEONE WON

        			a = False #MAKES THE QUADRANT INWHICH THE LETTER IS LINKED TO, TAKEN. THEREFORE IT CAN'T BE CHOSEN AGAIN

        			Tie = Tie + 1 #ADDS '1' TO THE VALUE OF 'TIE'. THIS WILL DETECT WETHER THERE IS A TIE


        		#ELSE STATEMENT THAT COMPLETES THE SAME ACTIONS ABOVE EXCEPT FOR O's PLAYER
        		#THIS HAPPENS WHEN TURN IS SET TO '1'
        		else:

        			win.blit(O_Symbol,(133,113)) #PRINTS THE 'Y' IN THE QUADRANT THAT WAS CLICKED

        			Turn = 0 # MAKE ITS THE OTHER PLAYER's TURN (X)

        			board[1] = 'Y' #MARKS THE BACKEND BOARD WHICH HELPS IN DETECTING WHETHER SOMEONE WON

        			a = False #MAKES THE QUADRANT INWHICH THE LETTER IS LINKED TO, TAKEN. THEREFORE IT CAN'T BE CHOSEN AGAIN

        			Tie = Tie + 1 #ADDS '1' TO THE VALUE OF 'TIE'. THIS WILL DETECT WETHER THERE IS A TIE
        	


        	#SAME RULES APPLY AS WHAT WAS SAID ABOVE
        	if second.collidepoint(pos) and b:
        		if Turn == 0:
        			win.blit(X_Symbol,(233,113))
        			Turn = 1
        			board[2] = 'X'
        			b = False
        			Tie = Tie + 1
        		else:
        			win.blit(O_Symbol,(233,113))
        			Turn = 0
        			board[2] = 'Y'
        			b = False
        			Tie = Tie + 1

        	

        	#SAME RULES APPLY AS WHAT WAS SAID ABOVE
        	if third.collidepoint(pos) and c:
        		if Turn == 0:
        			win.blit(X_Symbol,(333,113))
        			Turn = 1
        			board[3] = 'X'
        			c = False
        			Tie = Tie + 1
        		else:
        			win.blit(O_Symbol,(333,113))
        			Turn = 0
        			board[3] = 'Y'
        			c = False
        			Tie = Tie + 1

        	

        	#SAME RULES APPLY AS WHAT WAS SAID ABOVE
        	if fourth.collidepoint(pos) and d:
        		if Turn == 0:
        			win.blit(X_Symbol,(133,213))
        			Turn = 1
        			board[4] = 'X'
        			d = False
        			Tie = Tie + 1
        		else:
        			win.blit(O_Symbol,(133,213))
        			Turn = 0
        			board[4] = 'Y'
        			d = False
        			Tie = Tie + 1

        	

        	#SAME RULES APPLY AS WHAT WAS SAID ABOVE
        	if fifth.collidepoint(pos) and e:
        		if Turn == 0:
        			win.blit(X_Symbol,(233,213))
        			Turn = 1
        			board[5] = 'X'
        			e = False
        			Tie = Tie + 1
        		else:
        			win.blit(O_Symbol,(233,213))
        			Turn = 0
        			board[5] = 'Y'
        			e = False
        			Tie = Tie + 1

        	

        	#SAME RULES APPLY AS WHAT WAS SAID ABOVE
        	if sixth.collidepoint(pos) and f:
        		if Turn == 0:
        			win.blit(X_Symbol,(333,213))
        			Turn = 1
        			board[6] = 'X'
        			f = False
        			Tie = Tie + 1
        		else:
        			win.blit(O_Symbol,(333,213))
        			Turn = 0
        			board[6] = 'Y'
        			f = False
        			Tie = Tie + 1



        	#SAME RULES APPLY AS WHAT WAS SAID ABOVE
        	if seven.collidepoint(pos) and g:
        		if Turn == 0:
        			win.blit(X_Symbol,(133,313))
        			Turn = 1
        			board[7] = 'X'
        			g = False
        			Tie = Tie + 1
        		else:
        			win.blit(O_Symbol,(133,313))
        			Turn = 0
        			board[7] = 'Y'
        			g = False
        			Tie = Tie + 1
        	


        	#SAME RULES APPLY AS WHAT WAS SAID ABOVE
        	if eight.collidepoint(pos) and h:
        		if Turn == 0:
        			win.blit(X_Symbol,(233,313))
        			Turn = 1
        			board[8] = 'X'
        			h = False
        			Tie = Tie + 1
        		else:
        			win.blit(O_Symbol,(233,313))
        			Turn = 0
        			board[8] = 'Y'
        			h = False
        			Tie = Tie + 1



        	#SAME RULES APPLY AS WHAT WAS SAID ABOVE
        	if nine.collidepoint(pos) and i:
        		if Turn == 0:
        			win.blit(X_Symbol,(333,313))
        			Turn = 1
        			board[9] = 'X'
        			i = False
        			Tie = Tie + 1
        		else:
        			win.blit(O_Symbol,(333,313))
        			Turn = 0
        			board[9] = 'Y'
        			i = False
        			Tie = Tie + 1


        #IF STATEMENTS THAT CHECK IF SOMEONE WON TO DISPLAY WINNING LINE
        if cross1() is True:
            pygame.draw.line(win, (0,0,0),(145,100),(145,400),(5))
        if cross2() is True:
            pygame.draw.line(win, (0,0,0),(245,100),(245,400),(5))
        if cross3() is True:
            pygame.draw.line(win, (0,0,0),(345,100),(345,400),(5))
        if cross4() is True:
            pygame.draw.line(win, (0,0,0),(100,150),(400,150),(5))
        if cross5() is True:
            pygame.draw.line(win, (0,0,0),(100,250),(400,250),(5))
        if cross6() is True:
            pygame.draw.line(win, (0,0,0),(100,350),(400,350),(5))
        if diagonal1() is True:
            pygame.draw.line(win, (0,0,0),(100,100),(400,400),(7))
        if diagonal2() is True:
            pygame.draw.line(win, (0,0,0),(400,100),(100,400),(7))
        if cross1_O() is True:
            pygame.draw.line(win, (0,0,0),(147,100),(147,400),(5))
        if cross2_O() is True:
            pygame.draw.line(win, (0,0,0),(247,100),(247,400),(5))
        if cross3_O() is True:
            pygame.draw.line(win, (0,0,0),(347,100),(347,400),(5))
        if cross4_O() is True:
            pygame.draw.line(win, (0,0,0),(100,147),(400,147),(5))
        if cross5_O() is True:
            pygame.draw.line(win, (0,0,0),(100,247),(400,247),(5))
        if cross6_O() is True:
            pygame.draw.line(win, (0,0,0),(100,347),(400,347),(5))
        if diagonal1_O() is True:
            pygame.draw.line(win, (0,0,0),(100,100),(400,400),(7))
        if diagonal2_O() is True:
            pygame.draw.line(win, (0,0,0),(400,100),(100,400),(7))




        	
        #CHECKS IF THE FUNCTION THAT DETRMINES WHETHER SOEMONE WON IS TRUE
        if CheckIfWin() is True:

        	win.blit(Win_Text,(150,25)) #PRINTS THAT THERE IS A WINNER

        	board = ['#','1','2','3','4','5','6','7','8','9'] #RESETS THE BACKEND BOARD 

        	Tie = 0 #RESETS TIE COUNTER

        	a=b=c=d=e=f=g=h=i=False #MAKES ALL POSITION CHOSEN AS GAME IS OVER




        #CHECKS IF THE FUNCTION THAT DETRMINES WHETHER THERE IS A TIE IS TRUE
        if CheckifTie() is True:

        	win.blit(Tie_Text,(210,25)) #PRINTS THAT THERES A TIE

        	board = ['#','1','2','3','4','5','6','7','8','9'] #RESETS THE BACKEND BOARD 

        	a=b=c=d=e=f=g=h=i=False  #MAKES ALL POSITION CHOSEN AS GAME IS OVER

    pygame.display.update()


 

pygame.quit

