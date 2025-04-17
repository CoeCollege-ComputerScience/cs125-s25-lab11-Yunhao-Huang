with open('cs.txt', 'r') as f1, open('math.txt', 'r',) as f2:
    next(f1)
    next(f2)
    names1 = set(line.strip() for line in f1 if line.strip())
    names2 = set(line.strip() for line in f2 if line.strip())

common_names = names1 & names2
all_names = names1 | names2
cs_name = names1 - names2

print("Names in both files:")
for name in sorted(common_names):
    print(name)

print("Names in either file:")
for name in sorted(all_names):
    print(name)

print("Names only in cs.txt:")
for name in sorted(cs_name):
    print(name)

with open('studentYear.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split('\t')
        if len(parts) < 2:
            continue
        year, name = parts

        if year == '2' and name in names1:
            print(f"[a] cs in year 2：{name}")

        elif year == '1' and name not in names1 and name not in names2:
            print(f"[b] not cs or math in year 1：{name}")

        elif year == '4' and (name in names1 or name in names2):
            print(f"[c] cs or math in year 4：{name}")