from subject import Observer, Subject


class InstaVIP(Subject):

    def __init__(self) -> None:
        super().__init__()
        self.observers_collection = []

    def registerObserver(self, ob: Observer):
        self.observers_collection.append(ob)

    def unregisterObserver(self, ob: Observer):
        self.observers_collection.pop()

    def notifyObservers(self):
        for observer in self.observers_collection:
            observer.update()

    def newPost(self):
        print('created a new post')
        self.notifyObservers()