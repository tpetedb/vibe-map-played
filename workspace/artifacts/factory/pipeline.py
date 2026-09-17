import duckdb

con = duckdb.connect("camp.duckdb")
con.execute(
    "CREATE OR REPLACE TABLE bronze AS "
    "SELECT * FROM read_csv('raw.csv', all_varchar = true)"
)
con.execute(
    "CREATE OR REPLACE TABLE silver AS "
    "SELECT played_at, player, try_cast(score AS INTEGER) AS score FROM bronze "
    "WHERE try_cast(score AS INTEGER) IS NOT NULL"
)
con.execute(
    "CREATE OR REPLACE TABLE gold AS "
    "SELECT player, max(score) AS best FROM silver GROUP BY player"
)
for name in ("bronze", "silver", "gold"):
    print(name, con.execute(f"SELECT count(*) FROM {name}").fetchone()[0])
con.close()
