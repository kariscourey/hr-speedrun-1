from django.shortcuts import render
from posts.models import Post

# Create your views here.
def show_posts(request):  # django will call show_posts() for us; request instace is an object
    # print("HELLO")
    # print(request)  # if you don't return anything, browser will "hang"
    #     # WSGI request


    # fetch posts from the model
    posts = Post.objects.all()

    # put data about posts into context
    context = {  # variables available to you in template
    'message': 'hello world',
    'posts': posts,
    }

    # render and return html template
    return render(request, 'posts.html', context)
        # request, string of template from templates folder, dictionary
