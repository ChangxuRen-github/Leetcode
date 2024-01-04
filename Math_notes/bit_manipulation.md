### Links

|I am here|
|Here I am|

- this is the first item of the list
    - this is the inner item of the above list

```java
public class Example {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(args));
    }
}
```


Bit Operations
===============
AND operation:
--------------
The AND operation x & y produces a number that has one bits in positions
where both x and y have one bits. Using the AND operation, we can check
if a number x is even because x & 1 = 0 if x is even, and x & 1 = 1 if x 
is odd. **More generally, x is divisible by 2^(k) exactly when x & (2^(k) - 1) = 0.**   
####Useful properties: 
- bit & 0 = 0
- bit & 1 = bit

OR operation:
-------------
The OR operation x | y produces a number that has one bits in positions where at least
one of x and y have one bits.  
####Useful properties:
- bit | 0 = bit
- bit | 1 = 1



