from bs4 import BeautifulSoup

##################################################################
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
BRO_URL = 'https://www.mtggoldfish.com/sets/The+Brothers+War#paper'
BRO_MONEY_DICT = {}
BRO_HTML = open('The+Brothers+War','r')
#####################################################################
#foils 23,168,251
#borderless 377
DMU_NUMS = [  4,  5, 10, 13, 18, 20, 25, 28, 29, 32,\
			 35, 41, 48, 54, 55, 57, 58, 61, 64, 64,\
			 66, 66, 68, 69, 78, 79, 83, 85, 89, 93,\
			 94, 95,101,105,109,112,113,113,125,126,\
			128,129,132,134,136,138,139,147,148,151,\
			157,158,160,162,163,164,168,168,172,174,\
			179,181,181,186,187,191,196,224,226,237,\
			237,238,241,249,251,251,251,253,253,257,\
			258,264,267,270,272,276,279,292,314,321,\
			337]
DMU_URL = 'https://www.mtggoldfish.com/sets/Dominaria+United#paper'
DMU_MONEY_DICT = {}
DMU_HTML = open('Dominaria+United','r')
####################################################################

def parse(handle, lut_dict={}):
	index = handle.read()
	S = BeautifulSoup(index, 'lxml')
	rows =  (S.find_all("tr"))
	# print(rows)#S.find_all("td", {"class": "text-right"}))
	header = (S.body.main.\
		find('div',{'class':'container-fluid layout-container-fluid'}).\
		find('div',{'data-react-class':'CardsContainer'}).\
		find('div',{'class':'table-responsive'}).table.thead.tr)
	for ind, i in enumerate(header):
		# print(i.text)
		if 'Card Num' in i.text:
			i_num = (ind)
		if 'Tabletop Price' in i.text:
			i_mon = (ind)
	body = (S.body.main.\
		find('div',{'class':'container-fluid layout-container-fluid'}).\
		find('div',{'data-react-class':'CardsContainer'}).\
		find('div',{'class':'table-responsive'}).table.tbody)
	for ind, i in enumerate(body):
		if ind==0:
			continue
		for jind, j in enumerate(i):
			if jind==i_num:
				cn_idx = int(j.text)
				# print(int(j.text),j.text)
			if jind==i_mon:
				try:
					m_idx =float(j.text[1:])
				except ValueError:
					m_idx =0 
				# print(float(j.text[1:]), j.text)
		lut_dict[cn_idx] = m_idx
	val = 0
	for i in BRO_NUMS:
		try: 
			val += lut_dict[i]
		except KeyError:
			pass
	# print(val)
	return val
# print(header.tr)
'''
for i in (S.find_all("tr")):
	# Traversing the names of the tags
	for j in i:
		print(j.text)
		if '$' in j.text:
			print(j.text)

'''
if __name__=='__main__':
	print(parse(BRO_HTML,lut_dict=BRO_MONEY_DICT))
	print(parse(DMU_HTML,lut_dict=DMU_MONEY_DICT))
