import socket

print("localhost ->", socket.gethostbyname("localhost"))
for family, _, _, _, address in socket.getaddrinfo("localhost", 80):
    print(family.name, address[0])
try:
    print("vibe-map.invalid ->", socket.gethostbyname("vibe-map.invalid"))
except socket.gaierror as e:
    print("vibe-map.invalid -> no such name:", e.strerror)
