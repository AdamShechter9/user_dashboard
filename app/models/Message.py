from system.core.model import Model
import timeago, datetime

class Message(Model):
    def __init__(self):
        super(Message, self).__init__()

    def get_all_messages(self):
        # Gets latest 10 messages
        query = "SELECT messages.id, messages.contents, messages.from_user_id, messages.to_user_id, messages.updated_at, " \
                "a.firstname AS firstname, a.lastname AS lastname, b.firstname AS firstnameto, b.lastname AS lastnameto " \
                "FROM messages " \
                "JOIN users a ON messages.from_user_id = a.id " \
                "JOIN users b ON messages.to_user_id = b.id " \
                "ORDER BY messages.created_at DESC LIMIT 10 "
        all_messages = self.db.query_db(query)
        return all_messages

    def get_all_comments(self):
        # Gets all comments
        query = "SELECT comments.message_id, comments.contents, comments.user_id, comments.updated_at, " \
                "users.firstname AS firstname, users.lastname AS lastname  " \
                "FROM comments " \
                "JOIN users ON comments.user_id = users.id " \
                "JOIN messages ON comments.message_id = messages.id " \
                "ORDER BY comments.created_at ASC"
        all_comments = self.db.query_db(query)
        return all_comments

    def get_all_messages_from_user(self, user_id):
        # Get all messages from DB
        data = {
            'user_id': user_id
        }
        query = "SELECT messages.id, messages.contents, messages.from_user_id, messages.to_user_id, messages.updated_at, " \
                "users.firstname AS firstname, users.lastname AS lastname FROM messages " \
                "JOIN users ON messages.from_user_id = users.id " \
                "WHERE messages.to_user_id=:user_id " \
                "ORDER BY messages.created_at DESC"
        all_messages = self.db.query_db(query, data)
        return all_messages

    def get_all_comments_from_user(self, user_id):
        # Get all comments
        data = {
            'user_id': user_id
        }
        query = "SELECT comments.message_id, comments.contents, comments.user_id, comments.updated_at, " \
                "users.firstname AS firstname, users.lastname AS lastname FROM comments " \
                "JOIN users ON comments.user_id = users.id " \
                "JOIN messages ON comments.message_id = messages.id " \
                "WHERE messages.to_user_id=:user_id " \
                "ORDER BY comments.created_at ASC"
        all_comments = self.db.query_db(query, data)
        return all_comments

    def post_message(self, requestform):
        # store message to database.  posts to wall.
        data = {
            'contents': requestform['messagetext'],
            'from_user_id': requestform['from_user_id'],
            'to_user_id': requestform['to_user_id']
        }
        query = "INSERT INTO messages (contents, from_user_id, to_user_id, created_at, updated_at)" \
                "VALUES (:contents, :from_user_id, :to_user_id, NOW(), NOW())"
        self.db.query_db(query, data)
        return

    def post_comment(self, requestform):
        # store comments to database.  posts comment to wall.
        data = {
            'contents': requestform['commenttext'],
            'message_id': requestform['message_id'],
            'user_id': requestform['user_id']
        }
        query = "INSERT INTO comments (contents, message_id, user_id, created_at, updated_at)" \
                "VALUES (:contents, :message_id, :user_id, NOW(), NOW())"
        self.db.query_db(query, data)
        return

    def get_timeago(self, all_posts):
        now = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3.4)
        # input datetime
        for post in all_posts:
            diff_days = post['updated_at'] - now
            print diff_days
            # if diff_days
            post['updated_at'] = timeago.format(post['updated_at'], now)
        return all_posts