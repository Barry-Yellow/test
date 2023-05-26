from TeamProject.database.base import *
from threading import Thread
from TeamProject.module.receivedMail import receive_emails
from TeamProject.module.verifyUser import init_mail


def initial(app):
    init_db(app)
    drop_all(app)
    create_all(app)
    load_file(app, 'database/class.csv')
    # init_mail()
    # with app.app_context():
    #     username, password = find_Student_account(name="WKY")
    # add_user(name="WKY", username=username, password=password)
    # email_thread = Thread(target=receive_emails,
    #                     args=("WKY",), daemon=True)
    # email_thread.start()
    init_mail()
    #init_ai()
    email_thread = Thread(target=receive_emails, daemon=True)
    email_thread.start()
