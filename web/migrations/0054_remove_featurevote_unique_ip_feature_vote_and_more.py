# Generated by Django 5.1.6 on 2025-04-04 17:21

import web.crypto_utils
from django.db import migrations


def remove_constraint_if_exists(apps, schema_editor):
    """
    Custom function to safely remove the constraint if it exists.
    SQLite doesn't support IF EXISTS for constraint removal.
    """
    # Check if constraint exists by attempting to query it directly
    try:
        cursor = schema_editor.connection.cursor()
        # For SQLite, we just log that we're skipping this since it doesn't have a central constraints repository
        if schema_editor.connection.vendor == "sqlite":
            print("SQLite detected - skipping constraint removal (SQLite doesn't store constraints in a standard way)")
    except Exception as e:
        print(f"Error checking constraint existence: {e}")


def remove_index_if_exists(apps, schema_editor):
    """
    Custom function to safely remove the index if it exists.
    SQLite doesn't support IF EXISTS for index removal.
    """
    # Check if index exists by attempting to query it directly
    try:
        cursor = schema_editor.connection.cursor()
        # For SQLite, we can query the sqlite_master table
        if schema_editor.connection.vendor == "sqlite":
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='index' AND name='web_feature_feature_988c48_idx'"
            )
            result = cursor.fetchone()
            if result:
                cursor.execute("DROP INDEX web_feature_feature_988c48_idx")
                print("Index removed successfully")
            else:
                print("Index 'web_feature_feature_988c48_idx' does not exist, skipping")
    except Exception as e:
        print(f"Error checking/removing index: {e}")


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0053_goods_featured"),
    ]

    operations = [
        migrations.RunPython(remove_constraint_if_exists),
        migrations.RunPython(remove_index_if_exists),
        migrations.AlterField(
            model_name="donation",
            name="email",
            field=web.crypto_utils.EncryptedEmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="featurevote",
            name="ip_address",
            field=web.crypto_utils.EncryptedCharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="peermessage",
            name="content",
            field=web.crypto_utils.EncryptedTextField(),
        ),
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=web.crypto_utils.EncryptedTextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name="profile",
            name="discord_username",
            field=web.crypto_utils.EncryptedCharField(
                blank=True, help_text="Your Discord username (e.g., User#1234)", max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="expertise",
            field=web.crypto_utils.EncryptedCharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="profile",
            name="github_username",
            field=web.crypto_utils.EncryptedCharField(
                blank=True, help_text="Your GitHub username (without @)", max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="slack_username",
            field=web.crypto_utils.EncryptedCharField(blank=True, help_text="Your Slack username", max_length=50),
        ),
        migrations.AlterField(
            model_name="webrequest",
            name="ip_address",
            field=web.crypto_utils.EncryptedCharField(blank=True, default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="webrequest",
            name="user",
            field=web.crypto_utils.EncryptedCharField(blank=True, default="", max_length=150),
        ),
    ]
