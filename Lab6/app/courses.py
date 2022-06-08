from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db
from models import Course, Category, User, Review
from tools import CoursesFilter, ImageSaver

bp = Blueprint('courses', __name__, url_prefix='/courses')

PER_PAGE = 3

COURSE_PARAMS = ['author_id', 'name', 'category_id', 'short_desc', 'full_desc']
REVIEW_PARAMS = ['rating', 'text', 'course_id', 'user_id']

def params():
    return { p: request.form.get(p) for p in COURSE_PARAMS }

def search_params():
    return {
        'name': request.args.get('name'),
        'category_ids': request.args.getlist('category_ids'),
    }

def review_params():
    return { p: request.form.get(p) for p in REVIEW_PARAMS }

@bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    courses = CoursesFilter(**search_params()).perform()
    pagination = courses.paginate(page, PER_PAGE)
    courses = pagination.items
    categories = Category.query.all()
    return render_template('courses/index.html', courses=courses, categories=categories, pagination=pagination, search_params=search_params())

@bp.route('/new')
def new():
    categories = Category.query.all()
    users = User.query.all()
    return render_template('courses/new.html', categories=categories, users=users)

@bp.route('/create', methods=['POST'])
def create():
    f = request.files.get('background_img')
    if f and f.filename:
        img = ImageSaver(f).save()
    course = Course(**params(), background_image_id=img.id)
    db.session.add(course)
    db.session.commit()
    flash(f'Курс {course.name} был успешно добавлен!')
    return redirect(url_for('courses.index'))

@bp.route('/<int:course_id>')
def show(course_id):
    course = Course.query.get(course_id)
    review = Review.query.filter_by(course_id=course_id).all()
    users = User.query.all()
    return render_template('courses/show.html', course=course, review=review, users=users)

@bp.route('/<int:course_id>', methods=['POST'])
def apply_review(course_id):
    course = Course.query.filter_by(id=course_id).first()
    review = Review(**review_params())
    course.rating_sum += int(review.rating)
    course.rating_num += 1
    db.session.add(review)
    db.session.commit()
    review = Review.query.filter_by(course_id=course_id).all()
    flash('Ваш отзыв успешно записан!', 'success')
    return redirect(url_for('courses.show', course_id=course.id))

@bp.route('/<int:course_id>/reviews')
def reviews(course_id):
    review = Review.query.filter_by(course_id=course_id).all()
    users = User.query.all()
    course = Course.query.get(course_id)
    return render_template('courses/reviews.html', review=review, users=users, course=course)