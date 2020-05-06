#!/usr/bin/env python
# coding: utf-8

# # Dynamic Programming

# ## What is Dynamic Programming? 
# Dynamic Programming (DP) is a technique for solving complicated problems by breaking them down into *simpler subproblems*. 
# 
# ### This lecture we'll...
# * Introduce characteristics of DP problems
# * Walk through the main concepts behind DP using the Fibonacci Sequence as a basic example
# * Practice implementing an algorithm to a classic DP problem
# 
# ### Goals: 
# * Understand what optimal substructure and overlapping subproblems means
# * Use memoization or tabulation to decrease runtime
# * Translate a given recurrence relation into a working implementation

# ## What types of problems can we solve with DP? 
# 
# * Optimization
#   * Maximize/minimize some value given these constraints
# * Combinatorial
#   * How do we choose items from a set to meet certain conditions
# * DP Problems have **optimal substructure** and **overlapping subproblems**
# 

# # Fibonacci Sequence

# 
# ## What is the Fibonacci Sequence? 
# 
# 0, 1, 1, 2, 3, 5, 8, 11, 13...
# 
# Each element in the Fibonacci Sequence is the sum of the previous two elements. 
# 
# $$F(0) = 0$$
# $$F(1) = 1$$
# $$F(n) = F(n-1) + F(n-2)$$

# In[ ]:


def fib(n): 
    """Returns the nth Fibonacci number"""
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
 


# In[ ]:


print(fib(10)) 


# ## What do we notice about the implementation of `fib`?

# 1. It's recursive!
#     1. A function is recursive if the function calls itself.
#     1. Each call to `fib` is smaller than the previous call --> these are "subproblems" of the original problem
#     1. We use the results from the smaller subproblems to calculate the result for the larger problem 
#     

# ### Optimal Substructure
# A problem has **optimal substructure** if the optimal solution to the problem can be constructed from the optimal solutions of the subproblems. 
# 
# In otherwords, the optimal solution can be defined recursively, and the relationship between the optimal solution and the sub-solutions is the **recurrence relation**.
# 
# * What are other examples of problems with optimal substructure? 
#     * Shortest Path: Let's say you're trying to find the shortest path from city A to city B ($P(A, B)$). The path between any two points on $P(A,B)$ will be the shortest path between those two points.  

# ## What else do we notice about the implementation in fib?
# 
# 2. It's a pretty inefficient implementation

# In[ ]:


import time

def time_fib(fib_func, n): 
    start = time.time()
    fib_func(n)
    end = time.time()
    print(f"{n}: {end-start}")


# In[ ]:


for i in [5, 10, 15, 20, 25, 30, 35, 40]:
    time_fib(fib, i)


# ![call tree for fib(6)](attachment:fib_tree.jpeg)
# 
# 1. How many times is `fib(2)` called?
# 1. How many times is `fib` called in the above diagram? 
# 

# 1. How many times is `fib(2)` called? 
#     1. 5
# 1. How many times is `fib` called? 
#     1. For `fib(6)`: 25
#     1. In general, `fib` has an lower bound of $2^{n/2}$ calls and upperbound of $2^{n-1}$. So the overall runtime is $O(2^n)$ which is exponential!

# ## Overlapping Substructure
# 
# A problem has **overlapping substructure** if it can be broken down into subproblems which are **reused several times**
# 
# 
# We end up doing a lot of repeat work. How can we optimize this?

# ## Idea 1: Memoization
# 
# Store the results to the subproblems as we go so we can access them later without recomputing.
# 
# **Key Idea:** We can use extra space to decrease the runtime (**space-time tradeoff**)

# In[ ]:


memo = {}  # global cache

def fib_memo1(n): 
    # Base cases
    if n == 0: return 0
    if n == 1: return 1
    
    # Check if the result is already in the cache and return it if present
    raise NotImplementedError("Fill this in")
    
    # If not, calculate the result and store it in the cache. 
    solution = fib_memo1(n-1) + fib_memo1(n-2)
    raise NotImplementedError("Fill this in")    

    return solution


# In[ ]:


for i in [10, 20, 30, 40, 50]:
    time_fib(fib_memo1, i)


# In[ ]:


# Sidenote: Python has a built in cache you can use!
import functools

@functools.lru_cache  # <-- this is called a decorator
def fib_memo2(n): 
    if n == 0: return 0
    if n == 1: return 1
    return fib_memo2(n-1) + fib_memo2(n-2)


# ## Idea 2: Tabulation
# 
# Calculate and store the results to the subproblems *beforehand*, starting from `0` and working way up to `n`.
# * Memoization is top-down and recursive
# 
# * Tabulation is bottom-up and iterative

# In[ ]:


def fib_tab(n): 
    # initialize array and fill in the "base cases"
    tab = [0 for i in range(0, n+1)]
    tab[0] = 0
    tab[1] = 1

    # Calculate and store the rest of the values
    for i in range(2, n+1): 
        raise NotImplementedError("Fill this in")
    
    return tab[n]


# In[ ]:


for i in [5, 10, 15, 20, 30, 50]:
    time_fib(fib_tab, i)


# In[ ]:


# Extra credit: Fib with "sliding window" 
# fib_tab currently keeps track of all previously calculated values of fib from i=0...n
# Try reducing the amount of space requires by only keeping track of the previous
# two values

def fib_tab2(n):
    raise NotImplementedError("Fill this in")


# # Summary of Key Points
# 
# 1. Problems that can be solved by DP have: 
#     1. **Optimal Substructure** 
#         1. The problem has a recurrence relationship
#         1. You can use the solution to smaller subproblems to solve the overall problem. 
#     1. **Overlapping Subproblems** 
#         1. Can reduce computation time by using extra space to store the intermediate results
#     1. Approaches for implementing DP algorithms: 
#         1. **Memoization** (recursive, top-down)
#         1. **Tabulation** (iterative, bottom-up)

# ## Example: Weighted Interval Scheduling

# We have a set of jobs. Each job has a **start time** `job.start`, an **end time** `job.end` (`job.start < job.end`) and a **value** or profit associated with it `job.value`. Two jobs are **compatible** if they don't overlap. We want to find the subset of compatible jobs with the **maximum value**
# 
# ![weighted interval scheduling example](attachment:weighted_intervals_overview.png)
# 
# e.g., I'm a freelancer trying to schedule my next ten weeks. I'm considering a set of gigs that have set start/end times and will pay me certain amounts. I can only take one gig at once. How do I maximize how much I can earn?
# 

# ### Example: Weighted Interval Scheduling
# 
# ![weighted interval scheduling example](attachment:weighted_interval_start.png)
# 
# * The red box indicates the scope of the current problem we're considering.
# * Sort the jobs by increasing finish time. Consider each job in reverse order, starting with the last job. 
# * Let's say we're looking at the $j$th job. We can either include it or not include it. 

# ### Option 1: Include the job
# 
# If we include job $j$, we can only consider including other jobs that finish before job $j$ starts. 
# ![Subproblem when including the current job](attachment:weighted_intervals_option1_subproblem.png)
# * Let's define $p(j)$ as the index of the last job that finishes before job $j$ starts. 
# * The optimal value for this solution is the value of the current job ($jobs[j].value$) plus the optimal solution for jobs from $0...p(j)$

# ### Option 2: Exclude the job
# 
# If we don't exclude the job, we can consider all other jobs before job $j$. 
# ![Subproblem when including the current job](attachment:weighted_intervals_option2_subproblem.png)
# The optimal value is the optimal solution for jobs from $0...j - 1$.

# ![partial call tree for weighted interval scheduling](attachment:weighted_intervals_partial_tree.png)

# ### Recurrence relationship
# 
# * Jobs are labeled from $j = 0...n$ in order of increasing finish time. 
#     * We use $j$ to index into the given list of jobs. 
# * $OPT(j)$ is the optimal solution to the problem consider jobs from $0...j$. 
#     * Base case is when we are considering 0 jobs, which means we can have 0 value. $OPT(-1) = 0$
# * $p(j)$ is the index of the last job that finishes before job $j$ starts
#     * `jobs[p(j)].finish <= jobs[j].start`
#     * $p(j) = -1$ if there is no job that finishes before $j$ starts
#     * $p(j) < j$
# 
# $$OPT(-1) = 0$$
# $$OPT(j) = \max (jobs[j].value + OPT(p(j), OPT(j-1))$$
# 

# In[ ]:


from collections import namedtuple
from typing import List, Tuple, Dict

Job = namedtuple('Job', 'start, end, value')


# Extra: What's the current run time for this implementation? Is there a way we could decrease the run time? 
def get_previous_jobs(jobs: List[Job], job_index: int):
    """ 
    Given a list of jobs and a job, returns the index of the last job that finishes before the given job starts. 
    Returns -1 if there are no non-overlapping previous jobs
    """
    current_job = jobs[job_index] 
    
    for i in range(job_index - 1, -1, -1):  # Iterate through jobs backwards
        prev_job = jobs[i]
        if prev_job.end <= current_job.start: 
            return i
    return -1


# In[ ]:


def weighted_intervals(jobs: List[Job]) -> int: 
    """ Given a list of jobs with weights, returns the maximum possible value from a subset of compatible jobs."""
    def _weighted_intervals(current_job_index: int) -> int:
        """Helper function that takes current_job_index (j) to index into the list of jobs"""
        # Base case: OPT(-1) = 0
        if current_job_index == -1: 
            return 0

        # Option 1: include the last job
        # get jobs that finish before current job: p(j)
        previous_jobs_index = get_previous_jobs(jobs, current_job_index)  

        # solve subproblem: OPT(p(j))
        raise NotImplementedError("Uncomment the below line and fill it in")
        # subproblem_value = ???

        # use result from subproblem to calculate overall solution: jobs[j].value + OPT(p(j))
        include_value = jobs[current_job_index].value + subproblem_value  

        # Option 2: exclude the last job 
        # solve subproblem: OPT(j-1)
        raise NotImplementedError("Uncomment the below line and fill it in")
        # exclude_value = ???

        # Choose the maximum of the two options
        return max(include_value, exclude_value)
    
    return _weighted_intervals(len(jobs) - 1)


# In[ ]:


jobs = [
    Job(1, 3, 2), 
    Job(0, 5, 5), 
    Job(2, 5, 8),
    Job(3, 6, 5), 
    Job(5, 8, 3), 
    Job(6, 10, 1)
]

print(weighted_intervals(jobs))


# * Notice we haven't added memoization or tabulation yet. 
#     * How many times do we end up calling `_weighted_intervals(0)`? 

# In[ ]:


def weighted_intervals_memo(jobs: List[Job]) -> int: 
    """ Given a list of jobs with weights, returns the subset of jobs that maximizes the value of the jobs."""
    cache = {}
    def _weighted_intervals_memo(current_job_index: int) -> int:
        """Helper function that takes an index into the list of jobs and a cache of previously calculated subproblems."""
        # Check if we've already solved this problem before: 
        if current_job_index in cache:
            return cache[current_job_index]

        # Base case: OPT(-1) = 0
        if current_job_index == -1: 
            return 0

        # Option 1: include the last job
        # get jobs that finish before current job: p(j)
        previous_jobs_index = get_previous_jobs(jobs, current_job_index)  

        # solve subproblem: OPT(p(j))
        subproblem_value = _weighted_intervals(previous_jobs_index)

        # use result from subproblem to calculate overall solution: jobs[j].value + OPT(p(j))
        include_value = jobs[current_job_index].value + subproblem_value  

        # Option 2: exclude the last job 
        # solve subproblem: OPT(j-1)
        exclude_value = _weighted_intervals(current_job_index - 1)  
        
        # Choose the maximum of the two options
        solution = max(include_value, exclude_value)
        
        # Add current problem and solution to the cache
        cache[current_job_index] = solution
        return solution
    return _weighted_intervals_memo(len(jobs) - 1, {})

print(weighted_intervals_memo(jobs))


# ### Implementation: Extensions and Next Steps
# 
# * How would you implement this with tabulation? 
# 
# * Right now we're only returning the value of optimum solution. How would you return the actual subset of jobs as well?

# In[ ]:


def weighted_intervals_tab(jobs): 
    """ Given a list of jobs with weights, returns the subset of jobs that maximizes the value of the jobs."""

    # Fill in max_value to contain the maximum value from the set of jobs from 0...i
    max_value = [0 for _ in jobs]
    
    for current_job_index, job in enumerate(jobs):
        # Option 1: Include the job
        # get jobs that finish before current job: p(j)
        previous_job_index = get_previous_jobs(jobs, current_job_index)

        # Get the solution to the subproblem
        if previous_job_index == -1:
            # No previous jobs finish before current job starts. Base case
            raise NotImplementedError("Uncomment the below line and fill it in")
            # subproblem_value = ???
        else: 
            # OPT(p(j))
            raise NotImplementedError("Uncomment the below line and fill it in")
            # subproblem_value = ???

        # use result from subproblem to calculate overall solution: jobs[j].value + OPT(p(j))
        include_value = subproblem_value + job.value
        
        # Option 2: Exclude the job
        if current_job_index == 0:  
            # j-1 would be -1. Base case
            raise NotImplementedError("Uncomment the below line and fill it in")
            # exclude_value = ???
        else:
            # Get the solution to subproblem: OPT(j-1)
            raise NotImplementedError("Uncomment the below line and fill it in")
            # exclude_value = ???
        
        # Choose the maximum of the two options
        raise NotImplementedError
        
    return max_value[-1]  # Return solution to the overall problem

print(weighted_intervals_tab(jobs))


# ## Summary
# 
# * Why talk about DP? 
# * You probably won't be coming up with new DP algorithms every day, but
#     * DP algorithms have applications across industries and in many tools you use daily.
#     * The core concepts of DP are important to understand in computer science. 

# ### DP in Real Life
# 
# * Shortest Path: Bellman-Ford 
#     * Network routing
# * Longest Common Subsequence
#     * DNA Sequence Alignment 
#     * Document diffing (`git diff`)
# * E-commerce: [Calculating dicount offers](https://medium.com/myntra-engineering/discount-offers-using-dynamic-programming-ba383098c628)
#     * Each item has an original sticker price and a discount associated with it (e.g., 20% off an original sticker price of $50).
#     * Each item can also be part of a Buy One Get One Free offer, where you can combine pairs of items and get the one with the lower original sticker price for free.
#     * You cannot apply an item's discount if you're also using it as part of a BOGO deal. 
#     * How do you optimally apply the available discounts to maximize your savings? 
# 

# ### DP in YOUR life 
# 
# * Optimal Substructure
#     * Recursion is everywhere in computer science. 
#         * Trees, XML, File systems
#         * Linked lists
#         * Sorting and searching
#     * It's also a popular topic for SWE interviews
# * Overlapping Subproblems 
#     * Space-Time tradeoff: memoize or tabulate
#     * Memoization is a form of caching
#     * If your program is really slow, ask if there's repeat work being done and if you can store intermediate results somewhere

# # Questions?