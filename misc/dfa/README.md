# Machine Trouble

The challenge allows the user to define the states and transitions for a DFA . The program runs the flag against the machine defined by user and gives output 1 if the flag is part of the machine defined else 0 is returned. There can be situation where the machine gets stuck due to absence of valid transition to run over the string.

Here are few test machines to understand the method to get insight about flag.

Algorithm to check if the first letter is ‘d’ or not.

```
3
2
4
0 d 2
0 ~d 1
2 @ 2
1 @ 1
```

Algorithm to check if the third letter is ‘a’ or not.

```
5     //NUmber of states
4     // Final state
6     //Number of Transition
0 @ 1 //Transitions
1 @ 2
2 a 4
2 ~a 3
4 @ 4
3 @ 3
```

Flag:pearl{dfa_hacked}
