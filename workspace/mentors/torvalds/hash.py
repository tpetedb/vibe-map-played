"""The same hash git gives, from the bytes git actually hashes."""

import hashlib

BODY = b"what is up, doc?"
blob = b"blob " + str(len(BODY)).encode() + b"\x00" + BODY
print(hashlib.sha1(blob).hexdigest())
