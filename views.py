from flask import (
    Blueprint, 
    render_template, 
    request, 
    redirect, 
    url_for)
from .app import db
from .models import Comment

main = Blueprint('main', __name__)

@main.route('/')
def index():
    comments = Comment.query.all()
    return render_template('index.html', comments=comments)

@main.route('/sign', methods=['GET', 'POST'])
def sign():
    if request.method == 'POST':
        name = request.form.get('name')
        comment = request.form.get('comment')

        new_comment = Comment(name=name, comment_text=comment)
        db.session.add(new_comment)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    return render_template('sign.html')
