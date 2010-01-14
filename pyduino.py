from juno import *

@route('/')
def index(w):
    return 'Hi there!'

run()