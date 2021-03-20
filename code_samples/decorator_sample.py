
def mana_requirement(mana_cost):
    def resource_requirement(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self = args[0]
            if mana_cost < self.mana:
                print("Calling Function: " + func.__name__)
                return func(*args, **kwargs)
        return wrapper
    return resource_requirement


class Hero:
    def __init__(self):
        self.mana = 10

    @mana_requirement(12)
    def cast(self):
        return 'success'


hero = Hero()
print(hero.cast())

