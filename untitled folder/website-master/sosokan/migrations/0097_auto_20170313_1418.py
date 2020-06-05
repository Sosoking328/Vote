# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-13 18:18
from __future__ import unicode_literals

from django.db import migrations



def update_usernames(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Profile = apps.get_model("sosokan", "UserProfile")
    for profile in Profile.objects.all():
    	if profile.user.username is None:
        	profile.user.username = profile.user.email
        	profile.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sosokan', '0096_auto_20170306_1751'),
    ]

    operations = [
    	migrations.RunPython(update_usernames),
    ]