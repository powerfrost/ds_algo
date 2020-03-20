"""
A game where you try to form the longest word possible.
AUTORUN: http://trie1.xavierchia.repl.run/
REPL.IT: https://repl.it/@xavierchia/Trie1
"""


class Trie:

  def __init__(self):
    self.root = {"*":"*"}
    self.high_score = 0



  def add_word(self, word):
    curr_node = self.root
    for letter in word:
      if letter not in curr_node:
        curr_node[letter] = {}
      curr_node = curr_node[letter]
    curr_node['*'] = '*'

  # def does_word_exist(self, word):
  #   curr_node = self.root
  #   for letter in word:
  #     if letter not in curr_node:
  #       return False
  #     curr_node = curr_node[letter]
  #   return '*' in curr_node

  def does_prefix_exist(self, prefix):

    curr_node = self.root
    for letter in prefix:
      if letter not in curr_node:
        return False
      curr_node = curr_node[letter]
    return True




  def play(self, prefix):
    print("\n" + "'" + prefix.upper() + "'" + " is a " + str(len(prefix)) + " letter word or prefix. Can you make it longer?" )
    letter = input("Enter the NEXT letter: ").lower()

    while len(letter) != 1:
      letter = input("Enter only ONE letter: ")

    prefix = prefix.lower() + letter.lower()

    if self.does_prefix_exist(prefix):
      self.play(prefix)

    else:
      self.high_score = max(self.high_score, len(prefix)-1)
      answer = input("\n" + "That's not a word :)" + "\n" + "Your high score is: " + str(self.high_score) + "\n" + "Play again? Y/N: ").lower()

      if answer == "y":
        self.play("HOP")
      else:
        print("It was fun playing together :)")


trie = Trie()

trie.add_word('hope')
trie.add_word('hops')
trie.add_word('hoppy')
trie.add_word('hoped')
trie.add_word('hoper')
trie.add_word('hopers')
trie.add_word('hopper')
trie.add_word('hopple')
trie.add_word('hopped')
trie.add_word('hoping')
trie.add_word('hopers')
trie.add_word('hopeful')
trie.add_word('hoplite')
trie.add_word('hophead')
trie.add_word('hoppers')
trie.add_word('hoppier')
trie.add_word('hopping')
trie.add_word('hoppled')
trie.add_word('hopples')
trie.add_word('hopsack')
trie.add_word('hoptoad')
trie.add_word('hopeless')
trie.add_word('hopefuls')
trie.add_word('hopheads')
trie.add_word('hoppingly')
trie.add_word('hoplites')
trie.add_word('hoplitic')
trie.add_word('hoppling')
trie.add_word('hoppings')
trie.add_word('hoppiest')
trie.add_word('hopsacks')
trie.add_word('hoptoads')
trie.add_word('hopefully')
trie.add_word('hopscotch')
trie.add_word('hopsacking')
trie.add_word('hopelessly')
trie.add_word('hopefulness')
trie.add_word('hopsackings')
trie.add_word('hopscotched')
trie.add_word('hopscotches')
trie.add_word('hoplessness')
trie.add_word('hopscotching')
trie.add_word('hopfulnesses')
trie.add_word('hoplessnesses')

print("Try to form the longest word possible")

if __name__ == "__main__":
  trie.play("HOP")
