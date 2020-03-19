"""
You need to climb a staircase that has n steps, and you decide to get some extra exercise by jumping up the steps. You can cover at most k steps in a single jump. Return all the possible sequences of jumps that you could take to climb the staircase, sorted.
"""

def climbingStaircase(n, k):
    answer = []

    if n < 0:
        return answer
    if n == 0:
        answer.append([])
        return answer

    for i in range(1, k + 1):
        for seq in climbingStaircase(n - i, k):
            answer.append([i] + seq)

    return answer