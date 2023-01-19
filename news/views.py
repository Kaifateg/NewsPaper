from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .filters import *
from .forms import *
from .models import *

class PostNews(ListView):
    template_name = 'post_news.html'
    context_object_name = 'postnews'
    queryset = Post.objects.all()
    ordering = '-time_create_post'
    paginate_by = 10


class PostNW(DetailView):
    queryset = Post.objects.all()
    template_name = 'post_nw.html'
    context_object_name = 'postnw'


class PostFilters(ListView):
    model = Post
    template_name = 'post_filter.html'
    context_object_name = 'postfilter'
    ordering = 'name_news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type_category = 'NW'
        return super().form_valid(form)


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type_category = 'AR'
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_info')


class CategoryListViev(PostNews):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_post'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-time_create_post')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_follower'] = self.request.user not in self.category.follower.all()
        context['category'] = self.category
        return context

@login_required
def follow(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.follower.add(user)

    message = 'You successfully follow on category'
    return render(request, 'follow.html', {'category': category, 'message': message})