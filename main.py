import config.queryString as queryString
import config.sharedSecret as sharedSecret

class BigBlueButton():
    def __init__(self, queryString, sharedSecret):
        self.checksum = build_checksum(queryString, sharedSecret)

    def _build_checksum(self, queryString, sharedSecret):
        return 1