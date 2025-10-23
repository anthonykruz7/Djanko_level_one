from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm  # Make sure forms.py exists!

# Home page — list all posts
def home(request):
    posts = Post.objects.all().order_by('-created_at')  # newest first
    return render(request, 'posts/home.html', {'posts': posts})


# Create a new post
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'posts/post_form.html', {
        'form': form,
        'form_type': 'create'
    })


# View post details
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


# Edit an existing post
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('details', pk=post.pk)  # ✅ Make sure your URL name is 'details'
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/post_form.html', {
        'form': form,
        'form_type': 'edit',
        'post': post
    })


# Delete a post
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'posts/delete_post.html', {'post': post})



