from datetime import datetime
from src.entities.account import Account
from src.models.entities import PersonModel

class Person:
    def __init__(self, name: str, born_date: str, country: str, identity: str):
        self.__name = name
        self.account: Account = None
        self.__born_date = born_date
        self.__country = country
        self.__identity = identity
        self.__validate_born_date

    def name(self) -> str:
        return self.__name
    
    def __validate_born_date(self) -> bool:
        if '/' not in self.__born_date:
            raise ValueError('Date must be DAY/MONTH/YEAR')
        year = self.__born_date.split('/')[2]
        month = self.__born_date.split('/')[1]
        day = int(self.__born_date.split('/')[0])
    
        if day not in range(1, 32):
            raise ValueError('Day must be at 1 and 31, you provide: {}'.format(day))

        if len(month) <1 or len(month) > 2:
            raise ValueError('Month must have at least 1 and max 2 digit, you provide: {}'.format(len(month)))

        if int(month) not in range(1, 13):
            raise ValueError('Month must be at 1 and 12, you provide: {}'.format(month))

        if len(year) <4:
            raise ValueError('Year must have at least 4 digits, you provide: {}'.format(len(year)))
        if int(year) > int(datetime.now().year):
            raise ValueError('The max year can you provide is {}'.format(int(datetime.now().year)))
        
        if int(datetime.now().year) - int(year) < 18:
            raise ValueError('You need to be older than 18 years')

    def age(self) -> int:
        return int(datetime.now().year) - int(self.__born_date.split('/')[2])

    def country(self) -> str:
        return self.__country
    
    def identity(self) -> str:
        return self.__identity    

    def get_account(self) ->  Account:
        if self.account is None:
            raise ValueError(f"No accounts found for user {self.__name}")

        return self.account 

    def add_account(self, account: Account):
        self.account = account
    
    def details(self) -> PersonModel:
        return PersonModel(
            name=self.name(),
            age=self.age(),
            country=self.country(),
            identity=self.identity()
        )