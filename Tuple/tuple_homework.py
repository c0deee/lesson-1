import random
a = tuple(random.randint(0, 9) for i in range(10))
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
print(a), sum(a)
print(long_word.count('т'))
print(long_word.count('а'))
print(long_word.count('и'))
