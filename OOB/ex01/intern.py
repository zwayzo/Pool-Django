class intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name"):
        self.name = name

    # def builder(self, name):
    #     self.name = name
    
    def __str__(self):
        return self.name
    
    class coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted"
        
    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")
    
    def make_coffee(self):
        return self.__class__.coffee()
    

if __name__ == "__main__":
    name = intern()
    print(name)
    name = intern("Mark")
    print(name)
    print(name.make_coffee())
    try:
        name.work()
    except Exception as e:
        print(e)