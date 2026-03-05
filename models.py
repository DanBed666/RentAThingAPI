from dataclasses import dataclass
from config import get_var

@dataclass
class User:

    uId: int = 0
    name: str = get_var("DEFAULT_INFO")
    surname: str = get_var("DEFAULT_INFO")
    username: str = get_var("DEFAULT_INFO")
    registerDate: str = get_var("DEFAULT_INFO")
    birthDate: str = get_var("DEFAULT_INFO")
    profilePhotoLink: str = get_var("DEFAULT_PROFILE")


@dataclass
class Offer:

    userId: int = 0
    offerId: int = 0
    title: str = get_var("DEFAULT_INFO")
    description: str = get_var("DEFAULT_INFO")
    price: float = 0.0
    offerCreateDate: str = get_var("DEFAULT_INFO")
    isOfferEnd: bool = True