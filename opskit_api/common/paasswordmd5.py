import hashlib


def md5passwd(passwd):
    md5 = hashlib.md5()
    md5.update(passwd.encode(encoding="utf-8"))
    return md5.hexdigest()
