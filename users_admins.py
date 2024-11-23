
class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__users_list = []

    def add_user(self, user):
        if isinstance(user, User):
            self.__users_list.append(user)
            print(f'Пользователь {user.get_name()} добавлен.')

    def remove_user(self, user):
        if user in self.__users_list:
            self.__users_list.remove(user)
            print(f'Пользователь {user.get_name()} удален.')
        else:
            print("Ошибка: Пользователь не найден в системе.")

    def get_users(self):
        for user in self.__users_list:
            print(f'ID: {user.get_user_id()}, Имя: {user.get_name()}, '
                  f'Уровень доступа: {user.get_access_level()}')


user1 = User(user_id=1, name="Иван Иванов")
user2 = User(user_id=2, name="Петр Петров")
admin = Admin(user_id=3, name="Светлана Светлова")
admin.add_user(user1)
admin.add_user(user2)
admin.get_users()

admin.remove_user(user1)
admin.get_users()