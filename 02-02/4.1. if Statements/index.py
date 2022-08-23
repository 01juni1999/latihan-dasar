print("hello world")
words = ("anggur", "alpukat", "mangga")
for i in words :
    print (i)

users = ('hp': 'active', 'kamera': 'inactive', 'iphone': 'active')
for user, status in users.copy().items():
        if status == 'inactive':
            del users(user)