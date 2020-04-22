# The Ten Divisibilities

This is a small script to find the solution of the following riddle, posted [here](https://www.theguardian.com/science/2020/apr/20/can-you-solve-it-john-horton-conway-playful-maths-genius) by Alex Bellos on The Guardian as 
> a celebration of John Horton Conway, the legendary British mathematician, who died of coronavirus earlier this month, aged 82.

Here is the formulation of the riddel 
>I have a ten digit number, abcdefghij. Each of the digits is different, and
>
>a is divisible by 1
>
>ab is divisible by 2
>
>abc is divisible by 3
>
>abcd is divisible by 4
>
>abcde is divisible by 5
>
>abcdef is divisible by 6
>
>abcdefg is divisible by 7
>
>abcdefgh is divisible by 8
>
>abcdefghi is divisible by 9
>
>abcdefghij is divisible by 10
>
>What’s my number?
>
>To clarify: a, b, c, d, e, f, g, h, i, and j are all single digits. Each digit from 0 to 9 is represented by exactly one letter. The number abcdefghij is a ten-digit number whose first digit is a, second digit is b, and so on. It does not mean that you multiply a x b x c x…

If I'll have time I'll post the actual solution I found with a friend (otherwise a similar solution by Alex Bellos [here](https://www.theguardian.com/science/2020/apr/20/did-you-solve-it-john-horton-conway-playful-maths-genius)), this brute force method became a necessary check after 3 failed attempted at solving it relying entirely on pen and paper.
Surprisngly, it turned out that 28 _actually is_ divisible by 7. A small detail we managed to overlook multiple times.

The code relies on only on standard Python3 libraries ([itertool](https://docs.python.org/3/library/itertools.html) for computing permutations and [time](https://docs.python.org/3/library/time.html) to record execution time).
You can run it in a command line ```bash python3 brute_force_10div.py``` from this repo folder  or with some IDE. It should take about 8s to go through all the permutations.
