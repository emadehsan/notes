from typing import List

'''
this file has both Bottom Up & Top Down approaches to solve this problem.

following method implements bottom up Dynamic Programming approach

relies on the intuition that:
  if there are x different possible states that can exist to reach C[i],
  there will only be at max x+1 different future states.
'''
def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  '''
  time: O(M^2):
      * there are M codes to be entered on either of the wheels
      * for each of those codes, the states set will contain at max M+1 states, other than the initial location 1, 
        no other code will be appear on either of the wheels that is not in the codes list C.
        duplicate states get removed. e.g. to go from 
          curr_states [(1,2), (1,4),(1,6)] to Code 3, you will have only these 
          next_states [(1,3), (2,3), (3,4), (3,6)]

  space: O(M+1)
  '''

  def distance(src, dest):
    return min(abs(src-dest), N - abs(src-dest))
  
  # starting states of both wheels and total cost so far
  states = dict()
  states[(1,1)] = 0

  for i in range(M):
    # we can use both locks to reach C[i]. let's remember all unique possible states
    # cause we might have to make some sub-optimal decisions, to achieve optimal overall costs

    next_state = dict()

    for A, B in states:
      cost = states[(A, B)]

      cost_a = distance(A, C[i])
      
      # write smaller wheel state first. order of wheels doesnt matter. we just need to avoid duplicate states in dict
      state_a = (min(C[i], B), max(C[i], B))

      if state_a not in next_state:
        next_state[state_a] = cost_a + cost
      next_state[state_a] = min(next_state[state_a], cost_a + cost)  # keep the smaller cost that ends with current combination/state

      cost_b = distance(B, C[i])
      
      state_b = (min(C[i], A), max(C[i], A))

      if state_b not in next_state:
        next_state[state_b] = cost_b + cost
      next_state[state_b] = min(next_state[state_b], cost_b + cost)

    # update current state for next iteration
    states = next_state
    
  # for the final state, pick the lowest cost of all states
  least_cost = float('inf')
  for A, B in states:
    least_cost = min(least_cost, states[(A, B)])

  return least_cost
  

'''
 Top-Down Dynamic Programming approach. Easier to arrive, but 
 computes all possible wheel states. Which can be M.

 Time: O(M^3)
 Space: O(M^3)
'''
def getMinCodeEntryTimeTopDown(N: int, M: int, C: List[int]) -> int:
  cache = {}
  def pick(i, A, B):
    # A: current code on wheel A
    # B: current code on wheel B
    
    if i == M:
      return 0
    
    if (i, A, B) in cache:
      return cache[(i, A, B)]
    
    # use lock wheel A
    # choices:
    # move A forward or backward to C[i]: abs(C[i]-A)
    # move A forward / backward to reach N, and then reach C[i]: N - (C[i] - A)
    cost_a = min(abs(C[i] - A), N - abs(C[i] - A))
    # if we moved A to C[i], for next stage, A will be C[i]
    subproblem_a = pick(i+1, C[i], B)

    cost_b = min(abs(C[i] - B), N - abs(C[i] - B))
    subproblem_b = pick(i+1, A, C[i])

    cache[(i, A, B)] = min(cost_a + subproblem_a, cost_b + subproblem_b)
  
    return cache[(i, A, B)]

  # start solving from C[0], wheels are at 1, 1
  return pick(0, 1, 1)


def test():
  testcases = [
    [3, 3, [1, 2, 3]],
    [10, 4, [9, 4, 4, 8]],
    [7, 10, [2, 5, 6, 7, 1, 4, 1, 7, 2, 3]]
  ]

  for N, M, C in testcases:
    print(
      getMinCodeEntryTime(N, M, C)
    )

test()
