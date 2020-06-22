from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # arguments and keyword arguments
	print(args, kwargs)
	print(request.user)
	# return HttpResponse("<h1>Hello World!</h1>")
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
		contacts = {
			'title': "Jim",
			2: "Joe",
			3: "Jack"
		}
		return render(request, "contact.html", contacts)
	


def about_view(request, *args, **kwargs):
	my_context = {
		"title": "This is about us",
		"this_is_ture": True,
		"my_number": 123,
		"my_list": [123, 4231, 312, 'abc'],
		"my_html": "<h1>Hello World</h1>"

	}
	return render(request, "about.html", my_context)	
