from .extractor import (
    clean_text,
    extract_title,
    get_all_hashtags,
    get_all_ids,
    get_all_media_urls,
    get_replies_text,
    separate_kcv_lines,
)
from .models.tweet_data import TweetData

tweet_data = TweetData(
    id_str="1",
    created_at="2023-10-01",
    favorite_count=0,
    in_reply_to_id=None,
    is_retweet=False,
    mentions=[],
    text="",
    urls=[],
    hashtags=["#fun"],
    media_urls=["http://example.com"],
    replies=[
        TweetData(
            id_str="2",
            created_at="2023-10-01",
            favorite_count=0,
            in_reply_to_id=None,
            is_retweet=False,
            mentions=[],
            text="Reply 1",
            urls=[],
            hashtags=["#exciting"],
            media_urls=[],
            replies=[],
        ),
        TweetData(
            id_str="3",
            created_at="2023-10-01",
            favorite_count=0,
            in_reply_to_id=None,
            is_retweet=False,
            mentions=[],
            text="Reply 2",
            urls=[],
            hashtags=["#fun"],
            media_urls=["http://example2.com"],
            replies=[],
        ),
    ],
)


def test_clean_text():
    text = "Check this out! #fun http://example.com"
    expected = "Check this out!"
    assert clean_text(text) == expected


def test_get_all_hashtags():
    expected = ["#fun", "#exciting"]
    assert set(get_all_hashtags(tweet_data)) == set(expected)


def test_get_all_media_urls():
    expected = ["http://example.com", "http://example2.com"]
    assert set(get_all_media_urls(tweet_data)) == set(expected)


def test_get_replies_text():
    expected = "Reply 1\nReply 2\n\n"
    assert get_replies_text(tweet_data) == expected


def test_extract_title():
    text = "Started reading: The Great Gatsby\nSome other text"
    expected = "The Great Gatsby"
    assert extract_title(text) == expected


def test_get_all_ids():
    expected = ["1", "2", "3"]
    assert get_all_ids(tweet_data) == expected


def test_separate_kcv_lines():
    text = "^Special line\nNormal line\n^Another special line"
    expected_special = ["^Special line", "^Another special line"]
    expected_other = "Normal line"
    special_lines, other_lines = separate_kcv_lines(text)
    assert special_lines == expected_special
    assert other_lines == expected_other
