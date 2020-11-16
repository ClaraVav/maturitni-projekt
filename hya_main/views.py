from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import ClanekForm, RegistraceForm, PrihlaseniForm, PostavaForm, PageForm, PageDeleteForm, PageUpdateForm
from .models import Clanek, Postava, Page


# Create your views here.
def clanek_list(request):
    clanky = Clanek.objects.filter(publikovano__lte=timezone.now()).order_by('-publikovano')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/clanek_list.html', {'clanky': clanky, 'postavy': postavy})


def clanek_detail(request, pk):
    clanek = get_object_or_404(Clanek, pk=pk)
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/clanek_detail.html', {'clanek': clanek, 'postavy': postavy})


def clanek_new(request):
    postavy = Postava.objects.order_by('prijmeni')
    IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
    if request.method == "POST":
        form = ClanekForm(request, request.POST, request.FILES)
        if form.is_valid:
            clanek = form.save()
            clanek.obrazek = request.FILES['obrazek']
            file_type = clanek.obrazek.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                print("Wrong type:", file_type)
            clanek.autor = request.user
            clanek.publikovano = timezone.now()
            clanek.save()
            return redirect('clanek_detail', pk=clanek.pk)
    else:
        form = ClanekForm()
    return render(request, 'hya_main/clanek_edit.html', {'form': form, 'postavy': postavy})


def clanek_delete(request, pk):
    clanek = get_object_or_404(Clanek, pk=pk)
    clanek.delete()


@login_required
def bazos(request):
    clanky = Clanek.objects.filter(publikovano__lte=timezone.now()).order_by('-publikovano')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/bazos_list.html', {'clanky': clanky, 'postavy': postavy})


@login_required
def internet(request):
    clanky = Clanek.objects.filter(publikovano__lte=timezone.now()).order_by('-publikovano')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/internet_list.html', {'clanky': clanky, 'postavy': postavy})


@login_required
def instablox(request):
    clanky = Clanek.objects.filter(publikovano__lte=timezone.now()).order_by('-publikovano')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/instablox_list.html', {'clanky': clanky, 'postavy': postavy})


@login_required
def bloxnews(request):
    clanky = Clanek.objects.filter(publikovano__lte=timezone.now()).order_by('-publikovano')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/blox_list.html', {'clanky': clanky, 'postavy': postavy})


@login_required
def uredka(request):
    clanky = Clanek.objects.filter(publikovano__lte=timezone.now()).order_by('-publikovano')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/uredka_list.html', {'clanky': clanky, 'postavy': postavy})


def pravidla(request):
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/pravidla.html', {'postavy': postavy})


def ateam(request):
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/ateam.html', {'postavy': postavy})


def galerie(request):
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/galerie.html', {'postavy': postavy})


def kontakt(request):
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/kontakt.html', {'postavy': postavy})


def special(request):
    return render(request, 'hya_main/clanek_list.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


def registr(request):
    if request.method == "POST":
        form = RegistraceForm(request.POST)
        name = request.POST.get('username')
        passw = request.POST.get('password1')
        if form.is_valid:
            osoba = form.save()
            uziv = authenticate(username=name, password=passw)
            osoba.save()
            login(request, uziv)
            return redirect('/')
    else:
        form = RegistraceForm()
    return render(request, 'hya_main/signup_screen.html', {'form': form})


def prihlas(request):
    if request.method == 'POST':
        form = PrihlaseniForm(request, request.POST)
        name = request.POST.get('username')
        passw = request.POST.get('password')
        if form.is_valid:
            osoba = authenticate(username=name, password=passw)
            login(request, osoba)
            return redirect('/')
    else:
        form = PrihlaseniForm()
    return render(request, 'hya_main/login_screen.html', {'form': form})


def profil(request):
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/profil.html', {'postavy': postavy})


def postava_new(request):
    postavy = Postava.objects.order_by('prijmeni')
    if request.method == "POST":
        form = PostavaForm(request.POST)
        if form.is_valid():
            postava = form.save(commit=False)
            postava.majitel = request.user
            postava.vytvoreno = timezone.now()
            postava.cele_jmeno = postava.full_jmeno()
            postava.save()
            return redirect('postava_detail', pk=postava.pk)
    else:
        form = PostavaForm()
    return render(request, 'hya_main/postava_new.html', {'form': form, 'postavy': postavy})


def postava_detail(request, pk):
    postava = get_object_or_404(Postava, pk=pk)
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/postava_detail.html', {'postava': postava, 'postavy': postavy})


def postava_delete(request, pk):
    postava = get_object_or_404(Postava, pk=pk)
    postava.delete()


def page_detail(request, urltitle):
    page = get_object_or_404(Page, urltitle=urltitle)
    return render(request, 'hya_main/page_detail.html', {'page': page})


@login_required
def page_new(request):
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid:
            page = form.save()
            page.author = request.user
            page.created_date = timezone.now()
            page.urltitle = page.urlify()
            page.save()
            return redirect('page_detail', urltitle=page.urltitle)
    else:
        form = PageForm()
    return render(request, 'hya_main/page_new.html', {'form': form})


@login_required
def page_edit(request, urltitle):
    page = get_object_or_404(Page, urltitle=urltitle)
    if request.method == "POST":
        form = PageUpdateForm(request.POST)
        if form.is_valid:
            page = form.save(commit=False)
            page.edited_date = timezone.now()
            page.urltitle = page.urlify()
            page.save()
            return redirect('page_detail', urltitle=page.urltitle)
    else:
        form = PageForm()
    return render(request, 'hya_main/page_edit.html', {'form': form, "page": page})


@login_required
def page_delete(request, urltitle):
    page = get_object_or_404(Page, urltitle=urltitle)
    if request.method == "POST":
        form = PageDeleteForm(request.POST)
        if form.is_valid:
            page = form.save(commit=False)
            page.deleted = True
            page.edited_date = timezone.now()
            page.save()
            return redirect('/')
    else:
        form = PageForm()
    return render(request, 'hya_main/page_delete.html', {'form': form, "page": page})

