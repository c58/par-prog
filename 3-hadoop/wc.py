# -*- coding: utf-8
import hadoopy
from collections import defaultdict


class Mapper(object):
  def __init__(self):
    pass

  def map(self, key, value):
    words = value.split()
    words_len = len(words)

    for i in range(0, words_len):
      if i > words_len - 3:
        break

      first_word = words[i].lower().strip(' \t\n\r.,;:')
      after_words = []
      for j in range(i+1, i+3):
        after_words.append(words[j].lower().strip(' \t\n\r.,;:'))

      yield first_word, after_words


class Reducer(object):
  def __init__(self):
    pass

  def reduce(self, first_word, all_words_after):
    doubles = defaultdict(int)
    triples = defaultdict(int)

    for words_after in all_words_after:
      doubles[(first_word, words_after[0])] += 1
      triples[(first_word, words_after[0], words_after[1])] += 1

    for t, f3 in triples.items():
      f2 = doubles.get(t[0:2], 0)
      if f2 == 0:
        p = 0
      else:
        p = float(f3) / float(f2)
      yield t[2], (t, f3, f2, p)


if __name__ == "__main__":
  hadoopy.run(Mapper, Reducer)