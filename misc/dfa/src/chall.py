#!/usr/local/bin/python
flag="dfa_hacked"
import sys

def set_variables():
    global no_states,trap,no_transitions,transitions,final_states,current_state,letters,error
    no_states=0
    no_transitions=0
    trap=0
    error=0
    letters=list('abcdefghijklmnopqrstuv_wxyz{}')
    transitions=[]
    final_states=[]
    current_state=0


def banner():
    banner=open("txt.txt","r").read()

    print(banner) 


def set_state():
    global no_states,no_transitions,final_states,error
    try:
        no_states=int(input("Enter number of states: "))
    except:
        print("Number of state should be an integer.")
        exit()
    if(no_states<1):
        print("Number of state can't be less than 1.")
        exit()
    print("States from q0 to q"+str(no_states-1)+" is created.")
    print("The starting state is set to q0.")
    final_states=input("Enter all the final states seperated by space (e.g., 5 7 9) to set q5,q7,q9 as final states: ")
    try:
        
        final_states.strip()
        final_states=final_states.split() 
        for i in range(len(final_states)):
            try:
                try:
                    final_states[i]=int(final_states[i])
                except:
                    print("ERROR:Final state must be integer and among valid generated states.")
                    error=1
                    exit()
                if (final_states[i]>no_states-1):
                    error=1
                    print("ERROR:Final state must be among valid generated states only.")
                    exit()
                    

            except:
                if(error==0):
                    print("ERROR:Final state must be integer and among valid generated states.")
                    error=1
                    exit()
                
    except:
        if(error==0):
            error=1
            print("ERROR:Only space seperated numbers are valid.")
            exit()
    try:
        if(error==1):
            exit()
        no_transitions=int(input("Enter the number of transitions.: "))
    except:
        if(error==0):
            error=1
            print("ERROR:Number of transitions must be integer")
            exit()
def find_transition(state,letter):
    global transitions
    global trap
    global current_state
    for transition in transitions:
        if transition[0]==state and transition[1]==letter:
            current_state=transition[2]
            return
    trap=1
def epsilon(state,finalstate): 
    global current_state
    global transitions
    global no_states
    global letters
    for letter in letters:
        transitions.append([state,letter,finalstate])
def checkdfa():
    global transitions
    for i in range(len(transitions)):
        initial=transitions[i][0]
        letter=transitions[i][1]
        final=transitions[i][2]
        for j in range(i+1,len(transitions)):
            if(transitions[j][0]==initial and transitions[j][1]==letter):
                error=1
                print("ERROR: Its DFA not NFA.")
                exit()
def antiepsilon(state,letter,finalstate):
    epsilon(state,finalstate)
    #print(transitions)
    f=transitions.index([state,letter,finalstate])
    if(f==-1):
        print("Error: Something went wrong. Check antepsilon,epsilon")
    transitions.pop(f)
def store_transitions(no_transitions):
    global error
    if(error==1):
        exit(0)
    print("Enter the transitions one at a time")
    print("Format: initial_state letter final_state")
    print("================================")
    for i in range(no_transitions):
        try:
            transition=input(">>>")
            transition=transition.split()
            transition[0]=int(transition[0])
            transition[2]=int(transition[2])

            if(len(transition)!=3 or len(transition[1])>2):
                print("ERROR:Error while storing transitions")
                #print(transition)
                exit(0)
            if (transition[1]=='@'):
                epsilon(transition[0],transition[2])
            elif  ('~' in transition[1]):
                antiepsilon(transition[0],transition[1][1],transition[2])
            else:
                transitions.append([transition[0],transition[1],transition[2]])
            checkdfa()
        except Exception as error:
            print("ERROR :Error while storing transitions.")
            error=1
            #print(error)
            exit(0)



def main():
    global no_states,trap,no_transitions,transitions,final_states,current_state,letters,error
    set_variables()
    banner()
    set_state()
    store_transitions(no_transitions)
    current_state=0
    checkdfa()
    for i in flag:
        if(error==1):
            exit()
        find_transition(current_state,i)
        if trap==1:
            print("Machine in trapped state.")
            error=1
            exit()
    if current_state in final_states:
        print("1")
    else:
        print("0")
main()
