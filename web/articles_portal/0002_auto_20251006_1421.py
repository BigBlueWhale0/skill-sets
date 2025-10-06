from django.db import migrations


def create_superuser(apps, schema_editor):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if User.objects.exists():
        return
    superuser = User.objects.create_superuser(
        username="superdupeduser",
        email="superdupeduser@mail.com",
        password="superdupeduser",
        last_login=timezone.now()
    )
    superuser.save()

operations = [
    migrations.RunPython(create_superuser)
]

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
    ]
