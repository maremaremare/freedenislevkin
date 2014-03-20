# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Homepage.photo1'
        db.alter_column(u'homepage_homepage', 'photo1_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['homepage.SmallBoxPhoto']))

        # Changing field 'Homepage.photo2'
        db.alter_column(u'homepage_homepage', 'photo2_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['homepage.SmallBoxPhoto']))

        # Changing field 'Homepage.photo3'
        db.alter_column(u'homepage_homepage', 'photo3_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['homepage.SmallBoxPhoto']))

    def backwards(self, orm):

        # Changing field 'Homepage.photo1'
        db.alter_column(u'homepage_homepage', 'photo1_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['homepage.SmallBoxPhoto']))

        # Changing field 'Homepage.photo2'
        db.alter_column(u'homepage_homepage', 'photo2_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['homepage.SmallBoxPhoto']))

        # Changing field 'Homepage.photo3'
        db.alter_column(u'homepage_homepage', 'photo3_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['homepage.SmallBoxPhoto']))

    models = {
        u'homepage.homepage': {
            'Meta': {'object_name': 'Homepage'},
            'big_texbox_title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'big_textbox': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo1'", 'null': 'True', 'to': u"orm['homepage.SmallBoxPhoto']"}),
            'photo2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo2'", 'null': 'True', 'to': u"orm['homepage.SmallBoxPhoto']"}),
            'photo3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo3'", 'null': 'True', 'to': u"orm['homepage.SmallBoxPhoto']"}),
            'show_big_textbox': ('django.db.models.fields.BooleanField', [], {}),
            'show_news': ('django.db.models.fields.BooleanField', [], {}),
            'slider': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['homepage.Slider']", 'symmetrical': 'False'}),
            'textbox1': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'textbox2': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'textbox3': ('django.db.models.fields.CharField', [], {'max_length': '300'})
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
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['homepage']