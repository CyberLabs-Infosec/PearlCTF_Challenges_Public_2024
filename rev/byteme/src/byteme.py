from hashlib import md5
import time

def crackme():
    print("""                           o                    
                       _---|         _ _ _ _ _ 
                    o   ---|     o   ]-I-I-I-[ 
   _ _ _ _ _ _  _---|      | _---|    \ ` ' / 
   ]-I-I-I-I-[   ---|      |  ---|    |.   | 
    \ `   '_/       |     / \    |    | /^\| 
     [*]  __|       ^    / ^ \   ^    | |*|| 
     |__   ,|      / \  /    `\ / \   | ===| 
  ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
  I_I__I_I__I_I  (====(_________)___|_|____|____
  \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_| 
   |[]      '|   | []  |`__  . [  \-\--|-|--/-/  
   |.   | |' |___|_____I___|___I___|---------| 
  / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] | 
 <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \  
 ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===> 
 ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [ 
 <===>     ' ||||| |   |   | ||||.||  []   <===>
  \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/ 
   |      . _||||| |   |   | ||||.|| |     | |
../|' v . | .|||||/____|____\|||| /|. . | . ./
.|//\............/...........\........../../\\
""")
    print()
    print("Welcome Warrior! You have made it till here")
    print("This is where best of the best have fallen prey to the fate")
    print()
    print("It is written that only the true Thalor can get The sword of Eldoria")
    print("Do you have what it takes to be Thalor?")
    print("Prove your mettle by bringing the sword out of the castle")
    print()
    print("Go on! unlock the castle with XEKLEIDOMA spell")

    print()
    spell = input("> ")
    print()

    if len(spell.strip()) != 12 or md5(spell.strip().encode()).hexdigest() != "9ce86143889d80b01586f8a819d20f0c":
        print("You are not THE ONE")
        print("True Thalor is a master of sorcery")
        print("Ground beneath you opens up and you fall into the depths of hell")
        exit()

    print("The door is opened!")
    print("You surely mastered sorcery")
    print()
    time.sleep(3)

    return spell

def solveme():
    print("""
                                            .""--..__
                     _                     []       ``-.._
                  .'` `'.                  ||__           `-._
                 /    ,-.\                 ||_ ```---..__     `-.
                /    /:::\\               /|//}          ``--._  `.
                |    |:::||              |////}                `. |
                |    |:::||             //'///                   -
                |    |:::||            //  ||'     
                /    |:::|/        _,-//\  ||
               /`    |:::|`-,__,-'`  |/  \ ||
             /`  |   |'' ||           \   |||
           /`    \   |   ||            |  /||
         |`       |  |   |)            \ | ||
        |          \ |   /      ,.__    \| ||
        /           `         /`    `\   | ||
       |                     /        \  / ||
       |                     |        | /  ||
       /         /           |        `(   ||
      /          .           /          )  ||
     |            \          |     ________||
    /             |          /     `-------.|
   |\            /          |              ||
   \/`-._       |           /              ||
    //   `.    /`           |              ||
   //`.    `. |             \              ||
  ///\ `-._  )/             |              ||
 //// )   .(/               |              ||
 ||||   ,'` )               /              //
 ||||  /                    /             || 
 `\\` /`                    |             // 
     |`                     \            ||  
    /                        |           //  
  /`                          \         //   
/`                            |        ||    
`-.___,-.      .-.        ___,'        (/    
         `---'`   `'----'`
""")
    print()
    print("As you walk in, you see a spectral figure Elyrian, the Guardian of Souls")
    print("He speaks to you in a voice that echoes through the chamber")
    print()
    print('"Brave warrior, before you lies the next trial on your path. Answer my riddle, and prove your worthiness to continue your quest."')

    print('''
"I am a word of ten, with numbers and letters blend,
Unravel me, and secrets I'll send.
Though cryptic in sight, I hold the code tight,
Unlock my mystery with wit and might."
''')
    
    answer = input("> ")
    print()
    answer = list(map(ord, list(answer.strip())))
    
    try:
        assert len(answer) == 10
        assert answer[6] + answer[7] + answer[8] - answer[5] == 190 
        assert answer[6] + answer[5] + answer[5] - answer[2] == 202 
        assert answer[9] + answer[3] + answer[2] + answer[5] == 433 
        assert answer[7] + answer[0] - answer[0] + answer[3] == 237 
        assert answer[1] - answer[9] - answer[5] + answer[4] == -50 
        assert answer[2] - answer[3] + answer[1] - answer[1] == -6 
        assert answer[8] - answer[7] - answer[6] + answer[5] == -88 
        assert answer[0] + answer[8] - answer[5] - answer[3] == -117 
        assert answer[5] + answer[6] + answer[8] + answer[2] == 385 
        assert answer[5] - answer[4] - answer[5] + answer[9] == 4 
        assert answer[2] - answer[9] + answer[5] - answer[0] == 63 
        assert answer[2] - answer[5] + answer[4] - answer[9] == 13 
        assert answer[8] + answer[3] + answer[7] - answer[6] == 167 
        assert answer[6] - answer[5] - answer[0] - answer[5] == -126 
        assert answer[2] - answer[5] - answer[6] - answer[4] == -199 
    except AssertionError:
        print("You are not worthy")
        print("Your soul has been cursed")
        print("You will seek your own death in a fortnight")
        exit()

    print("You have proven your `wit and might`")
    print("Elyrian, the Guardian of Souls, bows to you")
    print("You have unlocked the next chamber")
    print()
    time.sleep(4)

    return "".join([chr(x) for x in answer])

def breakme():
    sword = """
                      _..._
                     /MMMMM\\
                    (I8H#H8I)
                    (I8H#H8I)
                     \WWWWW/
                      I._.I
                      I._.I
                      I._.I
                      I._.I
                      I._.I
                      I._.I
                      I._.I
                      I.,.I
                     / /#\ \\
                   .dH# # #Hb.
               _.~d#XXP I 7XX#b~,_
            _.dXV^XP^ Y X Y ^7X^VXb._
           /AP^   \PY   Y   Y7/   ^VA\\
          /8/      \PP  I  77/      \8\\
         /J/        IV     VI        \L\\
         L|         |  \ /  |         |J
         V          |  | |  |          V
                    |  | |  |
                    |  | |  |
                    |  | |  |
                    |  | |  |
 _                  |  | |  |                  _
( \                 |  | |  |                 / )
 \ \                |  | |  |                / /
('\ \               |  | |  |               / /`)
 \ \ \              |  | |  |              / / /
('\ \ \             |  | |  |             / / /`)
 \ \ \ )            |  | |  |            ( / / /
('\ \( )            |  | |  |            ( )/ /`)
 \ \ ( |            |  | |  |            | ) / /
  \ \( |            |  | |  |            | )/ /
   \ ( |            |  | |  |            | ) /
    \( |            |   Y   |            | )/
     | |            |   |   |            | |
     J | ___...~~--'|   |   |`--~~...___ | L
     >-+<...___     |   |   |     ___...>+-<
    /     __   `--~.L___L___J.~--'   __     \\
    K    /  ` --.     d===b     .-- '  \    H
    \_._/        \   // I \\   /        \_._/
      `--~.._     \__\\ I //__/     _..~--'
             `--~~..____ ____..~~--'
                    |   T   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    |   |   |
                    I   '   I
                     \     /
                      \   /
                       \ /
                       """
    
    sword = sword.split("\n")

    for line in sword:
        print(line)
        time.sleep(0.1)

    print()
    print("There it is! The sword of Eldoria")
    print("Break it's shackles and show that you are the Thalor")
    print()

    chain = input("> ")
    print()

    best = [117, 84, 87, 108, 59, 85, 66, 71, 71, 30, 16]
    mod = list()
    plier = 69

    for i in range(len(chain)):
        mod.append(plier ^ ord(chain[i]))
        plier = ord(chain[i])
    
    if mod == best:
        print("Oh! True Thalor, you have broken the shackles")
        print("You are the chosen one")
        print("I kneel before you")
        print("Go on! Take the sword and fulfill your destiny")
        print()
        time.sleep(2)
        return chain
    else:
        print("You are not worthy")
        print("The fate has you in it's grip")
        print("You will be forgotten in the sands of time")
        exit()

if __name__ == "__main__":
    spell = crackme()
    answer = solveme()
    chain = breakme()

    print("Thalor has risen!")
    print("The prophecy has been fulfilled")
    print()
    print("#" * 39)
    print("##", " " * 33, "##")
    print("##", f"{spell}{answer}{chain}", "##")
    print("##", " " * 33, "##")
    print("#" * 39)
