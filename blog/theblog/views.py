from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from unicodedata import category
from django.http import HttpResponseRedirect
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CategoryForm, CommentForm

def CategoryView(request,cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categories.html',{'cats':cats.title().replace('-',' '), 'category_posts':category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html',{'cat_menu_list':cat_menu_list})

def LikeView(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    liked= False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked= True

    return HttpResponseRedirect(reverse('article-details',args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #this orders list accordingly like -id means latest first
    #ordering = ['-id']
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data( *args, **kwargs)
        context['cat_menu']= cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name= 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data( *args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked= False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True


        header_image_url = stuff.header_image.url if stuff.header_image else None
        context['cat_menu']= cat_menu
        context['total_likes']= total_likes
        context['liked'] = liked
        context['header_image_url'] = header_image_url
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(reverse('article-details', args=[str(self.object.pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.post_id= self.kwargs['pk']
        return super().form_valid(form)


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'
    success_url = reverse_lazy('home')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title','title_tag','body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


