from subject import Observer


class Follower(Observer):

    def __init__(self, username) -> None:
        super().__init__()
        self.username = username

    def update(self):
        print(f'notification for {self.username} : new post created by Ronaldo')