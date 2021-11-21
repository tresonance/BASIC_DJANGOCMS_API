# Generated by Django 3.1.13 on 2021-11-21 01:58

import aldryn_apphooks_config.fields
import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image
import myblog.models
import parler.fields
import parler.models
import sortedm2m.fields
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('cms', '0022_auto_20180620_1551'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms_myblog', '0001_initial'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('filer', '0014_folder_permission_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('app_config', aldryn_apphooks_config.fields.AppHookConfigField(help_text='When selecting a value, the form is reloaded to get the updated default', null=True, on_delete=django.db.models.deletion.CASCADE, to='cms_myblog.blogconfig', verbose_name='app. config')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='myblog.blogcategory', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'blog category',
                'verbose_name_plural': 'blog categories',
            },
            bases=(myblog.models.BlogMetaMixin, parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('date_published', models.DateTimeField(blank=True, null=True, verbose_name='published since')),
                ('date_published_end', models.DateTimeField(blank=True, null=True, verbose_name='published until')),
                ('date_featured', models.DateTimeField(blank=True, null=True, verbose_name='featured date')),
                ('publish', models.BooleanField(default=False, verbose_name='publish')),
                ('enable_comments', models.BooleanField(default=True, verbose_name='enable comments on post')),
                ('enable_liveblog', models.BooleanField(default=False, verbose_name='enable liveblog on post')),
                ('app_config', aldryn_apphooks_config.fields.AppHookConfigField(help_text='When selecting a value, the form is reloaded to get the updated default', null=True, on_delete=django.db.models.deletion.CASCADE, to='cms_myblog.blogconfig', verbose_name='app. config')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='myblog_post_author', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('categories', models.ManyToManyField(blank=True, related_name='blog_posts', to='myblog.BlogCategory', verbose_name='category')),
                ('content', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_content', slotname='post_content', to='cms.placeholder')),
                ('liveblog', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='live_blog', slotname='live_blog', to='cms.placeholder')),
                ('main_image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='myblog_post_image', to=settings.FILER_IMAGE_MODEL, verbose_name='main image')),
                ('main_image_full', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='myblog_post_full', to='filer.thumbnailoption', verbose_name='main image full')),
                ('main_image_thumbnail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='myblog_post_thumbnail', to='filer.thumbnailoption', verbose_name='main image thumbnail')),
                ('media', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media', slotname='media', to='cms.placeholder')),
                ('related', sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='myblog.Post', verbose_name='Related Posts')),
                ('sites', models.ManyToManyField(blank=True, help_text='Select sites in which to show the post. If none is set it will be visible in all the configured sites.', to='sites.Site', verbose_name='Site(s)')),
                ('tags', taggit_autosuggest.managers.TaggableManager(blank=True, help_text='Type a tag and hit tab, or start typing and select from autocomplete list.', related_name='myblog_tags', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'blog article',
                'verbose_name_plural': 'blog articles',
                'ordering': ('-date_published', '-date_created'),
                'get_latest_by': 'date_published',
            },
            bases=(myblog.models.KnockerModel, myblog.models.BlogMetaMixin, parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='LatestPostsPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='myblog_latestpostsplugin', serialize=False, to='cms.cmsplugin')),
                ('current_site', models.BooleanField(default=True, help_text='Select items from the current site only', verbose_name='current site')),
                ('template_folder', models.CharField(choices=[('plugins', 'Default template')], default='plugins', help_text='Select plugin template to load for this instance', max_length=200, verbose_name='Plugin template')),
                ('latest_posts', models.IntegerField(default=5, help_text='The number of latests articles to be displayed.', verbose_name='articles')),
                ('app_config', aldryn_apphooks_config.fields.AppHookConfigField(blank=True, help_text='When selecting a value, the form is reloaded to get the updated default', null=True, on_delete=django.db.models.deletion.CASCADE, to='cms_myblog.blogconfig', verbose_name='app. config')),
                ('categories', models.ManyToManyField(blank=True, help_text='Show only the blog articles tagged with chosen categories.', to='myblog.BlogCategory', verbose_name='filter by category')),
                ('tags', taggit_autosuggest.managers.TaggableManager(blank=True, help_text='Show only the blog articles tagged with chosen tags.', related_name='myblog_latest_post', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='filter by tag')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GenericBlogPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='myblog_genericblogplugin', serialize=False, to='cms.cmsplugin')),
                ('current_site', models.BooleanField(default=True, help_text='Select items from the current site only', verbose_name='current site')),
                ('template_folder', models.CharField(choices=[('plugins', 'Default template')], default='plugins', help_text='Select plugin template to load for this instance', max_length=200, verbose_name='Plugin template')),
                ('app_config', aldryn_apphooks_config.fields.AppHookConfigField(blank=True, help_text='When selecting a value, the form is reloaded to get the updated default', null=True, on_delete=django.db.models.deletion.CASCADE, to='cms_myblog.blogconfig', verbose_name='app. config')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AuthorEntriesPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='myblog_authorentriesplugin', serialize=False, to='cms.cmsplugin')),
                ('current_site', models.BooleanField(default=True, help_text='Select items from the current site only', verbose_name='current site')),
                ('template_folder', models.CharField(choices=[('plugins', 'Default template')], default='plugins', help_text='Select plugin template to load for this instance', max_length=200, verbose_name='Plugin template')),
                ('latest_posts', models.IntegerField(default=5, help_text='The number of author articles to be displayed.', verbose_name='articles')),
                ('app_config', aldryn_apphooks_config.fields.AppHookConfigField(blank=True, help_text='When selecting a value, the form is reloaded to get the updated default', null=True, on_delete=django.db.models.deletion.CASCADE, to='cms_myblog.blogconfig', verbose_name='app. config')),
                ('authors', models.ManyToManyField(limit_choices_to={'myblog_post_author__publish': True}, to=settings.AUTH_USER_MODEL, verbose_name='authors')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PostTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=752, verbose_name='title')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=752, verbose_name='slug')),
                ('subtitle', models.CharField(blank=True, default='', max_length=767, verbose_name='subtitle')),
                ('abstract', djangocms_text_ckeditor.fields.HTMLField(blank=True, default='', verbose_name='abstract')),
                ('meta_description', models.TextField(blank=True, default='', verbose_name='post meta description')),
                ('meta_keywords', models.TextField(blank=True, default='', verbose_name='post meta keywords')),
                ('meta_title', models.CharField(blank=True, default='', help_text='used in title tag and social sharing', max_length=2000, verbose_name='post meta title')),
                ('post_text', djangocms_text_ckeditor.fields.HTMLField(blank=True, default='', verbose_name='text')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='myblog.post')),
            ],
            options={
                'verbose_name': 'blog article Translation',
                'db_table': 'myblog_post_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'slug'), ('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='BlogCategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=752, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=752, verbose_name='slug')),
                ('meta_description', models.TextField(blank=True, default='', verbose_name='category meta description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='myblog.blogcategory')),
            ],
            options={
                'verbose_name': 'blog category Translation',
                'db_table': 'myblog_blogcategory_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'slug'), ('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
