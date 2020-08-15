from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('admin_panel_settings', '0002_options_valid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('position', models.CharField(default='left', max_length=255, verbose_name='Menu Position')),
                ('link_type',
                 models.IntegerField(choices=[(0, 'Internal'), (1, 'External')], default=0, verbose_name='Link Type')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Link')),
                ('icon', models.CharField(blank=True, max_length=255, null=True, verbose_name='Icon')),
                ('valid', models.BooleanField(default=True, verbose_name='Valid')),
                ('content_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE,
                                                   to='contenttypes.ContentType', verbose_name='ContentType')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menu Setting',
            },
        ),
    ]
