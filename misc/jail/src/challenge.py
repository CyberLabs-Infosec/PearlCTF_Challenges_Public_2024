#!/usr/local/bin/python
import blackbox as blackbox
import time
flag="pearl{j41l_3sc4p3_succ3sful_362de4}"

def banner():
    file=open("txt.txt","r").read()
    print(file)
def main():
    banner()
    cmd=input(">>> ")
    time.sleep(1)
    cmd=blackbox.normalise(cmd)
    if(blackbox.check_blocklist(cmd)):
        try:
            print(eval(eval(cmd)))
        except:
            print("Sorry no valid output to show.")
    else:
        print("Your sentence has been increased by 2 years for attempted escape.")
main()
