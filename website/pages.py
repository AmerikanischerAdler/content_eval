from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from .models import db, Eval

pages = Blueprint("pages", __name__)

@pages.route('/')
@pages.route('/home')
def home():
    return render_template('index.html')

@pages.route('/sub_form', methods=['POST'])
def sub_form():
    data = request.get_json()

    isMovie = int(request.form.get("isMovie", 0))
    isYT = int(request.form.get("isYT", 0))
    isBook = int(request.form.get("isBook", 0))
    isOther = int(request.form.get("isOther", 0))
    ctype = data.get('type', '')

    title = data.get('title', '')
    description = data.get('description', '')

    reflect = data.get('reflect', '')
    love = data.get('love', '')
    hate = data.get('hate', '')
    lesson = data.get('lesson', '')

    insights = data.get('insights', '')
    changes = data.get('change', '')

    new_eval = Eval(
        isMovie=isMovie,
        isYT=isYT,
        isBook=isBook,
        isOther=isOther,
        types=ctype,
        title=title,
        description=description,
        reflect=reflect,
        love=love,
        hate=hate,
        lesson=lesson,
        insights=insights,
        changes=changes,
    )

    db.session.add(new_eval)
    db.session.commit()

    return jsonify({'message': 'Content Evaluation Submitted Successfully!', 'data': data}), 200

