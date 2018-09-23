from flask import render_template

from snakeeyes.blueprints.page import page


@page.route('/')
def home():
    return render_template('home.html')


@page.route('/terms')
def terms():
    return render_template('terms.html')


@page.route('/privacy')
def privacy():
    return render_template('privacy.html')


@page.route('/faqs')
def faqs():
    return render_template('faqs.html')
