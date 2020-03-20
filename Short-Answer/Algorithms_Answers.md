#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) this is linear as input increases, the run time will increase at same rate.

b) O(n^2) this is polynomial. Most of the time nested loops are n^2. The first loop will have time O(n) and the second loop will have time O(n) for each index of the parent loop. So O(n \* n) or O(n^2).

c) O(n) linear. So bunnyEars(bunnies - 1) will actually be O(n) and all other statements are O(1). Constants get removed. O(n).

## Exercise II

So we have an n-story building and want to find the value of f-floor that doesn't break my egg. My first solution would be to use binary search to find f. Since the floors are sorted from smallest to largest this will work.
So find middle floor and throw egg off.
If egg breaks, we now use the bottom half only. If egg doesn't break, we now use the top half only.
Then we repeat the process finding the middle on whichever side passes.
Drop egg at new middle
Repeat process until we find egg[i] does not break, and egg[i + 1] does break.

Time complexity: O(log n) or linearithmic
