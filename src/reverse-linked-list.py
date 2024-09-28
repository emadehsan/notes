from typing import List, Optional

# an instance of this class acts like a item / node in our linked list
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

  
def create_linked_list(nums: List[int]) -> Optional[Node]:
  if len(nums) == 0:
    return None
  
  head = Node(nums[0])
  ptr = head

  for i in range(1, len(nums)):
    ptr.next = Node(nums[i])
    ptr = ptr.next

  return head

def print_linked_list(head: Node):
  if head is None:
    return

  ptr = head

  while ptr:
    print(ptr.val, ' -> ', end='')
    ptr = ptr.next
  print(None)

def reverse_linked_list(head: Node) -> Optional[Node]:
  if head is None:
    return None
  
  # ptr will traverse the list
  ptr = head
  # prev will point to the node just behind ptr, so that ptr could reverse its next (i.e. ptr.next) pointer
  prev = None 

  while ptr is not None:
    # save the reference to the next pointer in the list
    future = ptr.next

    # reverse step: point the current pointer's next to it's previous item
    ptr.next = prev  # this step reverses the node's arrow

    # current pointer will be prevoius for the next iteration
    prev = ptr

    # now move to the original next node
    ptr = future

  # the last item will become the head in reversed list
  head = prev

  return head


def test():

  nums = [1,2,3,4,5,6,7]
  ll = create_linked_list(nums)

  print('Original Linked List:')
  print_linked_list(ll)

  rll = reverse_linked_list(ll)
  print('\nReversed Linked List:')
  print_linked_list(rll)


test()
