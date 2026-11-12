import pandas as pd 
def filter_grades(dict,num):
  """
signature: dict,num -> strings
Explain: function takes in a dictionary of names and filters out and print names of students who have grades above the specified threshold.

>>> filter_grades({'Ruth': 13, 'Stan': 81, 'Mitch': 96, 'Matt': 61, 'Todd': 99}, 80)
'Stan'
'Mitch'
'Todd'
>>> filter_grades({'Abe': 100, 'Beth': 62, 'Cameron': 93, 'Debbie': 100}, 95)
'Abe'
'Debbie'
>>> filter_grades({'Abe': 100, 'Beth': 62, 'Cameron': 93, 'Debbie': 100}, 62)
'Abe'
'Cameron'
'Debbie'
"""
  series = pd.Series(dict)
  series1 = series[series.iloc[:] > num]
  for x in series1.index:
    print("'" + x + "'")

  


filter_grades({'Abe': 100, 'Beth': 62, 'Cameron': 93, 'Debbie': 100}, 95)
