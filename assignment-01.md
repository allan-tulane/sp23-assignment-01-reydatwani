

# CMPS 2200 Assignment 1

**Name:**___Rey Datwani___


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  Yes, 2^(n+1) is in O(2^n). This is true because if you multiply a constant by 2^(n+1), it will always be greater than 2^n. For example, 2 * 2^n >= 2(n+1). This proves that 2^(n+1) in O(2^n). 
.  
.  
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  No, 2^(2n) is not in O(2^n). For example if you multiplied O(2^n) by a constant c, then you would have 2^(2n) <= c * 2^n. If you divide both sides by 2^n, then you are left with 2^n < c. There is not constant c that makes that statement true, therefore, 2^(2n) is not in O(2^n). 
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  No, n^(1.01) is not in O(log^2 n). Since f(n) is in O(g(n)), assume f(n) = n^(1.01) and O(g(n)) = O(log^2 n). The limit from n to infinity of f(n)/g(n) should equal 0. The limit from n to infinity n^(1.01)/O(log^2 n) is infinity. Therfore, n^(1.01) is not in O(log^2 n).
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes, n^(1.01) is in omega(log^2 n). Using the same logic as above. The limit from n to infinity yields infinity for f(n)/g(n). 
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  No, sqrt(n) is not in O(log n)^3. Using the same logic as above. The limit from n to infinity yields infinity for sqrt(n)/O(log n)^3 is infinity. 
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?
.  Yes, sqrt(n) is in omega(log n)^3. Using the same logic above. The limit from n to infinity yields infinity for f(n)/g(n) for both. 


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  
.  This function takes in a number x and sums it with the preceding number. The variable ra is the first preceding number and rb is the one before ra. Then ra plus rb is returned as the next number in the fibonacci sequence.
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  
.  The work of this implementation is O(n) and the span is O(n). 
.  
.  

  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   


  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  To calculate work, you start with W(n) = 2W(n/2) + 1. The height of the tree is log(n) and the number of leaves is 2^(log(n)). Therefore, you get O(n). The span is the same as above since this is a sequential algorithm. 
.  
.  

  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  
.  The work is the same as above. Since this is parallel now, you would use S(n) = S(n/2) + 1. You would multiply the worst level * the number of levels which is 1 * log(n). This would give you O(log(n)). 
.  
.