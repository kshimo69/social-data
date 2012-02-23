#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011 Shimomura Kimihiko <kshimo69@gmail.com>


import twitter

twitter_api = twitter.Twitter(domain="api.twitter.com", api_version='1')
trends = twitter_api.trends()
print [trend['name'] for trend in trends[0]["trends"]]
