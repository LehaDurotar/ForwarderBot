from enum import Enum


class WallTypeEnum(str, Enum):
    vkontakte = "vkontakte"
    twitter = "twitter"
    instagram = "instagram"


class SubscriberLevelEnum(str, Enum):
    guest = "guest"
    regular = "regular"
    premium = "premium"


class ChatTypeEnum(str, Enum):
    private = "private"
    channel = "channel"
    group = "group"
