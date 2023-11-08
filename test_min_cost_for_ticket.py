"""
Min cost for tickets:
You have planned some train traveling one year in advance. The 
days of the year in which you will travel are given as an integer 
array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:
- a 1-day pass is sold for costs[0] dollars,
- a 7-day pass is sold for costs[1] dollars, and
- a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel 
for 7 days: 2, 3, 4, 5, 6, 7, and 8. Return the minimum number of 
dollars you need to travel every day in the given list of days.

"""
COSTS = [2,7,15]
def min_cost_ticket(days: list[int]) -> int:
  n = len(days)
  cost = COSTS[0] * n
  if cost>COSTS[1]:
    if n<=7:
      return COSTS[1]
    else:
      return COSTS[2]
  
  return cost

# tests :
def test_dummy():
  assert True

def test_min_cost_1_day():
  assert min_cost_ticket([1])==2

def test_min_cost_2_consecutif_days():
  assert min_cost_ticket([1, 2])==4

def test_min_cost_3_consecutif_days():
  assert min_cost_ticket([1, 2, 3])==6

def test_min_cost_4_consecutif_days():
  assert min_cost_ticket([1, 2, 3, 4])==7

def test_min_cost_5_consecutif_days():
  assert min_cost_ticket([1, 2, 3, 4, 5])==7

def test_min_cost_7_consecutif_days():
  assert min_cost_ticket([1, 2, 3, 4, 5, 6, 7])==7

def test_min_cost_8_consecutif_days():
  assert min_cost_ticket([1, 2, 3, 4, 5, 6, 7, 8])==9 #7 + 2

def hid_test_min_costs():
  """
  [1,4,6,7] => 7$
  [8]       => 2$
  [20]      => 2$
  ==============
            => 11$
  """
  assert min_cost_ticket([1,4,6,7,8,20])==11



