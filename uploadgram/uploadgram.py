#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Copyright (C) 2021 The Authors
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import Client, __version__
from pyrogram.enums import ParseMode
from .get_config import get_config


class Uploadgram(Client):
    """ modded client """

    def __init__(self):
        super().__init__(
            name="UploadGram",
            api_id=int(17983098),
            api_hash="ee28199396e0925f1f44d945ac174f64",
            bot_token="6280972722:AAF33Sq6Jz6nJl9tURfRSfe6Po4r4hoY2aU",
            parse_mode=ParseMode.HTML,
            sleep_threshold=int(get_config("UG_TG_ST", 10)),
            no_updates=True
        )

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        print(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} started."
        )

    async def stop(self, *args):
        await super().stop()
        print("UploadGram stopped. Bye.")
