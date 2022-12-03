from flask import Flask, render_template
from config import Config
from posts.Blueprint import posts

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(posts, url_prefix='/blog')

