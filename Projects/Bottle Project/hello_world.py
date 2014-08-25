import bottle
from bottle import get, post, request, run, route, error, static_file, abort, redirect, response, template


@route('/login', method='GET')
def login():
    #response.charset = "ISO-8859-15"
    #return u"This will be sent with some encoding"
    return '''
    <form action="/do_login" method = "POST">
        Username: <input name ="username" type="text"/>
        Password: <input name ="password", type="text"/>
        <input value = "login" type="submit"/>
        '''

@route('/wrong_url', method="GET")
def wrong():
    redirect('/awa1')


@route('/do_login', method='POST')
def post_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        response.set_cookie('account', username, secret='some-secret-key')
        return template("<p>Welcome! {{name}} you are now logged in</p>", name=username)
    else:
        return "Login Failed"


@route('/restricted')
def restricted_area():
    username = request.get_cookie('account', secret='some-secret-key')
    if username:
        return template("Hello {{name}}!!! Welcome Back", name= username)
    else:
        return "you are not logged in... Access Denied"

@bottle.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return bottle.static_file(filename, 'template_2/images')


def check_login(username, password):
    if username and password:
        return True
    else:
        return False


run(host='localhost', port=8081, debug=True)
