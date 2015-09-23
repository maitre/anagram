# test
import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        print "Enter a word."

        formword = form.Form(
            form.Textbox('Word'),
            form.Button('Submit')
        )

        f = formword()
        print f.render()

        return "Complete."

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

