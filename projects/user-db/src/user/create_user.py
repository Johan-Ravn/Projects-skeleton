from hashlib import sha256
from typing import Optional

class Mail:
    def __init__(self, username: str, domain: str) -> None:
        self.user = username.replace(" ", "")
        self.domain = domain
    
    def getMail(self) -> str:
        """Basic mail creator"""
        return ''.join(self.user + self.domain)

class MailDomains:
    _instance = None
    _domains = ["gmail", "hotmail"] # Expand later
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def getDomains(self) -> list[str]:
        return self._domains

class HashPassword:
    def __init__(self, password: str) -> None:
        self.password = self.SHA_256_HASH(password)
        
    def __repr__(self) -> str:
        return self.password
    
    @staticmethod
    def SHA_256_HASH(password) -> str:
        SHA_HASH = sha256()
        SHA_HASH.update(password.encode('utf-8'))
        return SHA_HASH.hexdigest()

class User:
    def __repr__(self) -> str:
        parameters = [
            f"Name={self.name}\n",
            f"HashedPassword={self.hashedPassword}\n",
            f"Mmail={self.mail}\n",
            f"Id={self.id}\n"
        ]
        return f"{''.join(parameters)}"
    
    def __init__(self) -> None:
        self.name = None
        self.hashedPassword = None
        self.mail = None
        self.id = None
    
    def setName(self, name: str) -> None:
        self.name = name
    
    def setPassword(self, password: str) -> None:
        self.hashedPassword = HashPassword(password)
    
    def setMail(self, mail: str) -> None:
        self.mail = mail
        
    def setId(self, id: int) -> None:
        self.id = id
        
    def getName(self) -> str:
        return self.name
    
    def getPassword(self) -> str:
        return self.hashedPassword
    
    def getMail(self) -> str:
        return self.mail
    
    def getID(self) -> int:
        return self.id

class SingletonID:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        self.currentId = 1
    
    def getId(self) -> int:
        self.currentId += 1
        return self.currentId - 1
    
class UserFactory:
    def __init__(self, *, name: str, password: str, mail_username: str, mail_domain: str):
        self.name = name
        self.password = password
        self.mailUsername = mail_username # String containing everything except @gmail.com
        self.mailDomain = mail_domain
        self.id = SingletonID().getId()
    
    def createUser(self) -> User:
        user = User()
        user.setName(self.name)
        user.setPassword(self.password)
        user.setMail(Mail(self.mailUsername, self.mailDomain).getMail())
        user.setId(self.id)
        return user

class InputUserInfo:
    def __init__(self) -> None:
        self.name = None
        self.password = None
        self.mailUserName = None
        self.mailDomain = None
    
    def setInput(self) -> None:
        self.setName()
        self.setPassword()
        self.setMailUserName()
        self.setMailDomain()
    
    def setName(self) -> None:
        while True:
            nameInput = input("Input a name less than 19 characters:\n").strip()
            if len(nameInput) <= 0 or len(nameInput) > 18:
                print("Name too short or long")
                continue
            if not nameInput.isalpha():
                print("Name can only contain alphabetic characters")
                continue
            self.name = nameInput
            break
    
    def setPassword(self) -> None:
        while True:
            passwordInput = input("Input a password greater than 7 and less than 13 characters\n").strip()
            if len(passwordInput) < 8 or len(passwordInput) > 13:
                print("Password too short or long")
                continue
            if not any(c.islower() for c in passwordInput):
                print("Password needs one lowercase character")
                continue
            if not any(c.isupper() for c in passwordInput):
                print("Password needs one uppercase character")
                continue
            if not any(c.isdigit() for c in passwordInput):
                print("Password needs one digit")
                continue
            self.password = passwordInput
            break
    
    def setMailUserName(self) -> None:
        while True:
            username = input("Input mail username\n")
            allowed_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._")
            reserved_keywords = ["admin", "administrator", "root", "support", "help"]
            
            if not all(char in allowed_characters for char in username):
                continue
            
            if username.startswith(".") or username.endswith("."):
                continue
            
            if ".." in username:
                continue
            
            if len(username) > 64 or len(username) <= 8:
                continue

            if username.lower() in reserved_keywords:
                continue
            
            self.mailUserName = username
            break
    
    def setMailDomain(self) -> None:
        domains = MailDomains().getDomains()
        while True:
            domain = input("Input domain\n").strip().lower()
            if domain in domains:
                self.mailDomain = domain
                break
            
            elif domain == "help":
                print(domains)
                
            else:
                print("Wrong domain\nType \"Help\" to see possible domains")
    
    def getName(self) -> Optional[str]:
        return self.name
    
    def getPassword(self) -> Optional[str]:
        return self.password
    
    def getMailUserName(self) -> Optional[str]:
        return self.mailUserName
    
    def getMailDomain(self) -> Optional[str]:
        return self.mailDomain
                

def createUserFromInput():
    userInfo = InputUserInfo()
    userInfo.setInput()
    user = UserFactory(
        name=userInfo.getName(),
        password=userInfo.getPassword(),
        mail_username=userInfo.getMailUserName(),
        mail_domain=userInfo.getMailDomain()
    ).createUser()
    return user

