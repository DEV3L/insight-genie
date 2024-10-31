from dataclasses import dataclass


@dataclass
class EventData:
    event_date: str
    event_ids: list[str]
    favorite_count: int
    hashtags: list[str]
    is_start: bool
    kcv: list[str]
    media_urls: list[str]
    mentions: list[str]
    text: str
    title: str
    tweet_data: dict[str, any]
