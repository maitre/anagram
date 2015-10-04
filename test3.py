## test 3

from collections import defaultdict

try:
   input = raw_input
except NameError:
   pass

def parse_dictionary(filename):
   word_anagrams = defaultdict(set)

   with open(filename) as dictionary:
      for word in dictionary:
         word = word.rstrip()

         word_anagrams[''.join(sorted(word))].add(word)

   return word_anagrams

def main():
   word_anagrams = parse_dictionary("dict.txt")

   scrambled_word = input("Input scrambled word: ")
   sorted_word = ''.join(sorted(scrambled_word))

   anagram_list=set()
   if word_anagrams[sorted_word]:
      for word in word_anagrams[sorted_word]:
         anagram_list.add(word)

   else:
      anagram_list.add("No anagrams found")

   print format(anagram_list)

if __name__ == "__main__":
   main()

