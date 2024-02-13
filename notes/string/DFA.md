Terminology
===========
Computational model: allowed rules for information processing.
Machine = Computer: a instantiation of the computational model
= Program = Algorithm (a specific sequence of information processing rules)


Deterministic Finite Automata 
=============================

Input String ----> DFA ----> Reject or Accept

A restricted model of computation: 
- limited memory
- reads input from left to right, and accepts or rejects. 
 


Formal definition of DFA
========================
A deterministic finite automata is a 5-tupe M = (Q, sigma, delta, q0, F)
Where: 
- Q is a finite, non-empty set (called the set of states)
- sigma is a finite, non-empty set (called the alphabet)
- delta is a function of the form sigma:Q * Sigma ---> Q
  called transition function
- q0: is an element of Q (called the start state)
- F: is a subset of Q (called the set of accepting states)




