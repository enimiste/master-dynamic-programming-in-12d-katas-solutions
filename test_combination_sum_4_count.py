"""
Combination Sum 4 :
Given an array of distinct integers nums and a target integer 
target, return the number of possible combinations that add up 
to target.
Note that different sequences are counted as different 
combinations.
"""
def combinations_count(nums: list[int], target: int) -> int:
  combs = combinations(nums, target)
  print(combs)
  return len(combs)

def combinations(nums: list[int], target: int) -> list[list[int]]:
  if target<=0:
    return []
  if len(nums)==1:
    return [[nums[0]]] if target%nums[0]==0 else []
  case1 = combinations([nums[0]], target)
  case2 = combinations(nums[1:], target-nums[0])
  case3 = combinations(nums, target-nums[0])
  case4 = combinations(nums[1:], target)
  return  case1 + case2 + case3 + case4
  # TODO : ignore order
# tests
def test_dummy():
  assert True

def test_combinations_1_elem_zero():
  assert combinations_count([1], 0)==0

def test_combinations_1_elem_equal_target():
  assert combinations_count([1], 1)==1

def test_combinations_1_elem_gt_target():
  assert combinations_count([2], 1)==0

def test_combinations_1_elem_lt_target():
  assert combinations_count([1], 2)==1

def test_combinations_2_elem():
  """
  (1,1,1)
  (1,2)
  (2,1)
  """
  assert combinations_count([1, 2], 3)==3

def test_combinations_2_elem_ko():
  assert combinations_count([2, 4], 5)==0

def test_combinations_2_elem_ko():
  assert combinations_count([2, 4], 5)==0

def test_combinations_3_elem_lt_target():
  """
  (1,1,1,1)
  (1,1,2)
  (1,3)
  (1,2,1)
  (3,1)
  (2,1,1)
  (2,2)
  """
  assert combinations_count([1,2,3], 4)==7

def test_combinations_1_elem_lt_target():
  assert combinations_count([1], 2)==1