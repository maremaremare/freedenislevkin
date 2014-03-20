# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News_link'
        db.create_table(u'content_news_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'content', ['News_link'])

        # Adding model 'Photo'
        db.create_table(u'content_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'content', ['Photo'])

        # Adding model 'Video'
        db.create_table(u'content_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video', self.gf('embed_video.fields.EmbedVideoField')(max_length=200)),
        ))
        db.send_create_signal(u'content', ['Video'])

        # Adding model 'News_category'
        db.create_table(u'content_news_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'content', ['News_category'])

        # Adding model 'News_post'
        db.create_table(u'content_news_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.News_category'])),
        ))
        db.send_create_signal(u'content', ['News_post'])

        # Adding M2M table for field photos on 'News_post'
        m2m_table_name = db.shorten_name(u'content_news_post_photos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('news_post', models.ForeignKey(orm[u'content.news_post'], null=False)),
            ('photo', models.ForeignKey(orm[u'content.photo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['news_post_id', 'photo_id'])


    def backwards(self, orm):
        # Deleting model 'News_link'
        db.delete_table(u'content_news_link')

        # Deleting model 'Photo'
        db.delete_table(u'content_photo')

        # Deleting model 'Video'
        db.delete_table(u'content_video')

        # Deleting model 'News_category'
        db.delete_table(u'content_news_category')

        # Deleting model 'News_post'
        db.delete_table(u'content_news_post')

        # Removing M2M table for field photos on 'News_post'
        db.delete_table(db.shorten_name(u'content_news_post_photos'))


    models = {
        u'content.news_category': {
            'Meta': {'object_name': 'News_category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'content.news_link': {
            'Meta': {'object_name': 'News_link'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'content.news_post': {
            'Meta': {'object_name': 'News_post'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.News_category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['content.Photo']", 'symmetrical': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'content.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'content.video': {
            'Meta': {'object_name': 'Video'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['content']