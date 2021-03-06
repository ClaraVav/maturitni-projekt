# Generated by Django 2.2.13 on 2021-01-08 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import hya_main.customfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Postava',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vytvoreno', models.DateTimeField(null=True, verbose_name='Vytvořeno')),
                ('jmeno', models.CharField(max_length=30, verbose_name='Křestní jméno')),
                ('prijmeni', models.CharField(max_length=50, verbose_name='Příjmení')),
                ('narozeni', models.DateField(verbose_name='Datum narození')),
                ('narodnost', models.CharField(default='Česká', max_length=20, verbose_name='Národnost')),
                ('vyska', models.IntegerField(default=180, null=True, verbose_name='Výška')),
                ('nabozenstvi', models.CharField(max_length=20, null=True, verbose_name='Vyznání')),
                ('politika', models.CharField(max_length=20, null=True, verbose_name='Politická orientace')),
                ('vzdelani', models.CharField(max_length=50, null=True, verbose_name='Vzdělání')),
                ('rodice', models.CharField(max_length=70, null=True, verbose_name='Rodiče')),
                ('jazyky', models.CharField(max_length=70, null=True, verbose_name='Jazyky')),
                ('hobby', models.CharField(max_length=50, null=True, verbose_name='Koníčky')),
                ('bio', models.TextField(verbose_name='Životopis')),
                ('cele_jmeno', models.CharField(max_length=81)),
                ('majitel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Postavy',
            },
        ),
        migrations.CreateModel(
            name='Zprava',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('predmet', models.CharField(max_length=50, verbose_name='Předmět')),
                ('obsah', models.TextField(verbose_name='Obsah')),
                ('odeslano', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('precteno', models.BooleanField(default=False)),
                ('odesilatel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='odesilatel', to='hya_main.Postava', verbose_name='Odesílatel')),
                ('prijemce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prijemce', to='hya_main.Postava', verbose_name='Příjemce')),
                ('tvurce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Zpravy',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('urltitle', models.CharField(max_length=50, null=True)),
                ('tags', hya_main.customfields.TagField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('content', models.TextField()),
                ('deleted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Clanek',
            fields=[
                ('titulek', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('obsah', models.TextField()),
                ('vytvoreno', models.DateTimeField(default=django.utils.timezone.now)),
                ('kategorie', models.IntegerField(choices=[(1, 'Inzeráty'), (2, 'Noviny'), (3, 'InstaBlox'), (4, 'Internet'), (5, 'Úřední deska')], default=1)),
                ('obrazek', models.FileField(null=True, upload_to='obrazky/')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('postava', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hya_main.Postava', verbose_name='Postava jako autor')),
            ],
            options={
                'verbose_name_plural': 'Clanky',
            },
        ),
    ]
