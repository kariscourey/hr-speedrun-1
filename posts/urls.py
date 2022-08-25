from django.urls import path
from posts.views import show_posts

# This file defines patterns for the REST of the url (after what was already defined in urls.py)
urlpatterns = [
    # https://localhost:8000/posts  # /posts has already matched from other urls.py
    path('', show_posts, name="show_posts")  # putting name of fn, not calling it
]

# passing function show_posts to path
# handing path a copy of a function as you would a variable
# we want django to call our function, not us
