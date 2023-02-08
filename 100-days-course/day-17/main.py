class User:

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.followers += 1
        self.following += 1


u1 = User(1, "John")
print(u1.name)