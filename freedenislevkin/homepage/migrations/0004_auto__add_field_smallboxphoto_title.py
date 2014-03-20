# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SmallBoxPhoto.title'
        db.add_column(u'homepage_smallboxphoto', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SmallBoxPhoto.title'
        db.delete_column(u'homepage_smallboxphoto', 'title')


    models = {
        u'homepage.homepage': {
            'Meta': {'object_name': 'Homepage'},
            'big_texbox_title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'big_textbox': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo1'", 'null': 'True', 'to': u"orm['homepage.SmallBoxPhoto']"}),
            'photo2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo2'", 'null': 'True', 'to': u"orm['homepage.SmallBoxPhoto']"}),
            'photo3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo3'", 'null': 'True', 'to': u"orm['homepage.SmallBoxPhoto']"}),
            'show_big_textbox': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_news': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slider': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['homepage.Slider']", 'null': 'True', 'symmetrical': 'False'}),
            'textbox1': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'}),
            'textbox2': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'}),
            'textbox3': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'})
        },
        u'homepage.slider': {
            'Meta': {'object_name': 'Slider'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'homepage.smallboxphoto': {
            'Meta': {'object_name': 'SmallBoxPhoto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        }
    }

    complete_apps = ['homepage']