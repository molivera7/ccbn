# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EventoColectivo'
        db.create_table('promocion_eventocolectivo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('actividad', self.gf('django.db.models.fields.IntegerField')()),
            ('participantes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ninos', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ninas', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('jovenes_hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('jovenes_mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('adultos_hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('adultos_mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sensibilizacion', self.gf('django.db.models.fields.IntegerField')()),
            ('apropiacion', self.gf('django.db.models.fields.IntegerField')()),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('comentarios', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('acuerdos', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('promocion', ['EventoColectivo'])

    def backwards(self, orm):
        # Deleting model 'EventoColectivo'
        db.delete_table('promocion_eventocolectivo')

    models = {
        'promocion.coro': {
            'Meta': {'object_name': 'Coro'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'promocion.danza': {
            'Meta': {'object_name': 'Danza'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'promocion.eventocolectivo': {
            'Meta': {'object_name': 'EventoColectivo'},
            'actividad': ('django.db.models.fields.IntegerField', [], {}),
            'acuerdos': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'adultos_hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'adultos_mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'apropiacion': ('django.db.models.fields.IntegerField', [], {}),
            'comentarios': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes_hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'jovenes_mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ninas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ninos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'participantes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sensibilizacion': ('django.db.models.fields.IntegerField', [], {})
        },
        'promocion.musica': {
            'Meta': {'object_name': 'Musica'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'promocion.pintura': {
            'Meta': {'object_name': 'Pintura'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'promocion.teatro': {
            'Meta': {'object_name': 'Teatro'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['promocion']