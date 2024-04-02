# class DataFetcher:
#
#     def get(self, url: str): pass
#
#     def post(self): pass
#
#     def put(self): pass
#
#     def delete(self): pass
#
#     def get_user(self, id: int):
#         self.get('http://example.com/' + str(id))
#         print('http://example.com/' + str(id))
#
#     def get_requisites(self, id: int):
#         self.get('http://example.com/requisites/' + str(id))
#         print('http://example.com/' + str(id))
#
#     def get_clients(self):
#         self.get('http://example.com/')
#         print('http://example.com/clients/')


class HttpClient:
    def get(self, url: str): pass
    def post(self): pass
    def put(self): pass
    def delete(self): pass


class UserService:
    client: HttpClient

    def __init__(self, client: HttpClient):
        self.client = client

    def get_one_user(self, id: int):
        print('http://example.com/' + str(id))

    def get_all_user(self):
        print('http://example.com/users/')


class RequisitesService:
    def create_requisites(self): pass

    def get_requisites(self): pass

    def update_requisites(self): pass


client = HttpClient()

client.get_user(5)
client.get_requisites(5)
client.get_clients()