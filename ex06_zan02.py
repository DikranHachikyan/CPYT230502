# %%
tp = (12, 34, 45, 67, 79)

print( f'tp={tp}' )

# %%

print( f'tp[1] = {tp[1]}')

# %%
# TypeError
# tp[1] = 14

# %%

a, b, c, d, e = tp

print(f'a={a}, b={b}, c={c}, d={d}, e={e}')

# %%

a, b, *_ = tp

print(f'a={a}, b={b}')


# %%

*_, a, b = tp

print(f'a={a}, b={b}')

# %%

tp = 45, 34, 56, 78

print(f'tp = {tp}')
# %%

t1 = (10,)

print(f't1={t1} type is {type(t1)}')

# %%

print( 34 in tp )

# %%

print( 44 not in tp )
# %%

print( type(tp) is tuple )

# %%
# може и така, но не е правилно
# print( type(tp) == tuple )

# %%
