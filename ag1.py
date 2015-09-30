## $Id$
## web.py app to output anagrams

from collections import defaultdict
import web
from web import form

try:
   input = raw_input
except NameError:
   pass

def parse_dictionary(filename):
   dict_anagrams = defaultdict(set)

   with open(filename) as dictionary:
      for word in dictionary:
         word = word.rstrip()
         dict_anagrams[''.join(sorted(word))].add(word)

   return dict_anagrams

urls = ('/', 'index')
app = web.application(urls, globals())
render = web.template.render('tmpl/')

input_word = form.Form( 
    form.Textbox("Word"), )

word_anagrams = parse_dictionary("dict.txt")

class index: 
    def GET(self): 
        form_word = input_word()
        return render.formtemplate(form_word)

    def POST(self): 
        form_word = input_word() 

        if not form_word.validates(): 
            return render.formtemplate(form_word)

        else:
            sorted_word = 'dog'
            anagram_list=set()
            anagram_list.add("cat")

            print sorted_word
            print anagram_list

            sorted_word = ''.join(sorted(form_word.d.Word))

            if word_anagrams[sorted_word]:
                for word in word_anagrams[sorted_word]:
                    ## print("Possible Word for Scrambled Word: {}".form_wordat(word))
                    anagram_list.add(word)

            else:
                anagram_list.add("No anagrams found.")

            return(anagram_list)

            ## return "Results : %s " % (form_word.d.Word)

if __name__ == "__main__":
    app.run()

