from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from unidecode import unidecode
from django.template.defaultfilters import slugify
from .forms import *
from .models import *


# Create your views here.
def clanek_list(request):
    clanky = Clanek.objects.filter(vytvoreno__lte=timezone.now()).order_by('-vytvoreno')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/clanek_list.html', {'clanky': clanky, 'postavy': postavy})


def clanek_detail(request, slug):
    clanek = get_object_or_404(Clanek, slug=slug)
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/clanek_detail.html', {'clanek': clanek, 'postavy': postavy})


@login_required
def clanek_new(request):
    postavy = Postava.objects.order_by('prijmeni')
    IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
    if request.method == "POST":
        form = ClanekForm(request, request.POST, request.FILES)
        pic = request.FILES or None
        if form.is_valid:
            clanek = form.save()
            clanek.slug = slugify(unidecode(clanek.titulek))
            slug = clanek.slug
            clanek.obrazek = pic
            if pic:
                file_type = clanek.obrazek.url.split('.')[-1]
                file_type = file_type.lower()
                if file_type not in IMAGE_FILE_TYPES:
                    print("Wrong type:", file_type)
            clanek.autor = request.user
            clanek.vytvoreno = timezone.now()
            clanek.save()
            messages.success(request, 'Článek úspěšně vytvořen..')
            return redirect('clanek_detail', slug=slug)
        else:
            messages.error(request, 'Chyba při vytváření článku..')
    else:
        form = ClanekForm()
    return render(request, 'hya_main/clanek_edit.html', {'form': form, 'postavy': postavy})


def clanek_delete(request, pk):
    clanek = get_object_or_404(Clanek, pk=pk)
    clanek.delete()


@login_required
def bazos(request):
    clanky = Clanek.objects.filter(vytvoreno__lte=timezone.now()).order_by('-vytvoreno')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/bazos_list.html', {'clanky': clanky, 'postavy': postavy})


@login_required
def internet(request):
    clanky = Clanek.objects.filter(vytvoreno__lte=timezone.now()).order_by('-vytvoreno')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/internet_list.html', {'clanky': clanky, 'postavy': postavy})


@login_required
def instablox(request):
    clanky = Clanek.objects.filter(vytvoreno__lte=timezone.now()).order_by('-vytvoreno')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/instablox_list.html', {'clanky': clanky, 'postavy': postavy})


@login_required
def bloxnews(request):
    clanky = Clanek.objects.filter(vytvoreno__lte=timezone.now()).order_by('-vytvoreno')
    postavy = Postava.objects.order_by('prijmeni')
    return render(request, 'hya_main/blox_list.html', {'clanky': clanky, 'postavy': postavy})


@login_required
def uredka(request):
    clanky = Clanek.objects.filter(vytvoreno__lte=timezone.now()).order_by('-vytvoreno')
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
            try:
                login(request, uziv)
            except AttributeError:
                messages.error(request, 'Chyba při přihlašování u registrace')
                return redirect('/registrace')
            return redirect('/')
        else:
            messages.error(request, 'Chyba při registraci')
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
            try:
                login(request, osoba)
            except AttributeError:
                messages.error(request, 'Jméno či heslo není správné')
                return redirect('/prihlaseni')
            return redirect('/')
        else:
            messages.error(request, 'Chyba při přihlášení')
    else:
        form = PrihlaseniForm()
    return render(request, 'hya_main/login_screen.html', {'form': form})


@login_required
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
            messages.success(request, 'Postava úspěšně vytvořena')
            return redirect('postava_detail', pk=postava.pk)
        else:
            messages.error(request, 'Chyba při vytváření postavy')
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
            messages.success(request, 'Stránka úspěšně vytvořena')
            return redirect('page_detail', urltitle=page.urltitle)
        else:
            messages.error(request, 'Chyba při vytváření stránky')
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
    return render(request, 'hya_main/page_delete.html', {'form': form, 'page': page})


@login_required
def chat(request):
    postavy = Postava.objects.order_by('prijmeni')
    zpravy = Zprava.objects.order_by('odeslano')
    return render(request, 'hya_main/chat.html', {'postavy': postavy, 'zpravy': zpravy})


@login_required
def zprava_new(request):
    postavy = Postava.objects.order_by('prijmeni')
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid:
            msg = form.save(commit=False)
            msg.tvurce = request.user
            msg.odeslano = timezone.now()
            msg.save()
            messages.success(request, 'Zpráva úspěšně odeslána')
        else:
            messages.error(request, 'Chyba při odesílání zprávy')
            return redirect('/nova-zprava')
        return redirect('/chat')
    else:
        form = MessageForm()
    return render(request, 'hya_main/new-message.html', {'postavy': postavy, 'form': form})


@login_required
def zprava_detail(request, id):
    postavy = Postava.objects.order_by('prijmeni')
    zpravy = Zprava.objects.order_by('odeslano')
    msg = get_object_or_404(Zprava, id=id)
    return render(request, 'hya_main/chat-zprava.html', {'postavy': postavy, 'zpravy': zpravy, 'message': msg})
