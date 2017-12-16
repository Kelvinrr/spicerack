from py2p import mesh
sock = mesh.MeshSocket('0.0.0.0', 50000)
sock.connect('192.168.1.14', 50000)
sock.send('Hello my boi')
print(sock.recv())
