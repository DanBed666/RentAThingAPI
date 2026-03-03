from dataclasses import dataclass

@dataclass
class User:

    uId: int = 0
    name: str = "Brak"
    surname: str = "Brak"
    username: str = "Brak"
    registerDate: str = "Brak"
    birthDate: str = "Brak"
    profilePhotoLink: str = "https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_1280.png"


@dataclass
class Offer:

    userId: int = 0
    offerId: int = 0
    title: str = "Brak"
    description: str = "Brak"
    price: float = 0.0
    offerCreateDate: str = "Brak"
    isOfferEnd: bool = True