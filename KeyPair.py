from dataclasses import dataclass,field

@dataclass(frozen=True)
class KeyPair:
    public_key:bytes
    secret_key:bytes = field(repr=False)

#   def  __init__(self,public_key: bytes , secret_key: bytes) ->None :
#       self.public_key=public_key
#       self.secret_key=secret_key

    def public_key_boyutu(self) -> int:
        return len(self.public_key)


kp=KeyPair(b"abc",b"xyz123")
print(kp.public_key_boyutu())
print(kp.public_key)
print(kp)#repr=False private keyin yazılmasını engeller ama print(kp.secret_key) yazarsan görünür.

#kp.public_key="cdf" ->bu line frozen yüzünden artık çalışmaz