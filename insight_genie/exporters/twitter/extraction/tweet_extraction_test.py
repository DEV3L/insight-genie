from unittest.mock import mock_open, patch

import pytest

from .tweet_extraction import filter_tweets, load_twitter_data

mock_tweets_json = '[{"id_str": "1", "created_at": "Mon Oct 02 14:00:00 +0000 2023", "in_reply_to_id": null}, {"id_str": "2", "created_at": "Mon Oct 02 15:00:00 +0000 2023", "in_reply_to_id": "1"}]'


@pytest.fixture
def mock_tweets():
    return [
        {
            "tweet": {
                "id_str": "1",
                "created_at": "Mon Oct 02 14:00:00 +0000 2023",
                "favorite_count": 0,
                "entities": {"hashtags": [], "media": [], "user_mentions": [], "urls": []},
                "in_reply_to_status_id_str": None,
                "retweeted": False,
                "full_text": "Root tweet text - read",
            }
        },
        {
            "tweet": {
                "id_str": "2",
                "created_at": "Mon Oct 02 15:00:00 +0000 2023",
                "favorite_count": 0,
                "entities": {"hashtags": [], "media": [], "user_mentions": [], "urls": []},
                "in_reply_to_status_id_str": "1",
                "retweeted": False,
                "full_text": "Reply tweet text",
            }
        },
    ]


def test_load_twitter_data():
    with patch("builtins.open", mock_open(read_data=mock_tweets_json)):
        data = load_twitter_data()
        assert isinstance(data, list)
        assert len(data) == 2
        assert data[0]["id_str"] == "1"


def test_group_tweets(mock_tweets):
    grouped_tweets = filter_tweets(mock_tweets)
    assert len(grouped_tweets) == 1  # Only the root tweet should remain
    assert grouped_tweets[0].id_str == "1"
    assert len(grouped_tweets[0].replies) == 1
    assert grouped_tweets[0].replies[0].id_str == "2"
