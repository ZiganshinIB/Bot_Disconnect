import sqlite3 as sq


async def db_start():
    global db, cur

    db = sq.connect("test.db")
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, name TEXT , gender TEXT, description TEXT)")

    db.commit()


async def create_profile(user_id):
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchall()
    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ?, ?, ?)",(user_id, '', '', ""))
        db.commit()


async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute("UPDATE profile SET name = '{}', description= '{}', gender='{}' WHERE user_id == '{}'".format(
            data['name'], data['description'], data['gender'], user_id
        ))
        db.commit()