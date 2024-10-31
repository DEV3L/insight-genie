from dataclasses import dataclass
from typing import Dict, List

from .event_data import EventData
from .tweet_data import TweetData


@dataclass
class EventGroup:
    title: str
    event_ids: List[str]
    full_text: str
    hashtags: List[str]
    kcv: str
    media_urls: List[str]
    mentions: List[str]
    total_favorite_count: int
    tweets: List[TweetData]


def extract_event_groups(grouped_tweets: Dict[str, List[EventData]]) -> Dict[str, EventGroup]:
    return {title: _aggregate_event_data(title, events) for title, events in grouped_tweets.items()}


def _aggregate_event_data(group_title: str, events: List[EventData]) -> EventGroup:
    event_ids = list({event_id for event in events for event_id in event.event_ids})
    full_text = "\n".join(line for event in events for line in event.text.splitlines()[1:] if line.strip())
    hashtags = sorted({hashtag for event in events for hashtag in event.hashtags})
    kcv = next((event.kcv[0] for event in events if event.kcv), "")
    media_urls = list({media_url for event in events for media_url in event.media_urls})
    mentions = sorted({mention for event in events for mention in event.mentions})
    total_favorite_count = sum(event.favorite_count for event in events)

    return EventGroup(
        event_ids=event_ids,
        full_text=full_text,
        hashtags=hashtags,
        kcv=kcv,
        media_urls=media_urls,
        mentions=mentions,
        title=group_title,
        total_favorite_count=total_favorite_count,
        tweets=events,
    )
