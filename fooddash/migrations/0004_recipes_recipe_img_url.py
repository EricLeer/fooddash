# Generated by Django 2.1.5 on 2019-11-24 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddash', '0003_recipes'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='recipe_img_url',
            field=models.CharField(default='https://www.takeoutlist.com/assets/images/food_default.png', max_length=200),
        ),
    ]
