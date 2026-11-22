import dis
import os
from datetime import datetime, timedelta, timezone

import httpx
from dotenv import load_dotenv

load_dotenv()

_API_KEY = os.getenv("YOUTUBE_API_KEY")
_BASE_URL = "https://www.googleapis.com/youtube/v3"

def _get(endpoint: str, params: dict) -> dict:
    """Send a GET request to the YouTube API and return the JSON body."""
    params["key"] = _API_KEY
    response = httpx.get(f"{_BASE_URL}/{endpoint}", params=params, timeout=30)
    response.raise_for_status()
    return response.json()

def search_videos(query: str, max_results: int = 10, days: int=30) -> list[str]:
    """Find the most viewed recent videos for a query. Uses 1 of 100 daily search calls."""
    published_after = datetime.now(timezone.utc) - timedelta(days=days)
    data = _get("search", {
        "part": "id",
        "q": query,
        "type": "video",
        "order": "viewCount",
        "maxResults": max_results,
        "publishedAfter": published_after.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "relevanceLanguage": "en",
        "videoDuration": "medium",
    })
    return [item["id"]["videoId"] for item in data["items"]]

def get_videos(video_ids: list[str]) -> list[dict]:
    """Get title, channel and view count for up to 50 videos. Costs 1 unit."""
    data = _get("videos", {
        "part": "snippet, statistics",
        "id": ",".join(video_ids),
    })
    videos = []
    for item in data["items"]:
        videos.append({
            "title": item["snippet"]["title"],
            "channel_id": item["snippet"]["channelId"],
            "views": int(item["statistics"].get("viewCount", 0)),
            "language": item["snippet"].get("defaultAudioLanguage", "unknown"),
        })
    return videos

def get_subscriber_counts(channel_ids: list[str]) -> dict[str, int]:
    """Map channel ID to subscriber count for up to 50 channels. Costs 1 unit."""
    data = _get("channels", {
        "part": "statistics",
        "id": ",".join(channel_ids),
    })
    counts = {}
    for item in data["items"]:
        counts[item["id"]] = int(item["statistics"].get("subscriberCount", 0))
    return counts
