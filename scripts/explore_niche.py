from agent_office.youtube import search_videos, get_videos, get_subscriber_counts

QUERY = "restoring vintage watches"

video_ids = search_videos(QUERY)
videos = get_videos(video_ids)
channel_ids = list({video["channel_id"] for video in videos})
subs = get_subscriber_counts(channel_ids)

outliers = 0

for video in videos:
    channel_subs = subs.get(video["channel_id"], 0)
    views = video["views"]
    ratio = views / channel_subs if channel_subs else 0
    if 0 < channel_subs < 10000 and views > 5000:
        outliers+=1
    print(f"{views:>10,} views | {channel_subs:>9,} subs | x{ratio:>6.1f} | {video['title'][:60]} | {video['language']:>7}")

print(f"Outliers: {outliers}")
