from django.contrib.auth.hashers import BasePasswordHasher
import hashlib

class SHA1MapleHasher(BasePasswordHasher):
    """
    The SHA1 password hashing algorithm (not recommended)
    """
    algorithm = "sha1"

    def encode(self, password, salt):
        assert password is not None
        return hashlib.sha1(password).hexdigest()

    def verify(self, password, encoded):
        return constant_time_compare(encoded, self.encode(password))

    def safe_summary(self, encoded):
        print 'hello'
        return OrderedDict([
            (_('algorithm'), self.algorithm),
            (_('salt'), mask_hash('asd', show=2)),
            (_('hash'), mask_hash('asd')),
        ])