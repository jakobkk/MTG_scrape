from bs4 import BeautifulSoup
# foils 6,49,106,215,223,248,261
# borderless 286
BRO_NUMS = [  3,  5,  6, 11, 16, 17, 19, 22, 22, 23,\
			 28, 28, 32, 37, 37, 41, 43, 44, 44, 46,\
			 49, 49, 52, 54, 54, 68, 71, 71, 72, 73,\
			 73, 76, 77, 90, 91, 91, 93, 93,100,100,\
			102,103,103,106,106,106,109,110,116,117,\
			118,118,123,123,124,127,128,129,132,132,\
			133,136,136,147,147,152,152,153,153,158,\
			159,161,164,166,167,168,173,177,182,182,\
			184,184,187,196,197,199,201,208,213,215,\
			221,222,223,223,224,235,236,239,239,243,\
			248,248,249,251,251,255,258,258,260,260,\
			261,261,264,266,266,270,275,286]
BRO_URL = 'https://www.mtggoldfish.com/sets/The+Brothers+War#online'