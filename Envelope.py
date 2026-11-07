#this is the class where i will add
from dataclasses import dataclass
import base64

def _b64e(b: bytes) -> str:
    return base64.b64encode(b).decode()

def _b64d(s:str) -> bytes:
    return base64.b64decode(s)


@dataclass(frozen=True)
class Envelope:
    version:int
    algorithm:str
    kem_ciphertext:bytes
    nonce:bytes
    ciphertext:bytes

    def to_dict(self) -> dict:
        return {"version" : self.version ,"algorithm" : self.algorithm,"kem_ciphertext": _b64e(self.kem_ciphertext), "nonce": _b64e(self.nonce), "ciphertext":_b64e(self.ciphertext)}

    #@staticmethod bunu kullanırsak ilerde bu metodu alt classlardan biri kullnamak isterse sıkıntı yaşayabilirmiş o yüzden diğerini kullandık.Obje olarak extend eden classı değill Evelope döndürüyor.
    @classmethod #cls kullanacak classı otomatik alıyormuş. Ayrıca obje olarak extend eden classı döndürüyor.
    def from_dict(cls,d:dict) -> "Envelope":
        return cls(version=d["version"],algorithm=d["algorithm"],kem_ciphertext=_b64d(d["kem_ciphertext"]),nonce=_b64d(d["nonce"]),ciphertext=_b64d(d["ciphertext"]))


e = Envelope(1, "ML-KEM-768", b"kem", b"nonce", b"gizli")
e2 = Envelope.from_dict(e.to_dict())
print(e == e2)