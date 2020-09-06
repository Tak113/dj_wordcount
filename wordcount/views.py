#return/convert python code to Http request
from django.http import HttpResponse
#render fucntion
from django.shortcuts import render
import operator

# if someone comes to the URL, send the request to below function
def home(request):
	return render(request, 'home.html')

def count(request):
	#get text from textarea
	fulltext = request.GET['fulltext']

	#split words
	wordlist = fulltext.split()

	#set list box
	worddictionary = {}

	#count up each words
	for word in wordlist:
		if word in worddictionary:
			#Increase
			worddictionary[word] += 1
		else:
			#add to the dictionary
			worddictionary[word] = 1

	#sort
	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse = True)

	# show fulltext in terminal
	# print(fulltext)
	
	# 'fulltext' which user enters to be stored ni {'fulltext':}
	return render(request, 'count.html', 
		{'fulltext':fulltext, 'count':len(wordlist), 
		'sortedwords':sortedwords})

#about page
def about(request):
	return render(request, 'about.html')