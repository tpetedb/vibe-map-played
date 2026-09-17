import platform
import sqlite3

print("1 hardware:", platform.machine(), platform.processor() or "(not reported)")
print("2 operating system:", platform.platform())
print("3 runtime: Python", platform.python_version())
print("4 libraries: sqlite3", sqlite3.sqlite_version)
print("5 your app: vibe, in this camp")
print("6 the agent: whatever is reading and writing all of the above")
