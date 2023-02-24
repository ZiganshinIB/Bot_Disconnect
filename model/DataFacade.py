# Фасад - паттерн, структурирующий объекты

# Предоставляет унифицированный интерфейс вместо набора интерфейсов
# некоторой подсистемы. ФАСАД определяет интерфейс более высокого уровня,
# который упрощает использование подсистемы.
from model import sqlite
import applog

log = applog.get_logger('Test')


# role
async def add_user(user_id: str, **kwargs) -> None:
    await sqlite._create_user_full_(user_id, **kwargs)
    pass


async def get_user_id(user_id:str) -> dict:
    users = await sqlite._get_user_full_(user_id)
    assert (len(users) == 1)
    return {'id': users[0][0],
            'name': users[0][1],
            'last_name': users[0][2],
            'username': users[0][3],
            'city': users[0][4],
            'company': users[0][5],
            'deportment': users[0][6],
            'position': users[0][7],
            'description': users[0][8]
            }


async def is_access(user_id: str, access_name: str) -> bool:
    return await sqlite._is_user_in_access_(user_id, access_name)


async def get_user_id_role(role: str) -> list:
    users_id = await sqlite._get_users_in_role_id(role_name=role)

    return [{'id': user_id[0]} for user_id in users_id]


async def get_users(**conditions) -> list:
    sql_users = await sqlite._get_users_and_(**conditions)
    if not (sql_users):
        raise ValueError("Ошибка не найдено")
    users = [{'id': sql_user[0],
              'name': sql_user[1],
              'last_name': sql_user[2],
              'username': sql_user[3],
              'city': sql_user[4],
              'company': sql_user[5],
              'deportment': sql_user[6],
              'position': sql_user[7],
              'description': sql_user[8]
              }
             for sql_user in sql_users]
    return users


async def get_access(access_name: str) -> dict:
    sql_accesses = await sqlite._get_access_(access_name=access_name)
    return {'access_name': sql_accesses[0][0], 'description': sql_accesses[0][1]}


async def add_user_access(user_id: str, access_name: str):
    await sqlite._create_user_access_(user_id, access_name)
