from dataclasses import asdict
from datetime import datetime

from .extractor import (
    clean_text,
    extract_title,
    get_all_hashtags,
    get_all_ids,
    get_all_media_urls,
    get_replies_text,
    separate_kcv_lines,
)
from .models.event_data import EventData
from .models.tweet_data import TweetData


def build_events(tweets_with_terms: list[TweetData]) -> dict[str, list[EventData]]:
    events = {
        title: [
            event_data
            for event_data in (create_event_data(details) for details in tweets_with_terms)
            if event_data.title == title
        ]
        for title in {create_event_data(details).title for details in tweets_with_terms}
    }
    return events


def create_event_data(tweet_data: TweetData) -> EventData:
    is_start = "started" in tweet_data.text.lower()
    created_at_date = datetime.strptime(tweet_data.created_at, "%a %b %d %H:%M:%S +0000 %Y").strftime("%Y%m%d")
    book_title = extract_title(tweet_data.text)
    event_ids = get_all_ids(tweet_data)
    cleaned_text = clean_text(tweet_data.text + "\n" + get_replies_text(tweet_data))
    kcv, lines = separate_kcv_lines(cleaned_text)

    return EventData(
        event_date=created_at_date,
        favorite_count=tweet_data.favorite_count,
        hashtags=get_all_hashtags(tweet_data),
        is_start=is_start,
        mentions=tweet_data.mentions,
        media_urls=get_all_media_urls(tweet_data),
        kcv=kcv,
        text=lines,
        title=book_title,
        tweet_data=asdict(tweet_data),
        event_ids=event_ids,
    )
