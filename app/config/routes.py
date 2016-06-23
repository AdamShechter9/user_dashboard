"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

# Welcome Page.
routes['default_controller'] = 'Users'
# Welcome Page.  Sign in or register links.
routes['/'] = 'Users#index'
# Sign In page.
routes['/sign_in'] = 'Users#sign_in'
# Signs in user.
routes['POST']['/users/sign_in_user'] = 'Users#sign_in_user'
# Register Page.
routes['/register'] = 'Users#register'
# Registers user in DB. signs in user at the end.
routes['POST']['/users/register_user'] = 'Users#register_user'
# Dashboard pages
routes['/dashboard/admin'] = 'Users#dashboard_admin'
routes['/dashboard'] = 'Users#dashboard'
# Add new user.  Admin only.
routes['/users/new'] = 'Users#new'
# Registers user in DB. Admin only.  no sign in.
routes['POST']['/users/new_user'] = 'Users#new_user'
# Renders edit user profile.
routes['/users/edit'] = 'Users#edit'
# Updates DB with updated user info.
routes['POST']['/users/update_info'] = 'Users#update_info'
# Updates DB with updated user info.
routes['POST']['/users/update_password'] = 'Users#update_password'
# Updates DB with updated user info.
routes['POST']['/users/update_desc'] = 'Users#update_desc'
# Edit user page.  Admin only
routes['/users/edit/<user_id>'] = 'Users#edit_admin'
# Show user profile.
routes['/users/show/<user_id>'] = 'Users#show'
# post message on a wall
routes['POST']['/users/messagepost'] = 'Users#msg_post'
# post comment on a message
routes['POST']['/users/commentpost'] = 'Users#msg_comment_post'
# Sign out user
routes['/users/sign_out_user'] = 'Users#sign_out_user'
# Delete a user from database.
routes['POST']['/users/delete'] = 'Users#delete'