from .models import Category

def menu_links(request):
    #fetch all links from database
    links = Category.objects.all()
    #return list of category object in dictionary
    return dict(links=links)
