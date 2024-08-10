from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_add_created_updated_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
