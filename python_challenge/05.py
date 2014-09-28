
"""
I have to admit, I 100% cheated on this one. I had ABSOLUTELY no clue where to even start.
The only thing I got on my own was the word 'pickle', which led me to yes! pickle!. With some hints
I was able to find the banner.p, but I was at a complete loss on how to handle it.

Some of the trouble is due to me being in the wrong hints forum the entire time.

Without further ado:
"""

import urllib
import pickle

url_text = 'http://www.pythonchallenge.com/pc/def/banner.p'

banner_obj = urllib.urlopen(url_text)
banner = pickle.load(banner_obj)
banner_obj.close()

for item in banner:
	print ''.join(i[0]*i[1] for i in item)


