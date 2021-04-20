from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from .auth import login_required
from .models import Post
from .services import get_all_posts, create_post, delete_post, get_post_by_id_and_author, update_post

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    posts = get_all_posts()
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            create_post(title, body, g.user.id)
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


@bp.route('/<id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post_by_id_and_author(id, g.user.id)
    if not post:
        abort(403)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            update_post(id, title, body)
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    post = get_post_by_id_and_author(id, g.user.id)
    if not post:
        abort(403)
    delete_post(post.id)
    return redirect(url_for('blog.index'))
