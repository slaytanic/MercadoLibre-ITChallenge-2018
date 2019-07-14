import re 

def multiple_replace(dict, text):
  # Create a regular expression  from the dictionary keys
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text) 

if __name__ == "__main__": 

  n = 3
  n = 234612846789231
  m = 123456789
  adn = 'A'

  # text = "Larry Wall is the creator of Perl"

  dict = {
    # "Larry Wall" : "Guido van Rossum",
    # "creator" : "Benevolent Dictator for Life",
    # "Perl" : "Python",
    'A': 'AL',
    'L': 'PACA',
    'P': 'CP',
    'C': 'PC'
  } 

  for i in range(n):
    print(i)
    adn = multiple_replace(dict, adn)

  d = adn.count('ALPACA')

  print(adn)
  print(d)
  print(d % m)