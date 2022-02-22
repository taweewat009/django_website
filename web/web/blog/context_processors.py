from category.models import Category
from .models import Blogs



def category_link(request):
    links = Category.objects.all()
    last = Blogs.objects.all().order_by('-pk')
    return dict(link=links)


def last_blog(request):
    last = Blogs.objects.all().order_by('-pk')[:4]
    blogs = Blogs.objects.all()
    return dict(last=last,blogs=blogs)



