import json
from datetime import datetime
from typing import List

from ai_assistant_manager.encoding import UTF_8

from .models.tweet_data import TweetData, build_tweet_data
from .terms import ignore_terms, terms


def load_twitter_data() -> list[dict]:
    with open("./data/twitter/tweets.json", "r", encoding=UTF_8) as file:
        return json.load(file)


def filter_tweets(tweets: List[dict]) -> List[TweetData]:
    """Group tweets by their reply structure."""
    tweets_data = sorted(map(build_tweet_data, tweets), key=parse_tweet_date)
    tweet_dictionary = _build_tweet_dictionary(tweets_data)
    reply_ids = _identify_replies(tweets_data, tweet_dictionary)
    _append_replies(tweets_data, tweet_dictionary, reply_ids)

    return [
        group
        for group in list(filter(lambda td: td.id_str not in reply_ids, tweets_data))
        if any(term in group.text.split("\n")[0] for term in terms)
        and not any(term in group.text.lower() for term in ignore_terms)
        and not group.text.startswith("@")
    ]


def parse_tweet_date(tweet_data: TweetData) -> datetime:
    """Parse the created_at date of a tweet."""
    return datetime.strptime(tweet_data.created_at, "%a %b %d %H:%M:%S +0000 %Y")


def _build_tweet_dictionary(tweets_data: List[TweetData]) -> dict:
    """Build a dictionary of tweets by their id_str."""
    return {tweet_data.id_str: tweet_data for tweet_data in tweets_data}


def _identify_replies(tweets_data: List[TweetData], tweet_dictionary: dict) -> set:
    """Identify replies and return a set of reply ids."""
    return {
        tweet_data.id_str
        for tweet_data in tweets_data
        if tweet_data.in_reply_to_id and tweet_data.in_reply_to_id in tweet_dictionary
    }


def _append_replies(tweets_data: List[TweetData], tweet_dictionary: dict, reply_ids: set) -> None:
    """Append replies to their parent tweets."""
    for tweet_data in tweets_data:
        if tweet_data.id_str in reply_ids:
            parent_tweet = tweet_dictionary[tweet_data.in_reply_to_id]
            parent_tweet.replies.append(tweet_data)
