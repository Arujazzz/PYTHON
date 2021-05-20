a = list(map(int, input().split()))
seen = set()
print('\n'.join('NO' if x not in seen and not seen.add(x) else 'YES' for x in a))