Deterministic Finite Automata
=============================
Why KMP is related to dfa? 
Whenever there is a match between pattern and source, dfa transition from one state to another.

   a      b      a      b      c
0 ---> 1 ---> 2 ---> 3 ---> 4 ---> 5

0 is the beginning state, and 5 is the accepting state. 

  **a**     **b**        a         b         c
0 ------> 1 ------> 2 ------> 3 ------> 4 ------> 5
                    -

Assume dfa is currently at state 2. This means "ab" is matched. 
Furthermore, if we meet different characters, dfa will transition to different states.

We define the following definition for dfa: 
```Java
/*
dfa[j][c] = nextState
0 <= j < M, in which M is the length of pattern string
0 <= c < 256, in which 256 indicates all ASCII codes
0 <= nextState <= M
*/


public int search(String text) {
    int M = pattern.length();
    int N = text.length();
    int curState = 0;
    for (int i = 0; i < N; i++) {
        curState = dfa[curState][text.charAt(i)];
        if (curState == M) return i - M + 1; 
    }
    return -1;
}

```

How to construct dfa? 
In order to determine a transition from one state to another, we need to know two things: 
(1) current state. (2) which character coming in.

```Java
for 0 <= j < M:
    for 0 <= c < 256:
        dfa[j][c] = next
```

Notes: if dfa is current at state j, then it means there are j number of characters that has been matched,
       the next character to match is at index j (0-based index) of pattern string. 

        For string, if we are using # of character as indexing. Then, i is the number of # of characters.
        Then, str[i-1] is the last character that has been considered. str[i] is the next character to be 
        considered. In other words, str[i-1] is included in the i number of characters and str[i] is not 
        included in the i number of characters. 




case 1: if the coming character (c) is equal to pattern.charAt(j) ---> next = j + 1
case 2: if the coming character (c) is different from pattern.charAt(j) --> mismatch --> restore back to a previous state
        To determine which state we restore to, we define a shadow state.
        The shadow state has the follow property: 
        (1) it represents a proper prefix of pattern string
        (2) it is equal to the longest suffix of pattern[0:j)
        Then, since we know dfa[shadow][c] <--- calculated previously.
        We can reuse the transition of dfa[shadow][c]. 
        

```Java
public class KMP {
    private int[][] dfa;
    private String pattern;

    public KMP(String pattern) {
        this.pattern = pattern;
        this.dfa = buildDFA();
    }

    private int[][] buildDFA() {
        int M = pattern.length();
        int[][] dfa = new int[M][256];         // Think: why M not M+1? 
        dfa[0][pattern.charAt(0)] = 1; // No need to subtract 'a', as we are considering all ASCII code here
        int shadow = 0;

        for (int curState = 1; curState < M; curState++) {
            for (int c = 0; c < 256; c++) {
                if (c == pattern.charAt(curState)) {
                    dfa[curState][c] = curState + 1;
                } else {
                    dfa[curState][c] = dfa[shadow][c];
                }
            }
            shadow = dfa[shadow][pattern.charAt(curState)];
        }
        return dfa;
    }

    public int search(String text) {
        int M = pattern.length();
        int N = text.length();
        int curState = 0;
        for (int i = 0; i < N; i++) {
            char curChar = text.charAt(i);
            curState = dfa[curState][curChar];
            if (curState == M) return i - M + 1; 
        }
        return -1;
    }
}

```

source: [KMP](https://mp.weixin.qq.com/s/r9pbkMyFyMAvmkf4QnL-1g)
