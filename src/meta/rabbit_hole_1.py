from typing import List

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
  '''
  do partially-overlapping paths exist?

  5 -> 4 -> 3 -> 2 -> 4
  4 -> 3 -> 2 -> 4

  1, 4, 2, 3, 5

  how to cover overlapping paths?

  observations:
  1. once inside a cycle, all nodes in the cycle will be visited. 
    so for the nodes in cycle, set the path length for each of those to the size of the cycle
  2. for all the other nodes that lead to the cycle, add their respective sizes by unrolling the stack

  '''

  # convert to 0-indexed page numbering
  for i in range(N):
    L[i] -= 1

  # starting at i-th node, the path length:
  path_len = [0] * N

  for i in range(N):
    if path_len[i] == 0:
      visited = set()
      path_stack = []
      j = i
      while j not in visited and path_len[j] == 0:
        visited.add(j)    
        path_stack.append(j)
        j = L[j]

      # path_len > 0 and j in visited won't be simultanously true, because that means j is in a cycle and its path is already known
      # if its path is already known, we wouldn't have started exploring it in the first place
      if path_len[j] > 0 and j not in visited:
        # case 2: we already know the path_len for nodes j on-wards, just use their path_len
        # unstack nodes, setting their path_len
        # now, for all the other nodes in the path_stack, set their path size
        count = 1
        while path_stack:
          node = path_stack.pop()
          path_len[node] = count + path_len[j]
          count += 1
      else:
        # cycle is found. count cycle size. set path len equal to size of cycle for all nodes in the cycle. 
        # for nodes leading to the cycle, set path len by unpacking the stack
        set_path_len(path_len, path_stack, L, j)

  return max(path_len)

def set_path_len(path_len, path_stack, L, j):
  cycle_nodes = set()
  cycle_len = 0
  k = j
  while k not in cycle_nodes:
    cycle_len += 1
    cycle_nodes.add(k)
    k = L[k]

  # now, for all the node in the cycle, set path_len to be cycle size
  for node in cycle_nodes:
    path_len[node] = cycle_len

  # now, for all the other nodes in the path_stack, set their path size
  count = 1
  while path_stack:
    node = path_stack.pop()
    if node not in cycle_nodes:
      path_len[node] = count + cycle_len
      count += 1

def test():
  testcases = [
    [4, 1, 2, 1],
    [4, 3, 5, 1, 2],
    [2, 4, 2, 2, 3],
  ]

  for L in testcases:
    print(
      getMaxVisitableWebpages(len(L), L)
    )

test()
