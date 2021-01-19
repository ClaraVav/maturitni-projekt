from django.db import models
from django.conf import settings
from django.utils import timezone
from .customfields import TagField

# Create your models here.


class Page(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50, primary_key=True)
    urltitle = models.CharField(max_length=50, null=True)
    tags = TagField()
    created_date = models.DateTimeField(default=timezone.now)
    edited_date = models.DateTimeField(default=timezone.now, null=True)
    content = models.TextField(null=False)
    deleted = models.BooleanField(default=False)

    def publish(self):
        self.edited_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def urlify(self):
        safe = self.title
        for a in self.title:
            if a == " ":
                a = "_"
        self.urltitle = self.title
        self.title = safe
        return self.urltitle


class Clanek(models.Model):
    KATEGORIE = (
        (1, 'Inzeráty'),
        (2, 'Noviny'),
        (3, 'InstaBlox'),
        (4, 'Internet'),
        (5, 'Úřední deska'),
    )

    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False)
    postava = models.ForeignKey('hya_main.Postava', on_delete=models.CASCADE, null=True,
                                verbose_name="Postava jako autor")
    titulek = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField()
    obsah = models.TextField()
    vytvoreno = models.DateTimeField(default=timezone.now)
    kategorie = models.IntegerField(default=1, choices=KATEGORIE)
    obrazek = models.FileField(upload_to='obrazky/', null=True)

    class Meta:
        verbose_name_plural = 'Clanky'

    def publish(self):
        self.publikovano = timezone.now()
        self.save()

    def __str__(self):
        return self.titulek


class Postava(models.Model):
    majitel = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False)
    vytvoreno = models.DateTimeField(blank=False, null=True, verbose_name="Vytvořeno")
    jmeno = models.CharField(max_length=30, null=False, verbose_name="Křestní jméno")
    prijmeni = models.CharField(max_length=50, null=False, verbose_name="Příjmení")
    narozeni = models.DateField(null=False, verbose_name="Datum narození")
    narodnost = models.CharField(max_length=20, default='Česká', verbose_name="Národnost")
    vyska = models.IntegerField(default=180, null=True, verbose_name="Výška")
    nabozenstvi = models.CharField(max_length=20, null=True, verbose_name="Vyznání")
    politika = models.CharField(max_length=20, null=True, verbose_name="Politická orientace")
    vzdelani = models.CharField(max_length=50, null=True, verbose_name="Vzdělání")
    rodice = models.CharField(max_length=70, null=True, verbose_name="Rodiče")
    jazyky = models.CharField(max_length=70, null=True, verbose_name="Jazyky")
    hobby = models.CharField(max_length=50, null=True, verbose_name="Koníčky")
    bio = models.TextField(null=False, verbose_name="Životopis")
    cele_jmeno = models.CharField(max_length=81)

    class Meta:
        verbose_name_plural = 'Postavy'

    def vytvoreni(self):
        self.vytvoreno = timezone.now()
        self.save()

    def full_jmeno(self):
        self.cele_jmeno = self.jmeno + " " + self.prijmeni
        self.save()
        return self.cele_jmeno


class Zprava(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    tvurce = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    odesilatel = models.ForeignKey('hya_main.Postava', on_delete=models.CASCADE, verbose_name="Odesílatel",
                                   related_name="odesilatel")
    prijemce = models.ForeignKey('hya_main.Postava', on_delete=models.CASCADE, verbose_name="Příjemce",
                                 related_name="prijemce")
    predmet = models.CharField(max_length=50, null=False, verbose_name="Předmět")
    obsah = models.TextField(null=False, verbose_name="Obsah")
    odeslano = models.DateTimeField(null=False, blank=True, default=timezone.now)
    precteno = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Zpravy'

    def send(self):
        self.odeslano = timezone.now()
        self.save()
