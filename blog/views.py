from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import CreateBlogForm
from blog.models import Blog, Subscription
from blog.tasks import send_blog_email


class BlogsView(ListView):
    model = Blog
    template_name = 'blog/blogs.html'


class BlogView(DetailView):
    model = Blog
    template_name = 'blog/blog.html'


class CreateSubscriptionView(CreateView):
    model = Subscription
    fields = '__all__'
    template_name = 'blog/blogs.html'
    success_url = reverse_lazy('blogs')


@login_required
def blog_create_view(request):
    form = CreateBlogForm()
    if request.method == "POST":
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            send_blog_email.delay(blog.title, "Hello sir, hope you do well, we are glad to present you our new blog"
                                              "you can read it here: "
                                              f"https://{request.get_host()}{blog.get_absolute_url()}")
            return redirect('blogs')

    return render(request, 'blog/create-blog.html', context={'form': form})
