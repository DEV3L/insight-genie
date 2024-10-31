from dataclasses import dataclass, field


@dataclass
class TweetData:
    id_str: str
    created_at: str
    favorite_count: int
    hashtags: list[str]
    in_reply_to_id: str
    is_retweet: bool
    media_urls: list[str]
    mentions: list[str]
    text: str
    urls: list[str]
    replies: list["TweetData"] = field(default_factory=list)


def build_tweet_data(tweet: dict) -> TweetData:
    return TweetData(
        id_str=tweet["tweet"]["id_str"],
        created_at=tweet["tweet"]["created_at"],
        favorite_count=int(tweet["tweet"]["favorite_count"]),
        hashtags=[hashtag["text"] for hashtag in tweet["tweet"]["entities"].get("hashtags", [])],
        in_reply_to_id=tweet["tweet"].get("in_reply_to_status_id_str"),
        is_retweet=tweet["tweet"]["retweeted"],
        media_urls=[media["media_url_https"] for media in tweet["tweet"]["entities"].get("media", [])],
        mentions=[mention["screen_name"] for mention in tweet["tweet"]["entities"]["user_mentions"]],
        text=tweet["tweet"]["full_text"],
        urls=[url["expanded_url"] for url in tweet["tweet"]["entities"].get("urls", [])],
    )
