"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  if (x <= 1):
    return x
  else:
    ra, rb = foo(x - 1), foo(x - 2)
    return ra + rb
    ### TODO
    pass

def longest_run(mylist, key):
  greatestRun = 0
  count = 0
  for i in mylist:
    if i == key:
      count += 1
    else:
      greatestRun = max(greatestRun, count)
      count == 0
  return max(greatestRun, count)
    ### TODO
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
  if len(mylist) == 1:
    mylist[0] == key
    
  middle = len(mylist) // 2
  left = longest_run_recursive(mylist[0:middle], key)
  right = longest_run_recursive(mylist[middle:], key)
  l = left.left_size
  r = right.right_size
  greatestRun = 0

  if left.is_entire_range:
    l = middle
  if right.is_entire_range:
    r = len(mylist) - middle
  if left.is_entire_range && right.is_entire_range:
    return result 

  if right.left_size > 0 && left.right_size > 0 || right.is_entire_range && left.right_size > 0 || left.is_entire_range && right.left_size > 0:
    greatestRun = left.longest_size + right.longest_size
  else:
    greatestRun = max(right.longest_size, left.longest_size)

  result = Result(l, r, greatestRun, False)
  return result
    
  ### TODO
    pass

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


