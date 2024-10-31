import re
from functools import reduce
from typing import List, Tuple

from .models.tweet_data import TweetData

HASHTAG_PATTERN = r"#\w+"
URL_PATTERN = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
LINE_PATTERN = r"^- @.*$"


def clean_text(text: str) -> str:
    """Remove hashtags, URLs, and lines starting with '-' from the text."""
    text = re.sub(HASHTAG_PATTERN, "", text)
    text = re.sub(URL_PATTERN, "", text)
    text = re.sub(LINE_PATTERN, "", text, flags=re.MULTILINE)
    return text.strip()


def get_all_hashtags(tweet_data: TweetData) -> List[str]:
    """Recursively gather all hashtags from the tweet and its replies."""
    return sorted(set(tweet_data.hashtags).union(*(get_all_hashtags(reply) for reply in tweet_data.replies)))


def get_all_media_urls(tweet_data: TweetData) -> List[str]:
    """Recursively gather all media URLs from the tweet and its replies."""
    return list(set(tweet_data.media_urls).union(*(get_all_media_urls(reply) for reply in tweet_data.replies)))


def get_all_ids(tweet_data: TweetData) -> List[str]:
    """Recursively gather all id_str from the tweet and its replies."""
    return sorted(set([tweet_data.id_str]).union(*(get_all_ids(reply) for reply in tweet_data.replies)))


def get_replies_text(tweet_data: TweetData) -> str:
    """Recursively gather replies text with indentation based on the level of nesting."""
    replies_text = [reply.text for reply in tweet_data.replies]
    replies_text.extend(get_replies_text(reply) for reply in tweet_data.replies)
    return "\n".join(replies_text)


def extract_title(text: str) -> str:
    """Extract the book title from the tweet text."""
    phrases_to_remove = [
        "Started listening to:",
        "Finished listening to:",
        "Started reading:",
        "Finished reading:",
        "Finished reading ",
        "Started reading ",
    ]
    return reduce(lambda t, phrase: t.replace(phrase, ""), phrases_to_remove, text.split("\n")[0]).strip()


def separate_kcv_lines(text: str) -> Tuple[List[str], str]:
    """Separate lines starting with '^' from the rest of the text."""
    lines = text.splitlines()
    special_lines = [line for line in lines if line.startswith("^")]
    other_lines = [line for line in lines if not line.startswith("^")]
    return special_lines, "\n".join(other_lines)
