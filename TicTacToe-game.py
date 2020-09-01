import time   #only to create a slowdown so that things don't happen way too fast
rules="1. The game is played on a grid that's 3 squares by 3 squares.\n\n2. You are X, your friend is O. Players take turns putting their marks in empty squares.\n\n3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.\n\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie."
def storedisrec(decide,scores=""):
    with open('leadrboard.txt','a+') as fo:
        if decide==0:
          for k in scores:
             fo.write(str(k)+'#&#&#')
        else:
            L=[]
            fo.seek(0)
            ola=fo.read()
            if len(ola)!=0:
               for ko in ola.split('#&#&#'):
                  L.append(ko)
               return L
            else:
               return L

def deletleader():
    f=open('leadrboard.txt','w')
    f.write('')
    f.close()               

def dell(ender):  #empties the list ender
    while(len(ender)!=0):
        ender.pop(0)

def tableview(listta): #DISPLAYS THE LEADERBOARD
     q=len(listta)+1
     if(len(listta)!=0):
        print("LEADERBOARD:                \n  \n\n＼(▽￣＼(￣▽￣)／￣▽)／")
        print()
        print()
        print(" ___________________________________")
        print("|_ROUND.NO_|_________NAME___________|     ")


        cop="NO ONE(TIE)"                       
        pl=1
        for i in range(len(listta)):
            if(listta[i]!='0' and listta[i]!=''):
                    print("|  ",pl,"     |",listta[i]," "*(21-len(listta[i])),"|")
            
            elif(listta[i]=='0' and listta[i]!=''):
                
                    print("|  ",pl,"     |",cop," "*(21-len(cop)),"|")
            pl+=1
    
        print("|||||||||||||||||||||||||||||||||||||")
        print("-------------------------------------")    
        print()
        print()
        print() 


     else:
       print("_"*101)
       print()
       print()
       print("              ","NO GAMES HAVE BEEN PLAYED YET   ⊙ ▂ ⊙      |PLAY SOME ROUNDS AND THEN CHECK ^_^")
       print()
       print()
       print("_"*101)
   

def post(pos):   #shows the available position
    a=0   
    print("-"*100)
    print()
    print()
    op="_"*29 
    k=0
    li=0
    for HEK in range(1,5):
          if HEK!=1:
                print("                     ","|_________|_________|_________|")
          else:

              print("                      ",op)
          if(k%2==0 and k!=6):
               print("                     ","|  ",pos[li][1],"    |   ",pos[li+1][1],"   |   ",pos[li+2][1],"   |")
          else:
                print()
          k+=2
          li+=3
              
    print("-"*100)
    print()
    print()
    print()

    
#shows the location in numeric form
def loca(pos):
    print("_"*100)
    print()
    print("LOCATIONS:")
    op="_"*29 
    k=0
    li=0
    for HEL in range(1,5):
          if(li!=9):
              
            if pos[li][0]==0:
                 henna1='N'
            else:
                 henna1=pos[li][0]
            if(pos[li+1][0]==0):
                    henna2='N'
            else:
                   henna2=pos[li+1][0]
            if pos[li+2][0]==0:
                   henna3='N'
            else:
                  henna3=pos[li+2][0]
          else:
              pass

          if HEL!=1:
                print("                     ","|_________|_________|_________|")
          else:

              print("                      ",op)
          if(k%2==0 and k!=6):
                  print("                     ","|  ",henna1,"    |   ",henna2,"   |   ",henna3,"   |")
          else:
                print()
          k+=2
          li+=3
              
        
    print("_"*100) 
    print()
    print()
    print()


    
    
""" this marks the position"""
def turn(mark,loca,pos):
    a=0
    
    for i in pos:
                    
            if(str(i[0])==loca):
                           
                   pos[a][1]=mark
                   pos[a][0]=0
                           
                   break
            a+=1

def check(ender,pos): #checks if a combination has been made or not
    while(2<3):
      a=0
      if(pos[0][1]==pos[4][1] and pos[0][1]!='*'):
          if(pos[0][1]==pos[8][1]):
              dell(ender)
              a=8
    
              break
      if(pos[2][1]==pos[4][1] and pos[2][1]!="*"):
          if(pos[2][1]==pos[6][1]):
              dell(ender)
              
              a=8
              
              break
      lp=0
      while(a<7):
           b=a+1
           c=a+2
           d=lp
           e=d+3
           f=e+3
           if(pos[a][1]==pos[b][1] and pos[a][1]!="*"):
               if(pos[a][1]==pos[c][1]):
                   
                   dell(ender)
                
        
                   
                   break
           elif(pos[d][1]==pos[e][1] and pos[d][1]!="*"):
               if(pos[d][1]==pos[f][1]):
                   dell(ender)

                   break
           else:
               pass
           a+=3
           lp+=1

      break
     
def gamestart(score):
      x='n'
      pos=[['1','*'],['2','*'],['3','*'],['4',"*"],['5','*'],['6','*'],['7','*'],['8','*'],['9','*']]
      nop=['1','2','3','4','5','6','7','8','9','10']
      loca(pos)
      hey=[]
      ender=["checker","nothing imp"]
      count=0
      kok=1
      print("+"*100)
      print()
      print("PLAYER 1:")
      print()
      while(kok>0):
           t=input("NAME:")
           t=t.upper()
           if t=="":
              print()
              print("NAME CANNOT BE EMPTY")
              print()
              print()
           else:
               MOe=len(t)
               kok=0
               nam1=t.strip()
               if(len(t)>21):
                     nam1=t[:-(MOe-21)]
      print() 
      print()
      print("+"*100) 
      kak=1
      print()
      print()
      time.sleep(0.50)
      print("-"*100)
      print()

      print("PLAYER 2:")
      print()
      while(kak>0):
               t=input("NAME:")
               t=t.upper()
               if t=="":
                    print()
                    print("NAME CANNOT BE EMPTY")
                    print()
                    print()
               else:
                   MOe=len(t)
                   kak=0
                   nam2=t.strip()
                   if(len(t)>21):
                         nam2=t[:-(MOe-21)]

      L=0
      print()
      print()
      print("-"*100)
      print()
      print()
      while(2>1):
         if(L==0):
            post(pos)
         
         if(L==0):
           print(nam1,":")
           print()
         else:
             print(nam1,":","\n","(MARKER IS-",x,")")
             print()
         a1=0
         
         while(a1==0 and L==0):                              
            
             x=input("CHOOSE YOUR MARKER('X' OR 'O'):")
             print()
             print()
             x=x.strip()
             x=x.upper()
             if(x=='X' or x=='O' or x=='0'):
                          a1=1
                          if(x=='0'):
                              x='O'
                
             else:
                 print("PLEASE CHOOSE FROM THE GIVEN OPTIONS ONLY")
                 time.sleep(0.3)
                 print()
                 print()
         a2=0
         print()
         while(a2==0):
            time.sleep(0.1)
            y=input("MARK THE LOCATION(LO:SHOWS AVAILABLE LOCATION):")
            print()
            y=y.strip()
            y=y.upper()
            if(y=='LO'):
                print()
                print()
                loca(pos)
            elif(y not in hey and y in nop):
                turn(x,y,pos)
            
                
                                
                a2=1
            
            elif(y in hey and y in nop):
                
                print("THIS POSITION HAS ALREADY BEEN OCCUPIED")
                time.sleep(0.3)
                print()
                print()
                
            else:
                print("PLEASE ENTER A VALID LOCATION OR COMMAND")
                time.sleep(0.3)
                print()
                print()
           
         print()
         print()
         if(L==0):
           if(x=='X'):
               ojo='O'
           else:
               ojo='X'
         hey.append(y)
         count+=1
         if count>=5 and count!=9:
             check(ender,pos)
             
             if(len(ender)==0):
                
                print()
                post(pos)
                time.sleep(0.40)
                print("+"*100)
                print()
                print()
                print("                   ",nam1,"IS THE WINNER")
                
                print()
                print("                ","☆彡(ノ^ ^)ノ Congratulations ヘ(^ ^ヘ)☆彡")
                print()
                print("-"*100)
                print()
                score.append(nam1)
             
                break
             else:
                 post(pos)
         elif(count==9):
             time.sleep(0.44)
             print("+"*100)
             print()
             print()
             print("                   ","NO ONE WON THIS GAME")
             print()
             print()
             print("-"*100)
             score.append(0)
             print()
             break

         else:
             post(pos)
         if(L==0):
           print(nam2,": \n",ojo,"has been selected as the marker for PLAYER 2")
           print()
           
         else:
             print(nam2,":","\n(MARKER IS-",ojo,")")
        
        
         a3=0
         print()
         while(a3==0):
            k=input("MARK THE LOCATION(LO:SHOWS AVAILABLE LOCATION):")
            print()
            k=k.strip()
            k=k.upper()
            if(k=='LO'):
                print()
                print()
                loca(pos)
            elif(k in hey and k in nop):
                print("THIS POSITION HAS ALREADY BEEN OCCUPIED")
                print()
                print()
            elif(k not in hey and k in nop):
                turn(ojo,k,pos)
            
                
                                
                a3=1
                print()
                print()
            
            elif(k==y):
                print("THIS POSITION HAS ALREADY BEEN OCCUPIED")
                print()
                print()
            else:
                print("PLEASE ENTER A VALID LOCATION OR COMMAND")
                print()
                print()
         L=1
         count+=1
         hey.append(k)
         if count>=5:
             check(ender,pos)
             
             if(len(ender)==0):
                
                print()
                post(pos)
                time.sleep(0.40)
                print("+"*100)
                print()
                print()
                print("                   ",nam2,"IS THE WINNER")
                
                print()
                print("                ","☆彡(ノ^ ^)ノ Congratulations ヘ(^ ^ヘ)☆彡")
                print()
                print()
                print("-"*100)
                print()
                score.append(nam2)
              
             
                break
             
             else:
                 post(pos)
             
         else:
            post(pos)

print()
print()
print("+"*100)
print()
print()
print(" "*48,"*INFO* \n1.'n' MEANS THAT THE POSITION IS OCCUPIED \n2.LO WILL GIVE YOU THE AVAILABLE POSITIONS IN NUMERIC FORMAT \n3.THE NAMES CAN'T BE MORE THAN 21 CHARACTERS LONG\n\nNote:I might and might not add a vs computer option someday")
print()
print()
print("+"*100)
print()
print()
print()
print()
          
com=1         
while(com>0):
    newleadr=[]
    leaderboard=storedisrec(1)
    inp=input(f"● 1) START THE GAME \n\n● 2) VIEW THE LEADERBOARD \n\n● 3) DELETE THE LEADERBOARD \n\n● 4) TOTAL NO. OF ROUNDS PLAYED \n\n● 5) INFO \n\n● 6) RULES \n\n● 7) EXIT \n\n{('_'*100)}\nCHOOSE :")
    print()
    print()
    if inp=='6':
        print()
        print("_"*100)
        print()
        print()
        print(" "*48,"*RULES* \n\n"+rules)
        print()
        print()
        print("_"*100)
    elif(inp=='1'):
      
           print()
           gamestart(newleadr)
           storedisrec(0,newleadr)
    elif(inp=='2'):
        print()
        print()
        tableview(leaderboard)
    elif(inp=='3'):
            deletleader()
            print("_"*100)
            print()
            print("DELETED")
            print()
            print("_"*100)
            
    elif(inp=='4'):
             print("_"*100)
             print()
             print() 
             print("TOTAL NO OF ROUNDS PLAYED ARE--",len(leaderboard))
             print()
             print()
             print("_"*100)
    elif(inp=='5'):
                print("_"*100)
                print()
                print(" "*48,"*INFO* \n1.'n' MEANS THAT THE POSITION IS OCCUPIED \n2.LO WILL GIVE YOU THE AVAILABLE POSITIONS IN NUMERIC FORMAT \n3.THE NAMES CAN'T BE MORE THAN 21 CHARACTERS LONG")
                print()
                print()
                print("_"*100)
                
    elif(inp=='7'):
                com=0
                print()
                print("_"*100)
                print()
                print()
                print("COME AGAIN       \ (-_- )")
                print()
                print()
                print("_"*100)
                input('_')
    else:
        print("x"*100)
        print()
        print("PLEASE CHOOSE FROM THE GIVEN OPTIONS ONLY   (╯°□°）╯︵ ┻━┻")
        print()
        print("x"*100)
    
                    
    print()
    print()
    print()
