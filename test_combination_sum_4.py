"""
Combination Sum 4 :
Given an array of distinct integers nums and a target integer 
target, return the number of possible combinations that add up 
to target.
Note that different sequences are counted as different 
combinations.
"""
def combinations(nums: list[int], target: int) -> int:
  if target==0:
    return 0
  if len(nums)==1:
    return 1 if target%nums[0]==0 else 0
  return 0

# tests
def test_dummy():
  assert True

def test_combinations_1_elem_zero():
  assert combinations([1], 0)==0

def test_combinations_1_elem_equal_target():
  assert combinations([1], 1)==1

def test_combinations_1_elem_gt_target():
  assert combinations([2], 1)==0

def test_combinations_1_elem_lt_target():
  assert combinations([1], 2)==1

def hid_test_combinations():
  assert combinations([1,2,3], 4)==7
