from cryptography.fernet import Fernet

class CipherManager:
    _cipher = None

    @classmethod
    def initialize(cls, encryption_key: str):
        """
        Initialize the Fernet cipher with the provided encryption key.
        This must be called before using encrypt or decrypt.
        """
        cls._cipher = Fernet(encryption_key)

    @classmethod
    def encrypt(cls, data: str) -> str:
        if cls._cipher is None:
            raise ValueError("Cipher is not initialized. Call initialize() first.")
        return cls._cipher.encrypt(data.encode()).decode()

    @classmethod
    def decrypt(cls, data: str) -> str:
        if cls._cipher is None:
            raise ValueError("Cipher is not initialized. Call initialize() first.")
        return cls._cipher.decrypt(data.encode()).decode()