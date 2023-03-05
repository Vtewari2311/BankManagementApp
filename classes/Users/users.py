import abc

from app.models import Owner

class AbstractUser(abc.ABC):
    @abc.abstractmethod
    def getAccountID(self):
        pass

    @abc.abstractmethod
    def getEmail(self):
        pass

    @abc.abstractmethod
    def getUserName(self):
        pass

    @abc.abstractmethod
    def getPassword(self):
        pass

    @abc.abstractmethod
    def getFirstName(self):
        pass

    @abc.abstractmethod
    def getLastName(self):
        pass

    @abc.abstractmethod
    def getAccountNumber(self):
        pass

    @abc.abstractmethod
    def setEmail(self, param):
        pass

    @abc.abstractmethod
    def setUserName(self, param):
        pass

    @abc.abstractmethod
    def setPassword(self, param):
        pass

    @abc.abstractmethod
    def setFirstName(self, param):
        pass

    @abc.abstractmethod
    def setLastName(self, param):
        pass

    @abc.abstractmethod
    def setAccountNumber(self, param):
        pass


class Owner(AbstractUser):

    def __init__(self, model: Owner):
        self.model = model

    def getAccountID(self) -> int:
        return self.model.accountID.accountID

    def getEmail(self) -> str:
        return self.model.accountID.email

    def getUserName(self) -> str:
        return self.model.accountID.userName

    def getPassword(self) -> str:
        return self.model.accountID.password

    def getFirstName(self) -> str:
        return self.model.accountID.firstName

    def getLastName(self) -> str:
        return self.model.accountID.lastName

    def getUserType(self) -> str:
        return self.model.accountID.userType

    def getAccountNumber(self) -> str:
        return self.model.accountID.accountNumber

    def setEmail(self, email):
        if self.model.accountID.email == email:
            return
        if len(Owner.objects.filter(email=email)) != 0:
            raise ValueError("A user with this email already exists.")
        accID = self.model.accountID.accountID
        userObj = Owner.objects.get(accountID=accID)
        userObj.email = email
        userObj.save()

    def setUserName(self, name):
        if self.model.accountID.userName == name:
            return
        if len(Owner.objects.filter(userName=name)) != 0:
            raise ValueError("A user with this user name already exists.")
        accID = self.model.accountID.accountID
        userObj = Owner.objects.get(accountID=accID)
        userObj.userName = name
        userObj.save()

    def setPassword(self, pswd):
        if self.model.accountID.password == pswd:
            return
        if len(pswd) < 8:
            raise ValueError("User password is too small")
        accID = self.model.accountID.accountID
        userObj = Owner.objects.get(accountID=accID)
        userObj.password = pswd
        userObj.save()

    def setFirstName(self, name):
        if self.model.accountID.firstName == name:
            return
        accID = self.model.accountID.accountID
        userObj = Owner.objects.get(accountID=accID)
        userObj.firstName = name
        userObj.save()

    def setLastName(self, name):
        if self.model.accountID.lastName == name:
            return
        accID = self.model.accountID.accountID
        userObj = Owner.objects.get(accountID=accID)
        userObj.lastName = name
        userObj.save()

    def setAccountNumber(self, num):
        if self.model.accountID.accountNumber == num:
            return
        if len(num) != 12 or num.isnumeric():
            raise ValueError("User account number is not 12 digits")
        accID = self.model.accountID.accountID
        userObj = Owner.objects.get(accountID=accID)
        userObj.accountNumber = num
        userObj.save()

