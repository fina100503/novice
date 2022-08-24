# word = ["anggur","apel","jeruk"]
# for a in word:
#     print(a, len(a)
users = {'Hans': 'active', 'Éléonore': 'inactive', 'fina': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print(users)
        print(active_users)
a = {}
a["c"] = "d"
a["e"] = "f"
print(a)

       