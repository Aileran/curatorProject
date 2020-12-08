from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import AlbumForm, BookForm, MovieForm
from .models import Book, Movie, Album
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
# from django.contrib import messages


# @login_required decorator allows to limit access to the index page and check whether the user is authenticated
# if so, index page is rendered. If not, the user is redirected to the login page via login_url
@login_required(login_url='login')
def index(request):
    # Render the index page
    return render(request, 'curator/index.html')


def register_view(request):
    # This function renders the registration form page and create a new user based on the form data
    if request.method == 'POST':
        # We use Django's UserCreationForm which is a model created by Django to create a new user.
        # UserCreationForm has three fields by default: username (from the user model), password1, and password2.
        # If you want to include email as well, switch to our own custom form called UserRegistrationForm
        form = UserCreationForm(request.POST)
        # check whether it's valid: for example it verifies that password1 and password2 match
        if form.is_valid():
            form.save()
            # if you want to login the user directly after saving, use the following two lines instead, and redirect to index
            # user = form.save()
            # login(user)
            # redirect the user to login page so that after registration the user can enter the credentials
            return redirect('login')
    else:
        # Create an empty instance of Django's UserCreationForm to generate the necessary html on the template.
        form = UserCreationForm()
    return render(request, 'curator/register.html', {'form': form})


def login_view(request):
    # this function authenticates the user based on username and password
    # AuthenticationForm is a form for logging a user in.
    # if the request method is a post
    if request.method == 'POST':
        # Plug the request.post in AuthenticationForm
        form = AuthenticationForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            # get the user info from the form data and login the user
            user = form.get_user()
            login(request, user)
            # redirect the user to index page
            return redirect('index')
    else:
        # Create an empty instance of Django's AuthenticationForm to generate the necessary html on the template.
        form = AuthenticationForm()
    return render(request, 'curator/login.html', {'form': form})


def logout_view(request):
    # This is the method to logout the user
    logout(request)
    # redirect the user to index page
    return redirect('index')


def book(request):
    user = User.objects.get(username=request.user.username)
    user_books = Book.objects.filter(owner=user)
    return render(request, 'curator/book_collection.html', {"Books": user_books})
    # return render(request, 'curator/book_collection.html')


def movie(request):
    user = User.objects.get(username=request.user.username)
    user_movies = Movie.objects.filter(owner=user)
    return render(request, 'curator/movie_collection.html', {"Movies": user_movies})
    # return render(request, 'curator/movie_collection.html')


def album(request):
    user = User.objects.get(username=request.user.username)
    user_albums = Album.objects.filter(owner=user)
    return render(request, 'curator/album_collection.html', {"Albums": user_albums})
    # return render(request, 'curator/album_collection.html')


def delete_collection(request):
    return render(request, 'curator/delete.html')


def update_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form = BookForm()
        context = {'form': form}
        return render(request, 'curator/update.html', context)


def update_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie')
    else:
        form = MovieForm()
        context = {'form': form}
        return render(request, 'curator/update.html', context)


def update_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album')
    else:
        form = AlbumForm()
        context = {'form': form}
        return render(request, 'curator/update.html', context)