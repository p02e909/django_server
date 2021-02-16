from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		"author": "nhattao",
		"title": "blog post 1",
		"content": "1st post content",
		"date_posted": "aug 1, 2018"
	},
	{
		"author": "nhattao 2",
		"title": "blog post 2",
		"content": "2nd post content",
		"date_posted": "aug 2, 2018"
	},
]


def home(request):
	context = {
		"posts": posts
	}
	return render(request, "blog/home.html", context)


def about(request):
	return render(request, "blog/about.html", {"title": "about"})
