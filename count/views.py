from django.shortcuts import render, redirect
import operator

def home(request):
	return render(request, 'home/index.html')

def count(request):
	staff=request.GET['some_text']
	word=staff.split()
	word_dictionary={}
	for word_list in word:
		if word_list in word_dictionary:
			word_dictionary[word_list] += 1
		else:
			word_dictionary[word_list] = 1
	sorted_dictionary = sorted(word_dictionary.items(),reverse=True, key=operator.itemgetter(1))
	length=len(word)
	contex={'length': length, 'staff': staff, 'word_dictionary': sorted_dictionary}
	return render(request, 'home/index.html', contex)
