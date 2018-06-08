import data_manager
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mentor-2-names')
def mentor_2_names():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_2_names = data_manager.get_mentor_2_names()
    return render_template('mentor_names.html', mentor_2_names=mentor_2_names)


@app.route('/mentor_nick_names')
def mentor_nick_names():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_nick_names = data_manager.get_mentor_nick_names()
    return render_template('mentor_nick_names.html', mentor_nick_names=mentor_nick_names)


@app.route('/find_CAROL')
def find_CAROL():
    # We get back dictionaries here (for details check 'database_common.py')
    find_CAROL = data_manager.get_find_CAROL()
    return render_template('find_CAROL.html', find_CAROL=find_CAROL)


@app.route('/find_her_by_email')
def find_her_by_email():
    # We get back dictionaries here (for details check 'database_common.py')
    find_her_by_email = data_manager.get_find_her_by_email()
    return render_template('find_her_by_email.html', find_her_by_email=find_her_by_email)

@app.route('/add_new_applicant')
def add_new_applicant():
    # We get back dictionaries here (for details check 'database_common.py')
    add_new_applicant = data_manager.get_add_new_applicant()
    return render_template('add_new_applicant_Markus.html', add_new_applicant=add_new_applicant)

@app.route('/update_Jemima_Foremanadd')
def update_Jemima_Foremanadd():
    # We get back dictionaries here (for details check 'database_common.py')
    update_Jemima_Foremanadd = data_manager.get_update_Jemima_Foremanadd()
    return render_template('update_Jemima_Foremanadd.html', update_Jemima_Foremanadd=update_Jemima_Foremanadd)

@app.route('/delete_applicant_by_email')
def delete_applicant_by_email():
    # We get back dictionaries here (for details check 'database_common.py')
    delete_applicant_by_email = data_manager.get_delete_applicant_by_email()
    return render_template('delete_applicant_by_email.html')

@app.route('/show_mentor_table')
def show_mentor_table():
    # We get back dictionaries here (for details check 'database_common.py')
    show_mentor_table = data_manager.get_show_mentor_table()
    return render_template('show_mentors_table.html',show_mentor_table=show_mentor_table)    

@app.route('/show_applicant_table')
def show_applicant_table():
    # We get back dictionaries here (for details check 'database_common.py')
    show_applicant_table = data_manager.get_show_applicant_table()
    return render_template('show_applicants_table.html', show_applicant_table=show_applicant_table)

@app.route('/mentors')
def mentors():
    # We get back dictionaries here (for details check 'database_common.py')
    mentors = data_manager.get_mentors()
    return render_template('mentors.html', mentors=mentors)



if __name__ == '__main__':
    app.run(debug=True)