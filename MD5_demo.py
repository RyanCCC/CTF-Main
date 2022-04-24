import hashlib

filename = '/fllllllllllllag'
cook = 'efa50e1b-3d66-4463-8826-e606e10ad52a'

m_filename = hashlib.md5(filename.encode())
mm = hashlib.md5((cook + m_filename.hexdigest()).encode())

print(m_filename.hexdigest())
print(mm.hexdigest())