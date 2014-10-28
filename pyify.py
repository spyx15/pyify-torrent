import urllib2
import json
import urllib


def movieRequest(answer):
	download = False
	key = ''
	movieID = js["MovieList"][answer-1]["MovieID"]
	url1 = urllib2.urlopen('https://yts.re/api/movie.json?id='+movieID)
	js2 = json.load(url1)
	print js2["MovieTitleClean"]
	print js2["Genre1"],"/",js2["Genre2"]
	print "Movie rating: ",js2["MovieRating"]
	print "Description: ",js2["LongDescription"]
	for x in range(4):
		print js2["CastList"][x]["ActorName"]," as ", js2["CastList"][x]["CharacterName"]
	key = raw_input( "Press D to download torrent or press any key to back to menu: ")
	if key != 'd':
		menu()
	else:
		torrent = js2["TorrentUrl"]
		print "Start downloading torrent..."
		urllib.urlretrieve(torrent,js2["MovieTitle"]+".torrent")
		print "Download complete"


def menu():			
	#open yifi torrent page.
	url = 'https://yts.re/api/list.json?quality=720p'
	j = urllib2.urlopen(url)
	#copy file to json structure
	global js 
	js = json.load(j)

	i = 1
	print "\tWelcome to yify-torrent :)\n"

	for x in range(20):
		print i,". ",js["MovieList"][x]["MovieTitleClean"]
		i = i + 1

	answer = input("What movie do you want?: ")
	movieRequest(answer)

menu()
