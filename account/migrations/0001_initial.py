# Generated by Django 3.1 on 2020-09-07 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email адрес')),
                ('organisation', models.CharField(max_length=100, verbose_name='Организация')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserResultDigitalization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='')),
                ('digitalization', models.IntegerField(blank=True, null=True, verbose_name='Цифровизация')),
                ('digit_value_main_bp', models.IntegerField(blank=True, null=True, verbose_name='Цифровизация основных БП')),
                ('digit_value_manage_bp', models.IntegerField(blank=True, null=True, verbose_name='Цифровизация БП управления')),
                ('digit_value_auxiliary_bp', models.IntegerField(blank=True, null=True, verbose_name='Цифровизация вспомогательных БП')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Результат измерений',
                'verbose_name_plural': 'Результаты измерений',
            },
        ),
        migrations.CreateModel(
            name='IndicatorManageBP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Частный показатель БП управления')),
                ('value_of_indicator', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Значение частного показателя')),
                ('total_digitalization_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userresultdigitalization', verbose_name='Показатель БП управления')),
            ],
            options={
                'verbose_name': 'Частный показатель БП управления',
                'verbose_name_plural': 'Частные показатели БП управления',
            },
        ),
        migrations.CreateModel(
            name='IndicatorMainBP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Частный показатель основных БП')),
                ('value_of_indicator', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Значение частного показателя')),
                ('total_digitalization_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userresultdigitalization', verbose_name='Показатели основных БП')),
            ],
            options={
                'verbose_name': 'Частный показатель основных БП',
                'verbose_name_plural': 'Частные показатели основных БП',
            },
        ),
        migrations.CreateModel(
            name='IndicatorAuxiliaryBP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Частный показатель БП управления')),
                ('value_of_indicator', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Значение частного показателя')),
                ('total_digitalization_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userresultdigitalization', verbose_name='Показатель вспомогальных БП')),
            ],
            options={
                'verbose_name': 'Частный показатель вспомогательных БП',
                'verbose_name_plural': 'Частные показатели вспомогательных БП',
            },
        ),
        migrations.CreateModel(
            name='Depatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Не выбрано', 'Не выбрано'), ('Образование', 'Образование'), ('Наука', 'Наука'), ('Здравоохранение', 'Здравоохранение'), ('Нефтехимическая промышленность', 'Нефтехимическая промышленность'), ('Промышленность', 'Промышленность'), ('Легкая промышленность', 'Легкая промышленность'), ('Пищевая промышленность', 'Пищевая промышленность'), ('Траснпорт и коммуникации', 'Траснпорт и коммуникации'), ('Лесное хозяйство', 'Лесное хозяйство'), ('Сельское хозяйство', 'Сельское хозяйство'), ('Архитектура и строительство', 'Архитектура и строительство'), ('Энергетика', 'Энергетика'), ('Связь и информатизация', 'Связь и информатизация'), ('Природные ресурсы и охрана окружающей среды', 'Природные ресурсы и охрана окружающей среды')], max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отрасль/функциональная сфера',
                'verbose_name_plural': 'Отрасли/функциональные сферы',
            },
        ),
    ]
