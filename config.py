#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TamilFusion1


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5381948116:AAEPz_ngx3Q2314xYeJlkL-ow5zuOROoK-A")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "15655409"))
    API_HASH = os.environ.get("API_HASH", "ad6d7718a2b83df1ae1558754c560215")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1139006915").split())
    
