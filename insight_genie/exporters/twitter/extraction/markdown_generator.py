from .manager.author import Author
from .manager.image import Image
from .models.event_group import EventGroup


def generate_markdown(event_groups: dict[str, EventGroup]) -> str:
    formatted_events = map(lambda item: _format_event(*item), event_groups.items())
    return "\n".join(formatted_events)


def _format_event(title: str, event: EventGroup) -> str:
    author_mentions = ", ".join(event.mentions) if event.mentions else ""
    author_data = Author(title, author_mentions).get_author_description()

    event_ids = "- " + "\n- ".join(event.event_ids) if event.event_ids else ""
    hashtags = "- " + "\n- ".join(event.hashtags) if event.hashtags else ""
    media_markdown = _build_media_section(event.media_urls, title)

    return f"""## {title}

### Full Text

{event.full_text}

### MetaData

#### Hashtags

{hashtags}

#### Favorite Count

{event.total_favorite_count}

#### KCV

{event.kcv}

{author_data}
#### Event Ids

{event_ids}

### Media
{media_markdown}
"""


def _build_media_section(media_urls: list[str], title: str) -> str:
    return "".join([Image(media_url, title).get_image_description() for media_url in media_urls])
