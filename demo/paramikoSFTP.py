import paramiko

username = "***"
password = "***"

hostname = "127.0.0.1"
port = 22

try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)

    sftp =paramiko.SFTPClient.from_transport(t)

    sftp.put("/home/***/py_test/from/1.txt", "/home/***/py_test/to/1.txt")
    sftp.get("/home/***/py_test/to/2.txt", "/home/***/py_test/from/2.txt")
    t.close();
except Exception, e:
    import traceback
    traceback.print_exc()
    try:
        t.close()
    except:
        pass

