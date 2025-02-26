""" Utility functions for string operations"""

def upper_case(str):
  return str.upper()

def lower_case(str):
  return str.lower()

def palindrome_str(str):
  return str == str[::-1]

def reverse_str(str):
  return str[str::-1]
