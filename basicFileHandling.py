name = input("Enter file:")
handle = open(name)
store = dict()
for lines in handle:
    if lines.startswith('From') and not lines.startswith('From:'):
        line = lines.strip().split()
        word = line[5]
        store[word[:2]] = store.get(word[:2], 0) + 1

storedlist = sorted(list(store.items()))
for k,v in storedlist:
    print(k,v)
