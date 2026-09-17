import sqlite3

con = sqlite3.connect("well.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS scores")
cur.execute("CREATE TABLE scores(player, score)")
cur.executemany(
    "INSERT INTO scores VALUES (?, ?)",
    [("Lotte", 412), ("Tom", 380), ("Max", 512), ("Frank", 299), ("Rolinda", 640)],
)
cur.execute("CREATE INDEX scores_player ON scores(player)")
cur.execute("UPDATE scores SET score = score + 10 WHERE player = 'Lotte'")
cur.execute("UPDATE scores SET score = score - 10 WHERE player = 'Tom'")
con.commit()
for row in cur.execute("SELECT player, score FROM scores ORDER BY score DESC"):
    print(row)
con.close()
