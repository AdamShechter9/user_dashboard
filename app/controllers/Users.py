from system.core.controller import *

# To Do:
# Implement "time ago" function

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Message')
        self.db = self._app.db

    def index(self):
        # Render welcome page
        return self.load_view('index.html')

    def register(self):
        # Renders Register page.
        return self.load_view('register.html')

    def register_user(self):
        # Registers a new user.
        # grab request.form information
        requestform = request.form
        # Adds new user to database.
        reg_status = self.models['User'].register_user_db(requestform)
        if reg_status['status']:
            # Signs in.
            session['user'] = reg_status['user']['id']
            session['name'] = reg_status['user']['firstname']
            session['admin'] = reg_status['user']['user_level'] == str(9)
            return redirect('/dashboard')
        else:
            # Fail Register/Sign in.
            for error in reg_status['errors']:
                flash(error)
            return redirect('/register')

    def sign_in(self):
        # Renders sign in page
        return self.load_view('sign_in.html')

    def sign_in_user(self):
        # Signs in user to session.
        # grab request.form information
        requestform = request.form
        # Signs in
        login_status = self.models['User'].log_in_user(requestform)
        if login_status['status']:
            # Signs in.
            session['user'] = login_status['user']['id']
            session['name'] = login_status['user']['firstname']
            session['admin'] = int(login_status['user']['user_level']) == 9
            if session['admin']:
                return redirect('/dashboard/admin')
            else:
                return redirect('/dashboard')
        else:
            # Fail sign in.
            for error in login_status['errors']:
                flash(error)
            return redirect('/sign_in')

    def dashboard_admin(self):
        # admin check
        # Render Admin Dashboard
        all_users = self.models['User'].get_all_users()
        all_messages = self.models['Message'].get_all_messages()
        all_messages = self.models['Message'].get_timeago(all_messages)
        all_comments = self.models['Message'].get_all_comments()
        all_comments = self.models['Message'].get_timeago(all_comments)
        return self.load_view('dashboard.html', admin=session['admin'], all_users=all_users, all_messages=all_messages, all_comments=all_comments)

    def dashboard(self):
        # Render Dashboard
        all_users = self.models['User'].get_all_users()
        all_messages = self.models['Message'].get_all_messages()
        all_messages = self.models['Message'].get_timeago(all_messages)
        all_comments = self.models['Message'].get_all_comments()
        all_comments = self.models['Message'].get_timeago(all_comments)
        return self.load_view('dashboard.html', admin=session['admin'], all_users=all_users, all_messages=all_messages, all_comments=all_comments)

    def new(self):
        # Admin check
        # Renders new user page.
        if session['admin']:
            return self.load_view('new_user.html')
        else:
            return redirect('/dashboard')

    def new_user(self):
        # grab request.form information
        # adds to database
        requestform = request.form
        # Adds new user to database.
        new_status = self.models['User'].register_user_db(requestform)
        if new_status['status']:
            return redirect('/dashboard/admin')
        else:
            # Fail validation
            for error in new_status['errors']:
                flash(error)
            return redirect('/users/new')

    def edit(self):
        # Renders User Profile edit page.
        # grab user information from database
        user = self.models['User'].get_user_by_id(session['user'])
        return self.load_view('edit_user.html', user=user, admin=False)

    def edit_admin(self, user_id):
        # admin check
        if session['admin']:
            user = self.models['User'].get_user_by_id(user_id)
            return self.load_view('edit_user.html', admin=session['admin'], user=user)
        else:
            return redirect('/dashboard')

    def update_info(self):
        # Updates DB with user info.
        requestform = request.form
        update_route = "info"
        update_status = self.models['User'].update_user(requestform, update_route)

        if update_status['status']:
            return redirect('/users/show/'+str(update_status['user_id']))
        else:
            if session['admin']:
                return redirect('/users/edit/'+str(requestform['user_id']))
            else:
                return redirect('/users/edit')

    def update_password(self):
        # Updates DB with user info.
        requestform = request.form
        update_route = "password"
        update_status = self.models['User'].update_user(requestform, update_route)
        if update_status['status']:
            return redirect('/users/show/'+str(update_status['user_id']))
        else:
            if session['admin']:
                return redirect('/users/edit/'+str(requestform['user_id']))
            else:
                return redirect('/users/edit')

    def update_desc(self):
        # Updates DB with user info.
        requestform = request.form
        update_route = "desc"
        update_status = self.models['User'].update_user(requestform, update_route)
        if update_status['status']:
            return redirect('/users/show/'+str(update_status['user_id']))
        else:
            if session['admin']:
                return redirect('/users/edit/'+str(requestform['user_id']))
            else:
                return redirect('/users/edit')

    def show(self, user_id):
        # Show user profile.
        # Passes in user info
        user = self.models['User'].get_user_by_id(user_id)
        # Passes in all_messages
        all_messages = self.models['Message'].get_all_messages_from_user(user_id)
        # Passes in all comments for message
        all_messages = self.models['Message'].get_timeago(all_messages)
        all_comments = self.models['Message'].get_all_comments_from_user(user_id)
        all_comments = self.models['Message'].get_timeago(all_comments)
        return self.load_view('show_user.html', admin=session['admin'], user=user, all_messages=all_messages, all_comments=all_comments)

    def msg_post(self):
        # posts a message on a users wall
        requestform = request.form
        self.models['Message'].post_message(requestform)
        return redirect('/users/show/'+str(requestform['to_user_id']))

    def msg_comment_post(self):
        # posts a comment on a messaage
        requestform = request.form
        print "request form\n", requestform, '\n\n'
        self.models['Message'].post_comment(requestform)
        return redirect('/users/show/' + str(requestform['to_user_id']))

    def sign_out_user(self):
        # Sign out User from session.
        session.clear()
        return redirect('/')

    def delete(self):
        # deletes a user from the database.
        requestform = request.form
        self.models['User'].delete_user(requestform)
        return redirect('/dashboard/admin')
