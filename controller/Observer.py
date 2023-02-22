from model import DataFacade


async def notify(roles: list, data: dict, bot) -> None:
    users = []
    for role in roles:
        users += (await DataFacade.get_user_role(role))
        print(await DataFacade.get_user_role(role))
    users = set(users)
    pass


