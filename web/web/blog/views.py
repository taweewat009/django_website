from email.policy import default
from django.shortcuts import render,get_object_or_404,redirect
from category.models import Category
from .models import Blogs, Customer, PhotoAlbum  ,Comment 
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.core.mail import send_mail
from .forms import CommentForm,CustomerForm




# Create your views here.

def index(request,category_slug=None):
    blogs = None
    category_page = None
    if category_slug != None:
        category_page=get_object_or_404(Category,slug=category_slug)
        blogs = Blogs.objects.all().filter(category=category_page)
    else:
        blogs = Blogs.objects.all()
    
    # Pagination
    paginator = Paginator(blogs,9)
    try:
        page = int(request.GET.get('page',1))
    except:
        page = 1
    try:
        blogsperpage = paginator.page(page)
    except (EmptyPage,InvalidPage):
        blogperpage = paginator.page(paginator.num_pages)
      
    return render(request, 'index.html',{'blogs':blogsperpage,'category':category_page})

def index2(request,category_slug=None):
    blogs = None
    category_page = None
    if category_slug != None:
        category_page=get_object_or_404(Category,slug=category_slug)
        blogs = Blogs.objects.all().filter(category=category_page)
    else:
        blogs = Blogs.objects.all()
    
    # Pagination
    paginator = Paginator(blogs,6)
    try:
        page = int(request.GET.get('page',1))
    except:
        page = 1
    try:
        blogsperpage = paginator.page(page)
    except (EmptyPage,InvalidPage):
        blogperpage = paginator.page(paginator.num_pages)
      
    return render(request, 'index2.html',{'blogs':blogsperpage,'category':category_page})


def blogdetail(request,slug): 
    template_name = 'blogdetail.html'
    blogdetail = Blogs.objects.get(slug=slug)
    post = get_object_or_404(Blogs,slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    
    if request.method == 'POST':
        
        form = CommentForm(data= request.POST)
        
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
                                    
    else:
        form = CommentForm()
    
    return render(request,template_name,{'blogdetail':blogdetail,'form':form,'post':post,'new_comment':new_comment,'comments':comments})

    '''  
    try:
        blogdetail = Blogs.objects.get(category__slug=category_slug,slug=post_slug)
        blogdetail.views = blogdetail.views + 1
        blogdetail.save()
        page = blogdetail.id
        comment = Comment.objects.filter(post=page)
          
         
    except Exception as e :
        raise e
    ''' 
    
    
    ''' 
    blogdetail = Blogs.objects.get(slug=slug)
    blogdetail.views = blogdetail.views + 1
    blogdetail.save()
    return render(request,'blogdetail.html',{'blogdetail':blogdetail})
    '''

    '''  
    #def searchCategory(request,category_slug):
        categories = Category.objects.all()
        search = Blogs.objects.filter(slug=category_slug)
        blogs = Blogs.objects.all()
        last = Blogs.objects.all().order_by('-pk')[:1]
        template_name = 'searchcategory.html'

        return render(request,'searchcategory.html',{'search':search,'categories':categories,'last':last,'blogs':blogs,'template_name':template_name})
    '''

def about(request):
    photos = PhotoAlbum.objects.all()
    return render(request, 'bootstrap_templates/index.html',{'photos':photos})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            ['krutaweewat@gmail.com'], #to email
        ) 
        
        return render(request, 'bootstrap_templates/index.html',{'message_name':message_name})
    else:
        return render(request, 'bootstrap_templates/index.html')
    

def onlyme(request):
    return render(request,'onlyme.html' )


def sendwork(request):
    return render(request,'sendwork.html')

def sponsor(request):
    return render(request,'ads.txt')


def test_form(request):
    post = Customer.objects.all()
    form = CustomerForm()
    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.post = post 
            a.save()
    
    context = {'form':form,
               'post':post}
    return render(request,'test.html',context)



