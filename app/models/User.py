from system.core.model import Model
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def get_user_by_id(self, user_id):
        # Returns user information based on ID entered.
        query = "SELECT * FROM users WHERE id=:id"
        in_data = {
            'id': str(user_id)
        }
        user = self.db.query_db(query, in_data)
        return user[0]

    def get_user_by_email(self, user_data):
        # Returns user information based on ID entered.
        query = "SELECT * FROM users WHERE email=:email"
        in_data = {
            'email': user_data['email']
        }
        user = self.db.query_db(query, in_data)
        return user[0]

    def get_all_users(self):
        query = "SELECT * FROM users"
        all_users = self.db.query_db(query)
        return all_users

    def register_user_db(self, requestform):
        errors = []
        # Input Validation
        if len(requestform['firstname']) < 1 or len(requestform['lastname']) < 1 or len(requestform['email']) < 1 or len(requestform['password']) < 1 or len(requestform['confirmpassword']) < 1:
            # empty fields detected
            errors.append('No empty fields!')
        elif not EMAIL_REGEX.match(requestform['email']):
            # Valid email address failed
            errors.append("Invalid Email Address!")
        elif len(requestform['firstname']) < 2 or len(requestform['lastname']) < 2:
            errors.append('Names must be longer than 1 character!')
        elif len(requestform['password']) < 8:
            errors.append('Password must be at least 8 characters!')
        elif requestform['password'] != requestform['confirmpassword']:
            errors.append("Passwords don't match! Please try again.")

        if not errors:
            password_hash = self.bcrypt.generate_password_hash(requestform['password'])
            user_data = {
                'firstname': requestform['firstname'],
                'lastname': requestform['lastname'],
                'email': requestform['email'],
                'password': password_hash
            }
            # Querying the Database.  Inserting user.
            isemptyuserscheck = self.get_all_users()
            if isemptyuserscheck:
                # users database not empty
                query = "INSERT INTO users (firstname, lastname, email, password, user_level, created_at, updated_at)" \
                        "VALUES (:firstname, :lastname, :email, :password, 1, NOW(), NOW())"
            else:
                # users database empty.  make first user admin.
                query = "INSERT INTO users (firstname, lastname, email, password, user_level, created_at, updated_at)" \
                        "VALUES (:firstname, :lastname, :email, :password, 9, NOW(), NOW())"
            # Querying database.  Grabbing user info.
            user_id = self.db.query_db(query, user_data)
            user = self.get_user_by_id(user_id)
            out_data = {
                'status': True,
                'user': user
            }
            return out_data
        else:
            # Errors were detected.
            out_data = {
                'status': False,
                'errors': errors
            }
            return out_data

    def log_in_user(self, requestform):
        errors = []
        # Error validation
        if len(requestform['email']) < 1 or len(requestform['password']) < 1:
            errors.append('Email or password were left blank.')

        if not errors:
            # no errors in input entry
            user_data = {
                'email': requestform['email'],
            }
            user = self.get_user_by_email(user_data)
            if user:
                # User is found
                if self.bcrypt.check_password_hash(user['password'], requestform['password']):
                    # passwords match
                    out_data = {
                        'status': True,
                        'user': user
                    }
                    return out_data
                else:
                    # passwords don't match
                    errors.append('Passwords do not match! Try again.')
                    out_data = {
                        'status': False,
                        'errors': errors
                    }
                    return out_data
            else:
                # User is not found
                errors.append('Username not found! retry with a different name or register.')
                out_data = {
                    'status': False,
                    'errors': errors
                }
                return out_data
        else:
            # errors in input entry
            out_data = {
                'status': False,
                'errors': errors
            }
            return out_data

    def update_user(self, requestform, update_route):
        errors = []
        if update_route == 'info':
            # 'INFO SUBMIT'
            # Input Validation
            if len(requestform['firstname']) < 1 or len(requestform['lastname']) < 1 or len(requestform['email']) < 1:
                # empty fields detected
                errors.append('No empty fields!')
            elif not EMAIL_REGEX.match(requestform['email']):
                # Valid email address failed
                errors.append("Invalid Email Address!")
            elif len(requestform['firstname']) < 2 or len(requestform['lastname']) < 2:
                errors.append('Names must be longer than 1 character!')
            if not errors:
                if requestform['user_level']:
                    query = "UPDATE users SET firstname=:firstname, lastname=:lastname, email=:email, " \
                            "user_level=:user_level, updated_at=NOW()" \
                            "WHERE id=:id"
                    data = {
                        'firstname': requestform['firstname'],
                        'lastname': requestform['lastname'],
                        'email': requestform['email'],
                        'id': requestform['user_id'],
                        'user_level': requestform['user_level']
                    }
                else:
                    query = "UPDATE users SET firstname=:firstname, lastname=:lastname, email=:email, updated_at=NOW()" \
                            "WHERE id=:id"
                    data = {
                        'firstname': requestform['firstname'],
                        'lastname': requestform['lastname'],
                        'email': requestform['email'],
                        'id': requestform['user_id'],
                    }
        if update_route == 'password':
            # 'PASSWORD SUBMIT'
            # Input Validation
            if len(requestform['password']) < 8:
                errors.append('Password must be at least 8 characters!')
            elif requestform['password'] != requestform['confirmpassword']:
                errors.append("Passwords don't match! Please try again.")
            if not errors:
                password_hash = self.bcrypt.generate_password_hash(requestform['password'])
                query = "UPDATE users SET password=:password, updated_at=NOW()" \
                        "WHERE id=:id"
                data = {
                    'password': password_hash,
                    'id': requestform['user_id'],
                }
        if update_route == 'desc':
            # 'DESCRIPTION SUBMIT'
            # Input Validation
            if len(requestform['description']) < 1:
                errors.append("Description field is empty!")
            if not errors:
                query = "UPDATE users SET description=:description, updated_at=NOW()" \
                        "WHERE id=:id"
                data = {
                    'description': requestform['description'],
                    'id': requestform['user_id'],
                }
        if not errors:
            self.db.query_db(query, data)
            return {'status': True, 'user_id': requestform['user_id']}
        else:
            # errors in input entry
            out_data = {
                'status': False,
                'errors': errors
            }
            return out_data

    def delete_user(self, requestform):
        data = {
            'id': requestform['id']
        }
        query = "DELETE FROM users WHERE id=:id"
        self.db.query_db(query, data)
        return
