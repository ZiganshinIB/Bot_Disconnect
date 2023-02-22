# Фасад - паттерн, структурирующий объекты

# Предоставляет унифицированный интерфейс вместо набора интерфейсов
# некоторой подсистемы. ФАСАД определяет интерфейс более высокого уровня,
# который упрощает использование подсистемы.


# role
async def add_user(user_id: str, **kwargs):
    print(kwargs)
    pass


async def get_user(user_id):
    pass


async def is_access(access_name: str, user_id) -> bool:
    pass


async def get_user_role(role: str) -> list:
    return ['1']
