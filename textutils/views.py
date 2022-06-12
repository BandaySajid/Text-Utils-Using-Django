#I have created this file -- Sajid
from django.http import HttpResponse
from django.shortcuts import render


#For Hint
# with open('dummy.txt', 'r') as f:
#     content = f.read()
# def index(request):
#     return HttpResponse('''<a href = "https://bandaysajid.ga">Sajid Banday</a>''')
# def about(request):
#     return HttpResponse("This is About")
# def dummy(request):
#     return HttpResponse(content)

def index(request):
    # params = {'name' : 'Sajid', 'place' : 'Mars'}
    return render(request, 'index.html') #params) # render takes 3rd arguement as dictionary
    # return HttpResponse("Home")
def analyze(request):
    #Getting text
    djtext = (request.POST.get('text', 'default'))

    #Checking Checkbox Values
    removepunc = (request.POST.get('removepunc', 'OFF'))
    fullcaps = (request.POST.get('fullcaps', 'OFF'))
    newlinerem = (request.POST.get('newlinerem', 'OFF'))
    #Analyzing text
    print(djtext)
    print(removepunc)
    if removepunc == 'on':
        punctuations = '''.?!,:;_–()[]/\‘’“”$1234567890…&*{}'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' : 'Removed Punctuations', 'analyzed_text' : analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose' : 'Full Capitalised', 'analyzed_text' : analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlinerem == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose' : 'New Line Removed', 'analyzed_text' : analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    # else:
    #     return HttpResponse("Error")
    if removepunc !='on' and fullcaps != 'on' and newlinerem != 'on':
        return HttpResponse("Error")
    else : 
        return render(request, 'analyze.html', params)

# def capFirst(request):
#     return HttpResponse("Capitalize First Letter")
# def lineRem(request):
#     return HttpResponse("Remove New Line")
# def spaceRem(request):
#     return HttpResponse("Remove Space")
# def charCount(request):
#     return HttpResponse("Count Character")
