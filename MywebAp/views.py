from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')
def count(request):
    data=request.GET['fulltextarea']
    word_list=data.split()
    length=len(word_list)
    worddic={}
    for w in word_list:
        if w in worddic:
            worddic[w]+=1
        else:
            worddic[w]=1
    sorted_list=sorted(worddic.items(), key=operator.itemgetter(1))
    return render(request,'wordFrequecy.html',{'fulltext':data,'words':length, 'worddictionary':sorted_list})