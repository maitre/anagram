# test

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

word_anagrams = parse_dictionary("dict.txt")

input_word = form.Form( 
    form.Textbox("Word"), )

class index: 
    def GET(self): 
        form_word = input_word()
        return render.formtemplate(form_word)

    def POST(self): 
        form_word = input_word() 
        if not form_word.validates(): 
            return render.formtemplate(form_word)
        else:
            sorted_word = ''.join(sorted(form_word))
            print sorted_word

            return "Word : %s " % (form_word.d.Word)

if __name__ == "__main__":
    app.run()

