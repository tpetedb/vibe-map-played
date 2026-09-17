# The rules are the ones the Claude API rate limits page states: a 429 carries a
# retry-after header saying how long to wait, and an earlier retry fails.
RESPONSES = [(429, 2), (429, None), (200, None)]

wait = 2
for status, retry_after in RESPONSES:
    if status == 200:
        print("200 OK")
        break
    if retry_after is not None:
        print(f"429 retry-after {retry_after}")
        wait = retry_after
    else:
        print("429 no retry-after")
        wait *= 2
    print(f"waiting {wait} s")
