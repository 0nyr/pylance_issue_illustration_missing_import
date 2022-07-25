
class TestObject:
    name: str

    def __init__(self, name: str):
        self.name = name
        self.print_name()
    
    def print_name(self):
        print("TestObject({})".format(self.name))