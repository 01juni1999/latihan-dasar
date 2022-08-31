from flask import Flask
app = Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return "render_temperetur"('hello.html', name=None)

'<!doctype html>'
'<title>Hello from Flask</title>'
'{ ifname}'
'<h1>Hello {{ name }}!</h1>'
'{% else %}'
'<h1>Hello, World!</h1>'
'{% endif %}'


from markupsafe import Markup
Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
(u'<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
Markup.escape('<blink>hacker</blink>')
Markup(u'&lt;blink&gt;hacker&lt;/blink&gt;')
Markup('<em>Marked up</em> &raquo; HTML').striptags()
u'Marked up \xbb HTML'

if __name__ =="__main__":
    app.run()
