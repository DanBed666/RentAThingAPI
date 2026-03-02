from dataclasses import dataclass

@dataclass
class User:

    id: int = 0
    name: str = "Brak"
    surname: str = "Brak"
    age: int = 0
    email: str = "Brak"
    registerDate: str = "Brak"


@dataclass
class Offer:

    userId: int = 0
    offerId: int = 0
    title: str = "Brak"
    description: str = "Brak"
    price: float = 0.0
    offerCreateDate: str = "Brak"
    isOfferEnd: bool = True