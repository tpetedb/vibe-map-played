import csv

PLAYERS = [
    {"id": "7", "name": "Lotte", "email": "lotte@example.invalid"},
    {"id": "8", "name": "Tom", "email": "tom@example.invalid"},
    {"id": "9", "name": "Max", "email": "max@example.invalid"},
]
FIELDS = ["id", "name", "email"]
ERASE_ID = "7"


def write(path, rows):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


write("players.csv", PLAYERS)
with open("players.csv", newline="") as f:
    rows = list(csv.DictReader(f))

theirs = [row for row in rows if row["id"] == ERASE_ID]
rest = [row for row in rows if row["id"] != ERASE_ID]
write("export.csv", theirs)
write("players.csv", rest)
print(f"exported {len(theirs)} rows to export.csv")
print(f"erased {len(theirs)} rows, {len(rest)} rows left")
