
class SQLQueries:
    INSERT_USER = "INSERT INTO discord_users (username, user_id) VALUES (%s, %s) RETURNING id;"
    INSERT_EVENT = "INSERT INTO events (user_id, event_name, dice_roll) VALUES (%s, %s, %s) RETURNING id;"
    CHECK_USER = "SELECT * FROM users WHERE user_id = %s;"
    INSERT_CHARACTER = "INSERT INTO characters (user_id, username, char_name, stats) VALUES (%s, %s, %s, %s);"
