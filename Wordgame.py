"""Write a class called Wordgame. It should have a field that holds a list of words. The user of this class should pass the list of words they want to use
to the class. There should be the following methods:
    •   words_length(len) – returns a list of all the words of length 
    •	startswith(a) – returns a list of all words of that start with a
    •	endswith(s) – returns a list of all the words that end with s
    •	palindromes() — returns a list of all the palindromes in the list 
    •	only(h)-returns a list of the words that contain only those letters in h
    •	avoids(h) — returns a list of the words that contain none of the letters in h """



class Wordgame:
  def __init__(self, words):
    self.words = list(words)

  def words_length(self, length):
    result = list(filter(lambda x: len(x) == length, self.words))
    return result

  def starts_with(self, letter):
    result = list(filter(lambda x: x.startswith(letter), self.words))
    return result

  def ends_with(self, letter):
    result = list(filter(lambda x: x.endswith(letter), self.words))
    return result

  def palindromes(self):
    result = list(filter(lambda x: x == x[::-1], self.words))
    return result

  def only(self, letter):
    word_list = []
    for word in self.words:
      for i in word:
        if i == letter:
          word_list.append(word)
    return word_list
  
  def avoid(self, letter):
    avoid_list = []
    for word in self.words:
      if letter not in word:
        avoid_list.append(word)
    return avoid_list
    
# Using the class by assigning it to a variable
some = Wordgame(['ask', 'butter', 'man', 'esc', 'breathe', 'pop', 'mom'])

#Giving arguments
print(some.words_length(6))
print(some.starts_with('b'))
print(some.ends_with('k'))
print(some.palindromes())
print(some.only('b'))
print(some.avoid('a'))
