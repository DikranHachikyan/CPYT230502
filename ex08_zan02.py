# %%

conn = dict(
    db='sales',
    port=1521,
    host='localhost',
    keepalive=True
)

print( f'host = {conn["host"]}' )

# %%

user = {
    'first_name': 'Anna',
    'last_name' : 'Smith',
    'phone' : '999-99-99',
    'age' : 36,
    'friends': ['John', 'Markus']
}

print(f'{user["first_name"]} {user["last_name"]}')


# %%
user1 = ['Anna', 'Smith', '999-99-99', 36]

print(user1)
# %%
print(user1[2])

# %%

print(user.keys())
# %%

print(user.values())

# %%

print(user.items())
# %%

print('age' in user)

# %%
# KeyError
print(user['email'])

# %%
print( user.get('email', 'no@no.no'))

# %%
