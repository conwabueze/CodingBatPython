"""
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
"""

def not_string(str):
  if len(str)>2:
    if str[0:3] != "not":
      return "not " + str
    else:
      return str
  else:
    return "not " + str