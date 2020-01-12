from user import User

users = [
    User(1, 'u1', 'mypass'),
    User(2, 'u2', 'pass2')
]

# Maps username to the User
username_table = {u.username: u for u in users}
# Mapss user's id to the User
userid_table = {u.id: u for u in users}

# Returns user instance


def authenticate(username, password):
    user = username_table.get(username, None)  # return None if not found
    if user and password == user.password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
