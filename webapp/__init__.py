from flask import Flask, render_template

'''
def page_not_found(error):
    return render_template('404.html'), 404'''


def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)
    from .main import create_module as main_create_module
    main_create_module(app)

    return app
