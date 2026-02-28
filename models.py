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
class Offer:

    userId: int = 0
    offerId: int = 0
    title: str = ""
    description: str = ""
    price: float = 0.0
    offerCreateDate: str = ""
    isOfferEnd: bool = True