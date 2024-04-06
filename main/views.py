from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView
from .forms import NewsForm, RegisterForm
from .models import News
from django.http import Http404
from transliterate import translit
from django.contrib.auth.models import User, Group
import random, string
from django.db.utils import IntegrityError

def create_view(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("news")
        else:
            error = 'Не верна форма'

    form = NewsForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/news/create_news.html', context)

def new_date(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            User.objects.filter(username=request.user.username).update(first_name=first_name, last_name=last_name)

            return redirect("profile")



        return render(request, 'main/new_date.html')
    else:
        redirect('login')


def news(request):
    pagintator = Paginator(News.objects.all(), 4)
    news_list = pagintator.get_page(request.GET.get('news', 1))
    context = {
        'news_list': news_list
    }
    return render(request, 'main/news/news.html', context)

class NewsDetailView(DetailView):
    template_name = "main/news/news_get.html"
    model = News
    context_object_name = 'data'

@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def new_user(request):
    context = {
        'klass': {
            '9A': '9A',
            '9B': '9B',
            '9V': '9V',
            '10A': '10A',
            '10B': '10B',
            '10V': '10V',
            '11A': '11A',
            '11B': '11B',
            '11V': '11V',
        }

    }
    return render(request, 'main/new_user.html', context)

def new_user_slug(request, cat):
        if request.user.is_staff:
            if request.method == 'POST':
                a = translit(request.POST['text'], language_code='ru', reversed=True).split()
                b = request.POST['text'].split()
                i = 0
                while i < len(a)-1:
                    password = ''.join([str(random.randint(1, 9)) for _ in range(7)]) + random.choice(string.ascii_uppercase)
                    login = a[i]+a[i+1][:1]
                    try:
                        user = User.objects.create_user(username=login, email=password, password=password, first_name=b[i], last_name=b[i+1])
                        user.save()
                    except IntegrityError:
                        user = User.objects.create_user(username=login+'1', email=password, password=password, first_name=b[i], last_name=b[i + 1])
                        user.save()
                    group = Group.objects.get(name=cat)
                    group.user_set.add(user)
                    i += 2

            users = User.objects.filter(groups__name=cat)
            context = {
                'users': users,
                'klass': translit(cat, language_code='ru')
            }
            return render(request, 'main/new_user_slug.html', context)
        else:
            raise Http404()

