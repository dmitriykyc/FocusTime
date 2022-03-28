# Generated by Django 3.2.11 on 2022-03-28 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socnetwapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commentapp.comments', verbose_name='Номер родительского коммента')),
                ('parent_user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_user', to=settings.AUTH_USER_MODEL, verbose_name='Кому отвечаем на комент')),
                ('to_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_post_comment', to='socnetwapp.posttothefeed', verbose_name='Комментарий к этому посту')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Коментарий от пользователя')),
            ],
            options={
                'verbose_name': 'Коментарии',
            },
        ),
    ]
