import pytest
from src.math_utils import add, sub, multp, div

def add_test():
  assert add(6,4) == 10
  assert add(-4,8) == 4

def sub_test():
  assert sub(9,3) == 6
  assert sub(4,-4) == 8

def multp_test():
  assert multp(2,5) == 10
  assert multp(7,0) == 0

def div_test():
  assert div(12,4) == 3
  assert div (6,2) == 3
  

