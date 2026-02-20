import csv, sys

path = '/home/m1429240/Projetos/PainelCad/data/ocorrencias.csv'

with open(path, 'r', encoding='utf-8', errors='replace') as f:
    raw = f.read()

print(f"Total chars: {len(raw)}")
print(f"Has double quotes: {chr(34) in raw}")

lines = raw.split('\n')
print(f"Lines (split newline): {len(lines)}")

# try with \r\n
lines_crlf = raw.split('\r\n')
print(f"Lines (split crlf): {len(lines_crlf)}")

# Check field counts
header_fields = lines[0].rstrip('\r').split(',')
print(f"Header fields: {len(header_fields)}")

# Count how many lines have exactly the right number of fields
right_count = 0
wrong_count = 0
wrong_examples = []
for i, line in enumerate(lines[1:], 2):
    line = line.rstrip('\r')
    if not line.strip():
        continue
    fields = line.split(',')
    if len(fields) == len(header_fields):
        right_count += 1
    else:
        wrong_count += 1
        if len(wrong_examples) < 5:
            wrong_examples.append((i, len(fields), line[:200]))

print(f"Lines with correct field count ({len(header_fields)}): {right_count}")
print(f"Lines with wrong field count: {wrong_count}")
for ex in wrong_examples:
    print(f"  Line {ex[0]}: {ex[1]} fields -> {ex[2][:150]}")

# Check for quotes
quote_count = raw.count('"')
print(f"Total quote chars: {quote_count}")
if quote_count > 0:
    # find positions of quotes
    for i, ch in enumerate(raw):
        if ch == '"':
            start = max(0, i-30)
            end = min(len(raw), i+30)
            print(f"  Quote at pos {i}: ...{repr(raw[start:end])}...")
            break

# Try python csv module
with open(path, 'r', encoding='utf-8', errors='replace') as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        count += 1
    print(f"Python csv.reader row count: {count}")
