from django.http import Http404
from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from MainApp.models import Snippet
from MainApp.forms import SnippetForm, UserRegistrationForm, CommentForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета', "form": form}
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":  # информацию от формы
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            return redirect("snippets-list")


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        "snippets": snippets
    }
    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request, id):
    snippet = get_object_or_404(Snippet, id=id)
    form = CommentForm()
    context = {
        'pagename': 'Подробнее о сниппете',
        "snippet": snippet,
        "form": form
    }
    return render(request, 'pages/snippet_detail.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            pass
    return redirect(request.META.get('HTTP_REFERER', '/'))


def logout(request):
    auth.logout(request)
    return redirect('home')


def register(request):
    if request.method == "GET":
        form = UserRegistrationForm()
        context = {'pagename': 'Регистрация пользователя', "form": form}
        return render(request, 'pages/registration.html', context)
    if request.method == "POST":  # информацию от формы
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        context = {'pagename': 'Регистрация пользователя', "form": form}
        return render(request, 'pages/registration.html', context)


def comment_add(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        snippet_id = request.POST.get("snippet_id")
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.snippet = Snippet.objects.get(id=snippet_id)
            comment.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))

    raise Http404