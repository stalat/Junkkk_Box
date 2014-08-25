import time
from bottle import route, run, static_file, request,redirect

@route('/')
def home():
    return static_file('login.html', root='template_2/')

@route('/error')
def error():
    return "Sorry! The page requested by you is under processing or doesn't exist"


@route('/wrong_page')
def wrong_url():
    time.sleep(3)
    redirect('/')


@route('/do_login', method="post")
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if check_login(username, password):
        return static_file('index.html', root='template_2/')
    else:
        return wrong_url()


@route('/check_login')
def check_login(username, password):
    if username and password:
        return True
    else:
        return False


@route('/<filename:re:.*\.(jpg|png|gif|ico)>', method="GET")
def images(filename):
    return static_file(filename, root='template_2/images/')


@route('/<filename:re:.*\.css')
def stylesheets(filename):
    return static_file(filename, root='template_2/css/')


@route('<filename:re:.*\.html>')
def html(filename):
    return static_file(filename, root='template_2/')


@route('<filename:re:.*\.js>')
def javascript(filename):
    return static_file(filename, root='template_2/js/')


run(host='localhost', port=8082, debug=True)

