from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader, select_autoescape

@dataclass
class LinkItem:
    href: str
    title: str
    description: str = ""

@dataclass
class LinkList:
    id: str
    title: str
    items: list[LinkItem]

lists = [
    LinkList("web-projects", "web apps", [
        LinkItem("https://7x11x13.xyz/last-fm-overlap/", "last-fm-overlap", "view taste overlap of two last.fm users"),
        LinkItem("https://7x11x13.xyz/sc-banner/", "sc-banner", "create seamless soundcloud banners")
    ]),
    LinkList("desktop-projects", "desktop apps", [
        LinkItem("https://github.com/7x11x13/songs-to-youtube", "songs-to-youtube", "convert songs to videos and upload them to youtube"),
        LinkItem("https://github.com/7x11x13/free-bandcamp-downloader", "free-bandcamp-downloader", "download $0 minimum music from bandcamp"),
        LinkItem("https://github.com/7x11x13/bandcamp-auto-uploader", "bandcamp-auto-uploader", "upload albums to bandcamp")
    ]),
    LinkList("browser-projects", "browser extensions", [
        LinkItem("https://github.com/7x11x13/hidden-bandcamp-tracks", "hidden-bandcamp-tracks", "detect hidden tracks on bandcamp album pages"),
        LinkItem("https://github.com/7x11x13/sc-filter", "sc-filter", "filter your soundcloud feed")
    ]),
    LinkList("library-projects", "libraries", [
        LinkItem("https://github.com/7x11x13/soundcloud.py", "soundcloud-v2", "python wrapper for soundcloud's internal api"),
        LinkItem("https://github.com/7x11x13/youtube-up", "youtube-up", "python library for uploading videos using youtube's internal api"),
        LinkItem("https://github.com/7x11x13/ez-pyload", "ez-pyload", "python library for downloading files from filesharing sites")
    ]),
    LinkList("links", "links", [
        LinkItem("https://github.com/7x11x13", "github"),
        LinkItem("https://pypi.org/user/7x11x13/", "pypi")
    ])
]

env = Environment(
    loader=FileSystemLoader(searchpath="./"),
    autoescape=select_autoescape(),
    trim_blocks=True,
    lstrip_blocks=True
)

template = env.get_template("template.html")
with open("index.html", "w") as f:
    f.write(template.render(lists=lists))