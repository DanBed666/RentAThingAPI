from dataclasses import dataclass

@dataclass
class User:

    id: int = 0
    name: str = ""
    surname: str = ""
    age: int = ""
    email: str = ""
    registerDate: str = ""


@dataclass
class Offers:

    userId: int = 0
    offerId: int = 0
    title: str = ""
    description: str = ""
    price: int = 0
    offerCreateDate: str = ""