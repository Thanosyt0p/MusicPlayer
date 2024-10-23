"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "27731023")
        self.API_HASH: str = os.environ.get("API_HASH", "e5533bd0cafa7bfa95205b2aaed57bcb")
        self.SESSION: str = os.environ.get("SESSION", "BQBCE9_aDNBOND7LnSuLpVxQ_5CT_VM1_WtUKHgnkMhxCXBQIGSad-3k3nI5EnIJ94k8Eg1N-9GR9iP34Mkfz8MJQXcGJ-FsfBjdpcHXK0uxMChockwbmuUS-RhCC7etivT2q0c1Ta2egTMRCSMW5KE0mVg3oiI96don-ZzdtAxnDRNFuCKUPjlDQCZWqiZhOjnDByQxbfj1EorfnkXKlxOLxRFp5GDT1C76CsiGUu5d8GVmI7RjUyHcIMeNYq4Gv2aXTq0yhPoHv5IsD-FnEFPKoycRI9LnlHiIcHzSibRGyLdQuWbeAwbKTgFldS4gkz9fBIjIXKrhJr-gxqCGtNgoAAAAAY-q97QA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "6333624410:AAE80MnoUMn56KkpzpY1uF5t2VQrgrzbfbY")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "/").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


config = Config()
