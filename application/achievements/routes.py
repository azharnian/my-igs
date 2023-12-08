from flask import Blueprint, render_template, url_for, flash, redirect
from flask_login import login_required, current_user

from application.achievements.forms import *
from application.achievements.resources import *

achievements = Blueprint('achievements', __name__)

@achievements.route('/achievements/add', methods=['GET', 'POST'])
@login_required
def add_achievements():
    form = AddAchievementForm()

    if form.validate_on_submit():
        
        new_achievement = Achievement(
            name=form.name.data,
            organizer=form.organizer.data,
            description=form.description.data,
            category_id=form.category.data,
            comp_date=form.comp_date.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            student_id=current_user.id,  
            input_by=current_user.id
        )
        db.session.add(new_achievement)
        db.session.commit()

        flash('Achievement added successfully', 'success')
        return redirect(url_for('achievements.add_achievements'))

    return render_template('pages/achievements/add_achievement.html', form=form)

@achievements.route('/achievements/update/<int:achievement_id>', methods=['GET', 'POST'])
@login_required
def update_achievement(achievement_id):
    achievement = Achievement.query.get_or_404(achievement_id)
    form = UpdateAchievementForm(obj=achievement)

    if form.validate_on_submit():
        achievement.name = form.name.data
        achievement.organizer = form.organizer.data
        achievement.description = form.description.data
        achievement.category_id = form.category.data
        achievement.comp_date = form.comp_date.data
        achievement.start_date = form.start_date.data
        achievement.end_date = form.end_date.data
        db.session.commit()

        flash('Achievement updated successfully', 'success')
        return redirect(url_for('achievements.update_achievement', achievement_id=achievement.id))

    return render_template('pages/achievements/update_achievement.html', form=form, achievement=achievement)