from dataclasses import dataclass
from http.client import HTTPResponse


@dataclass
class User:
    id: int
    username: str
    password: str

    # def log(self):
    #     print(self.username)
    #
    # def send(self):
    #     return HTTPResponse(self)

    # def save_to_db(self):
    #     pass


class UserLogger:
    def log(self, user: User):
        print(user)


class UserController:
    def send(self, user: User):
        print(f'Объект {user} - отправлен')


class UserRepository:
    def save(self, user: User):
        print(f'Объект {user} - сохранен')


user = User(1, 'user1', 'pass')

logger = UserLogger()
logger.log(user)

controller = UserController()
controller.send(user)

repository = UserRepository()
repository.save(user)
