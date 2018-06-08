import database_common


@database_common.connection_handler
def get_mentor_names_by_first_name(cursor, first_name):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    WHERE first_name = %(first_name)s ORDER BY first_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names

#TASK 1: 2 mentors names
@database_common.connection_handler
def get_mentor_2_names(cursor):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    ORDER BY last_name;
                   """
                   )
    names = cursor.fetchall()
    return names

#TASK 2: mentor nick names
@database_common.connection_handler
def get_mentor_nick_names(cursor):
    cursor.execute("""
                    SELECT nick_name, first_name, last_name FROM mentors
                    ORDER BY nick_name;
                   """
                   )
    names = cursor.fetchall()
    return names

#TASK 3: find CAROL + her phone
@database_common.connection_handler
def get_find_CAROL(cursor):
    cursor.execute("""
                    SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number 
                    FROM applicants
                    WHERE first_name = 'Carol';
                   """
                   )
    names = cursor.fetchall()
    return names

#TASK 4: find her by email
@database_common.connection_handler
def get_find_her_by_email(cursor):
    cursor.execute("""
                    SELECT CONCAT (first_name, ' ', last_name) AS full_name, phone_number 
                    FROM applicants
                    WHERE email LIKE '%@adipiscingenimmi.edu';
                   """
                   )
    names = cursor.fetchall()
    return names

#TASK 5: add new applicant
@database_common.connection_handler
def get_add_new_applicant(cursor):
    cursor.execute("""
                    INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                    VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823)
                    ON CONFLICT DO NOTHING;
                                      
                    SELECT * FROM applicants 
                    WHERE last_name = 'Schaffarzyk';               
                   """
                    )
    names = cursor.fetchall()
    return names

#TASK 6: update Jemima Foreman's phone number
@database_common.connection_handler
def get_update_Jemima_Foremanadd(cursor):
    cursor.execute("""
                    UPDATE applicants
                    SET phone_number =  '003670/223-7459'
                    WHERE first_name = 'Jemima' AND last_name = 'Foreman';
                                      
                    SELECT * FROM applicants 
                    WHERE first_name = 'Jemima' AND last_name = 'Foreman';               
                   """
                    )
    names = cursor.fetchall()
    return names

#TASK 7: update Jemima Foreman's phone number
@database_common.connection_handler
def get_delete_applicant_by_email(cursor):
    cursor.execute("""
                    DELETE FROM applicants 
                    WHERE email LIKE '%mauriseu.net';              
                   """
                    )
    pass

#Additional: show mentor table
@database_common.connection_handler
def get_show_mentor_table(cursor):
    cursor.execute("""
                    SELECT * FROM mentors;
                   """
                    )
    names = cursor.fetchall()
    return names

#Additional: show applicant table
@database_common.connection_handler
def get_show_applicant_table(cursor):
    cursor.execute("""
                    SELECT * FROM applicants
                   """
                    )
    names = cursor.fetchall()
    return names

#TASK 1 PART2: mentors
@database_common.connection_handler
def get_mentors(cursor):
    cursor.execute("""
                    SELECT mentors.first_name, mentors.last_name, schools.name AS school_name, schools.country FROM mentors
                    INNER JOIN schools
                    ON mentors.city = schools.city
                    ORDER BY mentors.id
                    ;
                   """
                   )
    names = cursor.fetchall()
    return names

#TASK 2 PART2: all-school
@database_common.connection_handler
def get_all_school(cursor):
    cursor.execute("""
                    SELECT COALESCE(mentors.first_name,'No data') AS first_name, COALESCE(mentors.last_name,'No data') AS last_name, schools.name AS school_name, schools.country FROM mentors
                    RIGHT JOIN schools
                    ON mentors.city = schools.city
                    ORDER BY mentors.id
                    ;
                   """
                   )
    names = cursor.fetchall()
    return names
