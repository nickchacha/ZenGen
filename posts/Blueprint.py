from flask import  Blueprint, template_rendered, render_template

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def post_list():
    return render_template('posts/posts.html')
