import json

from insight_genie.exporters.twitter.extraction.tweet_extraction import load_twitter_data

from .manager.image import Image
from .models.event_group import EventGroup


def process_images(event_groups: dict[str, EventGroup]):
    return [
        Image(media_url, event.title).get_image_description()
        for event in event_groups.values()
        for media_url in event.media_urls
    ]


def filter_tweets_for_event_group(tweets: list[dict], event_ids: list[str]) -> list[dict]:
    return [tweet for tweet in tweets if tweet["tweet"]["id_str"] in event_ids]


def process_event_groups(event_groups: dict[str, EventGroup]) -> list[list[dict]]:
    tweets = load_twitter_data()

    for event_group in event_groups.values():
        tweet_events = filter_tweets_for_event_group(tweets, event_group.event_ids)
        json.dump(tweet_events, open(f"./data/twitter/events/groups/{event_group.title}.json", "w"))
