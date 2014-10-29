import json
import urllib2
import os
import urllib

def menu():
	while True:
		os.system('clear')
		print '*'*50
		print '\t\tYts.re searcher'
		print '*'*50
		print '\n'
		show()
		print "For help type :h"
		key = raw_input("Search: ")
		key_action(key)

def torrent():
	url = 'https://yts.re/api/list.json?limit='+limit+'&quality='+quality+'&set='+setPage
	conn = urllib2.urlopen(url)
	global text 
	text = json.load(conn)
	conn.close()

def show():
	index = 1
	for movie in range (int(limit)):
                print "%d. %s"%(index, text["MovieList"][movie]["MovieTitleClean"])
		index = index + 1

def setLimit():
	global limit
	limit = raw_input('Please set up show limit: ')
	torrent()

def setQuality():
	global quality
	option = ['720p','1080p','3D','ALL']
	newValue = raw_input('You can choose "720p" "1080p" "3D" or "ALL": ')
	if newValue in option:
		quality = newValue
		torrent()
	else:
		setQuality()

def setPages():
	global setPage
	newPage = raw_input("Which page do you want: ")
	setPage = newPage
	torrent()

def manual():
	os.system('clear')
	print """	Welcome in yify torrent
		For set up maximum show movies type ":set limit"
		for set up quality you looking  for type ":set quality"
		for set up page type ":n"
		for quit type ":quit"
		if you preview movie type ":go [number of  you looking for]
		"""
	raw_input()
	show()

def movieInfo(key):
	value = int(key)
	movieID = text['MovieList'][value-1]['MovieID']
	url1 = urllib2.urlopen('https://yts.re/api/movie.json?id='+movieID)
        js2 = json.load(url1)
        url1.close()
	os.system('clear')
	print '\n\n'
        print "Title: %s\n"% js2["MovieTitleClean"]
        print "Genre: %s/%s"% (js2["Genre1"],js2["Genre2"])
        print "Movie rating: %s"% js2["MovieRating"]
	print "Quality: %s \n"% js2["Quality"]
        print "Description: %s \n"% js2["LongDescription"]
        for x in range(4):
 	       print js2["CastList"][x]["ActorName"]," as ", js2["CastList"][x]["CharacterName"]
	key  =raw_input("Press d to dwnload torrent or any key to menu: ")
	if key.lower() == 'd':
		torrentFile = js2["TorrentUrl"]
                print "Start downloading torrent..."
                urllib.urlretrieve(torrentFile,js2["MovieTitle"]+".torrent")
                print "Download complete"
	else:
		show()


	

def key_action(key):
	key = key.split()
	if key[0].lower() ==  ':quit':
		exit()
	elif key[0].lower() == ':help':
		manual()
	elif key[0].lower() == ':set':
		if key[1].lower() == 'limit':
			setLimit()
		elif key[1].lower() == 'quality':
			setQuality()
	elif key[0].lower() == ':n':
		setPages()
	elif key[0].lower() == ':h':
		manual()
	elif key[0].lower() == ':go':
		movieInfo(key[1])
	

limit = '20'
setPage = '1'
quality = 'ALL'
torrent()
menu()
