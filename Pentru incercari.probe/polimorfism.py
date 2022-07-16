class Romanian():
    def language(self):
        print("Limba romana")

class USA():
    def language(self):
        print("Limba engleza")

obj_ro = Romanian()
obj_usa = USA()

for country in (obj_ro, obj_usa):
    country.language()