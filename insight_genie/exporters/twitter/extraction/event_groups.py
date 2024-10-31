import json

from .manager.image import Image
from .markdown_generator import generate_markdown
from .models.event_group import EventGroup
from .tweet_extraction import load_twitter_data


def process_images(event_groups: dict[str, EventGroup]):
    return [
        Image(media_url, event.title).get_image_description()
        for event in event_groups.values()
        for media_url in event.media_urls
    ]


def filter_tweets_for_event_group(tweets: list[dict], event_ids: list[str]) -> list[dict]:
    return [tweet for tweet in tweets if tweet["tweet"]["id_str"] in event_ids]


def process_event_groups(event_groups: dict[str, EventGroup]) -> list[list[dict]]:
    markdown = generate_markdown(event_groups)
    first_event_key = next(iter(event_groups))

    with open(f"./data/twitter/event_summaries/Event Summary - {first_event_key}.txt", "w") as markdown_file:
        markdown_file.write(markdown)

    tweets = load_twitter_data()
    for event_group in event_groups.values():
        tweet_events = filter_tweets_for_event_group(tweets, event_group.event_ids)
        json.dump(tweet_events, open(f"./data/twitter/events/groups/{event_group.title}.json", "w"))
