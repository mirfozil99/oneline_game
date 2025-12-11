import random
import time
playerheal=100
monsterheal=100
MaxHP=100
MaxHM=100
healP=10
healM=15
damageP=10
damageM=25
Monsters=[ "jorabey","qondosh","qalamchi"]
damageMon=[25,18,35]
healthMon=[100,150,200]
print("choose monster you would like to fight:")
for i in range(len(Monsters)):
    print(f"{i}) {Monsters[i]} : damage-{damageMon[i]} : health-{healthMon[i]}")
while True:
    try:
                    monserchoose=input("Monter Number :")
                    if len(monserchoose)==1:
                        monserchoose=int(monserchoose)   
                        break
                    else:
                        print("""
    Wrong input, give 1,2,3 based on below options:
    """)
    except:
                 print("""
Wrong input, give 1,2,3 based on below options:
""")
Monster=Monsters[monserchoose]
damageM=damageMon[monserchoose]
MaxHM=healthMon[monserchoose]
monsterheal=healthMon[monserchoose]
mw=0
pw=0
NUM=1
print(f"""
____________________________________________________________________________________________
Player N{NUM}                                            {Monster}
health {MaxHP}/{playerheal}                              health {MaxHM}/{monsterheal}
 
       *                                           ***
      /|->                                       <<|||
       ||                                          ???
    -------------------------------------------------------------
1) attack (damge P=15, M=25)
2) heal (heals P=10 ,M=15)
3) skip (skips the turn)
______________________________________________________________________________________________
""")
while True:
    while True:
            try:
                turn=input("choose your movement : ")
                if len(turn)==1:
                    turn=int(turn)   
                    break
                else:
                  print("""
Wrong input, give 1,2,3 based on below options:
1) attack (damge P=15, M=25)
2) heal (heals P=10 ,M=15)
3) skip (skips the turn)
""")
            except:
                 print("""
Wrong input, give 1,2,3 based on below options:
1) attack (damge P=15, M=25)
2) heal (heals P=10 ,M=15)
3) skip (skips the turn)
""")

    if turn == 1:
        monsterheal-=damageP
        print(f"""Players pick -- attack
                given damage({damageP})
             
             
             """)
    elif turn == 2:
        playerheal+=healP
        if playerheal >=MaxHP:
            playerheal==MaxHP
        print(f"""Players pick -- heal
                given heal({healP})
             
             
             """)
    elif turn == 3:
       print("""players pick -- skip
             
             
             
             """)

    print(f"""
____________________________________________________________________________________________
Player N1                                            Monster
health {MaxHP}/{playerheal}                              health {MaxHM}/{monsterheal}
    
        *                                           ***
        /|->                                       <<|||
        ||                                          ???
    -------------------------------------------------------------
1) attack (damge P=15, M=25)
2) heal (heals P=10 ,M=15)
3) skip (skips the turn)
______________________________________________________________________________________________
    """)
    if monsterheal<=0:
        pw=1
        break
    time.sleep(1)
    print("monster picking")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    monstarpick=random.randint(1,3)
    if monstarpick == 1:
        playerheal-=damageM
        print(f"""Monsters pick -- attack
                given damage({damageM})
             
             
             """)
    elif monstarpick == 2:
        monsterheal+=healM
        if monsterheal >MaxHM:
            monsterhea=MaxHM
            
        print(f"""Monsters pick -- heal
                given heal({healM})
             
             
             """)
    elif monstarpick == 3:
       print("""Monsters pick -- skip
             
             
             
             """)
    print(f"""
____________________________________________________________________________________________
Player N1                                           Monster
health {MaxHP}/{playerheal}                         health {MaxHM}/{monsterheal}
    
        *                                           ***
        /|->                                       <<|||
        ||                                          ???
    -------------------------------------------------------------
1) attack (damge P=15, M=25)
2) heal (heals P=10 ,M=15)
3) skip (skips the turn)
____________________________________________________________________________________________
    """)
    if playerheal<=0:
        mw=1
        break
if mw==1:
    print("""
************************************************************
          winer winer chiken diner 
                 Monter Winer
************************************************************
""")
elif pw==1:
    print(f"""
************************************************************
          winer winer chiken diner 
                 Player{NUM} Winer
************************************************************
""")
