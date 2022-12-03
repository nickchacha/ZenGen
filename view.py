from flask import request, render_template, flash, redirect, url_for, request, abort
from app import app


@app.route('/')
def index():
    return render_template('index.html')