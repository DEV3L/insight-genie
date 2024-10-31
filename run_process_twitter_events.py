from insight_genie.exporters.twitter.extraction.event_groups import process_event_groups, process_images
from insight_genie.exporters.twitter.extraction.events import build_events
from insight_genie.exporters.twitter.extraction.models.event_group import extract_event_groups
from insight_genie.exporters.twitter.extraction.tweet_extraction import (
    filter_tweets,
    load_twitter_data,
)

filter_text = "samurai"

tweets = load_twitter_data()

filtered_tweets = filter_tweets(tweets)
filtered_tweets = [tweet for tweet in filtered_tweets if filter_text in tweet.text.lower()]

events = build_events(filtered_tweets)
event_groups = extract_event_groups(events)

process_images(event_groups)
process_event_groups(event_groups)
