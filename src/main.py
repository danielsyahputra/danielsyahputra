from pathlib import Path
import datetime
import pytz

import feedparser

def update_footer():
    timestamp = datetime.datetime.now(pytz.timezone("Asia/Jakarta")).strftime("%c")
    footer = Path('../FOOTER.md').read_text()
    return footer.format(timestamp=timestamp)

def update_readme_github_activities(github_feed, readme_base, join_on):
    d = feedparser.parse(github_feed)
    activities = []
    for item in d.entries[:10]:
        if item.get('summary'):
            title = item["summary"] if item["summary"] != "No description" else item["title"]
            link = item.get("links")[0]["href"]
            activities.append(f" - [{title}]({link})")
    activities_joined = '\n'.join(activities)
    return readme_base[:readme_base.find(rss_title)] + f"{join_on}\n{activities_joined}"

if __name__=="__main__":
    rss_title = "### Activities by Daniel Syahputra on Github" # Anchor for where to append activities
    readme = Path('../README.md').read_text()
    updated_readme = update_readme_github_activities("https://rsshub.app/github/repos/danielsyahputra", readme, rss_title)
    with open('../README.md', "w+") as f:
        f.write(updated_readme + update_footer())