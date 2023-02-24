import sqlite3 as sq

import applog

log = applog.get_logger('Test')


async def _db_start_():
    global db, cur
    db = sq.connect("test.db")
    cur = db.cursor()
    db.commit()


async def _create_user_full_(user_id: str, name: str, last_name: str, username:str, city: object, company: object, deportment: object, position: object, description: object) -> None:
    user = cur.execute("SELECT 1 FROM user WHERE user_id == '{key}'".format(key=user_id)).fetchall()
    if not user:
        cur.execute("""INSERT INTO user (user_id, name, last_name,city,company, deportment, position, description)
        VALUES (?, ?, ?, ?,  ?, ?, ?, ?, ?)""",
                    (user_id, name, last_name, username, city, company, deportment, position, description))
        db.commit()


async def _create_user_access_(user_id: str, access_name: str):
    if not await _is_user_in_access_(user_id=user_id, access_name=access_name):
        cur.execute("""INSERT INTO user_access (user_id, access_name) VALUES (?, ?)""",
                    (user_id, access_name))
        db.commit()


async def _create_user_role_(user_id: str, role_name: str):
    if not await _is_user_in_role_(user_id=user_id, role_name=role_name):
        cur.execute("""INSERT INTO user_role (user_id, role_name) 
                VALUES (?, ?,)""",
                    (user_id, role_name))
        db.commit()


async def _get_user_of_id_full_(user_id: str,) -> list:
    user = cur.execute("SELECT * FROM user WHERE user_id == '{key}'".format(key=user_id)).fetchall()
    if not user:
        raise ValueError(f"Нет пользователя с {user_id}")
    return user


async def _get_user_of_username_full_(username: str,) -> list:
    user = cur.execute("SELECT * FROM user WHERE username == '{key}'".format(key=username)).fetchall()
    if not user:
        raise ValueError(f"Нет пользователя {username}")
    return user


async def _get_user_full_(data: dict,) -> list:
    user = cur.execute(f"SELECT * FROM user WHERE {list(data.items())[0][0]} == '{list(data.items())[0][1]}'").fetchall()
    if not user:
        raise ValueError(f"Нет пользователя с {list(data.items())[0][0]}: {list(data.items())[0][1]}")
    return user


async def _get_users_and_(**conditions) -> list:
    queri = f"SELECT * FROM user"
    if conditions:
        queri = queri + f" WHERE"
        count = 0
        for condition in conditions:
            if count > 0:
                queri = queri + " AND"
            count_ = 0
            for math in conditions[condition]:
                if count_ > 0:
                    queri = queri + " OR"
                queri = queri + f" {condition} == '{math}'"
                count_ += 1
            count += 1
    return cur.execute(queri).fetchall()


async def _get_users_or_(**conditions) -> list:
    queri = f"SELECT * FROM user"
    if conditions:
        queri = queri + f" WHERE"
        count = 0
        for condition in conditions:
            if count > 0:
                queri = queri + " OR"
            count_ = 0
            for math in conditions[condition]:
                if count_ > 0:
                    queri = queri + " OR"
                queri = queri + f" {condition} == '{math}'"
                count_ += 1
            count += 1
    return cur.execute(queri).fetchall()


async def _get_users_in_role_id(role_name) -> list:
    users = cur.execute("SELECT user_id FROM user_role WHERE role_name == '{key}'".format(key=role_name)).fetchall()
    if not users:
        raise ValueError(f"Нет информации про эти роли {role_name}")
    return users


async def _get_users_in_access_id(access_name) -> list:
    users = cur.execute("SELECT user_id FROM user_access WHERE access_name == '{key}'".format(key=access_name)).fetchall()
    if not users:
        raise ValueError(f"Нет информации про этот {access_name} доступ")
    return users


async def _get_access_(access_name) -> list:
    access = cur.execute(
        f"SELECT * FROM access WHERE access_name == '{access_name}'").fetchall()
    if not access:
        raise ValueError(f"Доступ {access_name} не найден")
    return access


async def _is_user_in_access_(user_id: str, access_name: str) -> bool:
    access = cur.execute(f"SELECT * FROM user_access WHERE (user_id == '{user_id}' AND access_name=='{access_name}')").fetchall()
    return not(not (access))


async def _is_user_in_role_(user_id: str, role_name: str) -> bool:
    access = cur.execute(f"SELECT * FROM user_role WHERE user_id == '{user_id}' AND role_name=='{role_name}'")
    return not (not access)


async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute("UPDATE profile SET name = '{}', description= '{}', gender='{}' WHERE user_id == '{}'".format(
            data['name'], data['description'], data['gender'], user_id
        ))
        db.commit()