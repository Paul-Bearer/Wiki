from django.shortcuts import render, redirect
from . import util
import markdown2, random

def index(request):
    entries = util.list_entries()
    x = util.get_entry("CSS")
    y = util.get_entry("Apple")
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def entry_page(request, title):
    content = util.get_entry(title)
    if content:
        new_content = markdown2.markdown(content)
        return render(request, "encyclopedia/entry_page.html", {
            "title": title,
            "found" : True,
            "content":new_content
        })

    else:
        return render(request, "encyclopedia/entry_page.html", {
            "title": title,
            "found" : False
        })

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    
    elif request.method == "POST":
        new_title = request.POST['title']
        description = request.POST['description']            
        util.save_entry(new_title, description)
        return redirect("entry_page", title=new_title)


def random_entry(request):
    entries = util.list_entries()
    rand_entry = random.choice(entries)
    return redirect("entry_page", title=rand_entry)


def edit(request, title):
    old_description = util.get_entry(title)
    if request.method == 'GET':
        return render(request, "encyclopedia/edit.html", {
            "old_title": title,
            "old_description": old_description
        })
    
    elif request.method == 'POST':
        new_description = request.POST['new_description']
        util.save_entry(title, new_description)
        return redirect("entry_page", title=title)


def search(request):
    if request.method == "POST":
        query = request.POST['q']
        result = util.get_entry(query) 
        if result:
            return redirect("entry_page", query)
        
        else:
            availible = util.list_entries()
            suggestions = []
            for i in availible:                              
                if query.lower() in i.lower():
                    suggestions.append(i)
            return render(request, "encyclopedia/search.html", {
                "suggestions": suggestions
            })
    else:
        return render(request, "encyclopedia/error.html")


