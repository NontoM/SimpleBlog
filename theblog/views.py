from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-post_date']
    ordering = ['-id']

    #pass context data into the page
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all() #get all data in Category model and assign it to cat_menu variable
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cats): #cats from url
    category_posts = Post.objects.filter(category__iexact=cats.replace('-', ' ')) #replace category - with a space, ilter using __iexact  which takes all the arguments ignoring upper and lower case
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})
    #cats.title(), title case


#querying database to grab all Category data(names), assigning to cat_menu_lis variable,passing that variable into our context dictionary, we can now access to this page
def CategoryListView(request): #cats from url
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})
    #cats.title(), title case

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

 #pass context data into the page
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all() #get all data in Category model and assign it to cat_menu variable
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'


class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
  
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
