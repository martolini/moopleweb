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

    def decode(self, password, salt):
        print 'hei'
        return None
    def verify(self, password, encoded):
        print password, encoded
        return constant_time_compare(encoded, self.encode(password))

    def safe_summary(self, encoded):
        algorithm, salt, hash = encoded.split('$', 2)
        assert algorithm == self.algorithm
        return OrderedDict([
            (_('algorithm'), algorithm),
            (_('salt'), mask_hash(salt, show=2)),
            (_('hash'), mask_hash(hash)),
        ])