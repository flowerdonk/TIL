from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.decorators import login_required

@require_safe
def index(request):
    articles = Article.objects.all()
    context = { 'articles' : articles }
    return render(request, 'articles/index.html', context)

@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article' : article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {
        'form' : form,
        'article' : article,
    }
    return render(request, 'articles/update.html', context)

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def comments_create(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk = pk)
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment_form.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')