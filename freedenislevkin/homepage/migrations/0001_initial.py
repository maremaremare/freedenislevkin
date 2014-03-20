# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slider'
        db.create_table(u'homepage_slider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'homepage', ['Slider'])

        # Adding model 'SmallBoxPhoto'
        db.create_table(u'homepage_smallboxphoto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'homepage', ['SmallBoxPhoto'])

        # Adding model 'Homepage'
        db.create_table(u'homepage_homepage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('textbox1', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('textbox2', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('textbox3', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('photo1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photo1', to=orm['homepage.SmallBoxPhoto'])),
            ('photo2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photo2', to=orm['homepage.SmallBoxPhoto'])),
            ('photo3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photo3', to=orm['homepage.SmallBoxPhoto'])),
            ('show_big_textbox', self.gf('django.db.models.fields.BooleanField')()),
            ('big_texbox_title', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('big_textbox', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('show_news', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'homepage', ['Homepage'])

        # Adding M2M table for field slider on 'Homepage'
        m2m_table_name = db.shorten_name(u'homepage_homepage_slider')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('homepage', models.ForeignKey(orm[u'homepage.homepage'], null=False)),
            ('slider', models.ForeignKey(orm[u'homepage.slider'], null=False))
        ))
        db.create_unique(m2m_table_name, ['homepage_id', 'slider_id'])


    def backwards(self, orm):
        # Deleting model 'Slider'
        db.delete_table(u'homepage_slider')

        # Deleting model 'SmallBoxPhoto'
        db.delete_table(u'homepage_smallboxphoto')

        # Deleting model 'Homepage'
        db.delete_table(u'homepage_homepage')

        # Removing M2M table for field slider on 'Homepage'
        db.delete_table(db.shorten_name(u'homepage_homepage_slider'))


    models = {
        u'homepage.homepage': {
            'Meta': {'object_name': 'Homepage'},
            'big_texbox_title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'big_textbox': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo1'", 'to': u"orm['homepage.SmallBoxPhoto']"}),
            'photo2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo2'", 'to': u"orm['homepage.SmallBoxPhoto']"}),
            'photo3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo3'", 'to': u"orm['homepage.SmallBoxPhoto']"}),
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