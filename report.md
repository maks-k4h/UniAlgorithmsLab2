## Lab 2 report

### Constants

*n = 10^6* — assumed size of the set;
*p = 0.01 = 1%* — desired false positive probability;

Therefore:
m = -n * ln(p) / (ln2)^2 = -10^6 * ln(0.01) / (ln2)^2 = 9,585,058 — recommended number of Blum-bits
l = m / n ln2 = -ln(p) / ln2 = -ln(0.01) / ln2 = 6.64385618977

We set:
M = 10,000,000
L = 7


### Example 

Input:

``` 
add apple
add banana
add cherry
has apple
has banana
has grape
add grape
has grape
#

```

Output:

```
Y
Y
N
Y

```