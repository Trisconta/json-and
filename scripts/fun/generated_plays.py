""" generated_plays.py

(c)2026 Henrique Moreira
"""

from dataclasses import dataclass
from typing import List
import csv


def main():
    do_script(load_playlists_from_tsv("ref_plays.tsv"))


def do_script(playlists):
    page = HTMLPlaylistPage(playlists, title="Turn Back The Clock & Friends")
    html = page.build()
    with open("playlists.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated playlists.html")


@dataclass
class Playlist:
    pid: str
    dzr_id: str
    name: str

    @property
    def dzr_url(self) -> str:
        return f"https://www.deezer.com/us/playlist/{self.dzr_id}"


class HTMLPlaylistPage:
    def __init__(self, playlists: List[Playlist], title="Playlists"):
        self.playlists = playlists
        self.title = title

    def build(self) -> str:
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>{self.title}</title>
<style>
    :root {{
      --bg: #0b1020;
      --card-bg: #151a2c;
      --accent1: #ffb347;
      --accent2: #7bdff2;
      --accent3: #c792ea;
      --accent4: #ff6b6b;
      --text-main: #f5f7ff;
      --text-muted: #a0a4c0;
    }}

    body {{
      margin: 0;
      font-family: system-ui, sans-serif;
      background: radial-gradient(circle at top, #1b2340 0, var(--bg) 55%);
      color: var(--text-main);
      min-height: 100vh;
      padding: 2.5rem 1.5rem 3rem;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    h1 {{
      margin: 0 0 0.5rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      font-size: 1.4rem;
    }}

    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 1.5rem;
      width: 100%;
      max-width: 1100px;
    }}

    .card {{
      background: linear-gradient(145deg, #101528, #181e34);
      border-radius: 1rem;
      padding: 1.1rem;
      border: 1px solid rgba(255, 255, 255, 0.04);
      box-shadow: 0 18px 40px rgba(0, 0, 0, 0.45);
      transition: transform 0.18s ease-out, box-shadow 0.18s ease-out;
    }}

    .card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 22px 55px rgba(0, 0, 0, 0.6);
      border-color: rgba(255, 255, 255, 0.12);
    }}

    .title {{
      font-size: 1.05rem;
      font-weight: 600;
      margin-bottom: 0.35rem;
    }}

    .pid {{
      font-size: 0.8rem;
      color: var(--accent3);
      margin-bottom: 0.7rem;
    }}

    .dzr-link {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.45rem 0.8rem;
      border-radius: 999px;
      border: 1px solid rgba(255, 255, 255, 0.18);
      background: radial-gradient(circle at top left, rgba(255, 179, 71, 0.18), transparent 55%);
      color: var(--text-main);
      font-size: 0.8rem;
      text-decoration: none;
      text-transform: uppercase;
      letter-spacing: 0.12em;
    }}

    .dzr-link:hover {{
      border-color: rgba(255, 255, 255, 0.6);
    }}
</style>
</head>
<body>

<h1>{self.title}</h1>

<div class="grid">
{self._render_cards()}
</div>

</body>
</html>
"""

    def _render_cards(self) -> str:
        return "\n".join(
            f"""
<article class="card">
  <div class="title">{pl.name}</div>
  <div class="pid">ID: {pl.pid} * {pl.dzr_id}</div>
  <a class="dzr-link" href="{pl.dzr_url}" target="_blank" rel="noopener noreferrer">
    Open at Site
  </a>
</article>
"""
            for pl in self.playlists
        )


def load_playlists_from_tsv(path: str) -> List[Playlist]:
    playlists = []
    with open(path, "r", encoding="ascii") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            if "#PID" in row:
                pid = row["#PID"]
            else:
                pid = row["PID"]
            obj = Playlist(
                pid=pid,
                dzr_id=row["ID"].strip(),
                name=row["Name"].strip(),
            )
            playlists.append(obj)
    return playlists


if __name__ == "__main__":
    main()
