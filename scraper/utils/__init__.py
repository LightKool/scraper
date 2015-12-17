# -*- coding: utf-8 -*-

import time

def current_milli_time():
	return int(round(time.time() * 1000))

def safe_strip(s):
	return s.strip() if s is not None and hasattr(s, 'strip') else ''