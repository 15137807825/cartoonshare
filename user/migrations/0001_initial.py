# Generated by Django 3.0.8 on 2020-08-21 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartoons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctitle', models.CharField(max_length=200)),
                ('cpub_date', models.DateField(blank=True, null=True)),
                ('cauth', models.CharField(max_length=200)),
                ('cimage', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'cartooninfo',
            },
        ),
        migrations.CreateModel(
            name='Cartoontype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.IntegerField()),
                ('typename', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'cartoontype',
            },
        ),
        migrations.CreateModel(
            name='CartoonUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_username', models.CharField(max_length=32, unique=True)),
                ('u_password', models.CharField(max_length=256)),
                ('u_email', models.CharField(max_length=64, unique=True)),
                ('is_active', models.IntegerField(default=1)),
                ('is_delete', models.IntegerField()),
            ],
            options={
                'db_table': 'cartoon_user',
            },
        ),
        migrations.CreateModel(
            name='ManageUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_username', models.CharField(max_length=32, unique=True)),
                ('u_password', models.CharField(max_length=256)),
                ('u_email', models.CharField(max_length=64, unique=True)),
                ('is_active', models.IntegerField(default=1)),
                ('is_delete', models.IntegerField()),
            ],
            options={
                'db_table': 'manage_user',
            },
        ),
        migrations.CreateModel(
            name='CartoonShow',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sinfo', models.CharField(max_length=5000)),
                ('shero', models.CharField(max_length=50)),
                ('cweb', models.CharField(max_length=2000)),
                ('cid', models.ForeignKey(blank=True, db_column='cid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.Cartoons')),
            ],
            options={
                'db_table': 'cartoonshow',
            },
        ),
        migrations.AddField(
            model_name='cartoons',
            name='ctype_id',
            field=models.ForeignKey(blank=True, db_column='tid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.Cartoontype'),
        ),
        migrations.CreateModel(
            name='Cartoonlike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_cartoons_num', models.IntegerField()),
                ('c_is_select', models.IntegerField()),
                ('c_cartoons', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='likes', to='user.Cartoons')),
                ('c_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.CartoonUser')),
            ],
            options={
                'db_table': 'cartoonlike',
            },
        ),
    ]
