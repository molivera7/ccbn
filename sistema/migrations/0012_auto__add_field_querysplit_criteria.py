# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'QuerySplit.criteria'
        db.add_column('sistema_querysplit', 'criteria',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'QuerySplit.criteria'
        db.delete_column('sistema_querysplit', 'criteria')

    models = {
        'sistema.estrategia': {
            'Meta': {'object_name': 'Estrategia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.TextField', [], {}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'programa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Modulo']"})
        },
        'sistema.filter': {
            'Meta': {'object_name': 'Filter'},
            'criteria': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'field': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'salida': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Salida']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sistema.modulo': {
            'Meta': {'object_name': 'Modulo'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sistema.querysplit': {
            'Meta': {'object_name': 'QuerySplit'},
            'criteria': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'field': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'meta': ('django.db.models.fields.IntegerField', [], {}),
            'salida': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Salida']"}),
            'tipo_meta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sistema.salida': {
            'Meta': {'object_name': 'Salida'},
            'estrategia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Estrategia']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'tipo_meta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'sistema.submodulo': {
            'Meta': {'object_name': 'SubModulo'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_module': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Modulo']"})
        }
    }

    complete_apps = ['sistema']