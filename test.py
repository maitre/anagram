# test
import web
from web import form

urls = ('/', 'index')
app = web.application(urls, globals())

render = web.template.render('tmpl/')

myform = form.Form( 
    form.Textbox("Word"), )

class index: 
    def GET(self): 
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.formtemplate(form)

    def POST(self): 
        form = myform() 
        if not form.validates(): 
            return render.formtemplate(form)
        else:
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
            return "Word : %s " % (form.d.Word)

if __name__ == "__main__":
    app.run()

