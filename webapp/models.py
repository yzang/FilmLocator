from __future__ import unicode_literals
from elasticsearch_dsl.connections import connections
from django.db import models

# Create your models here.
connections.create_connection(hosts=['localhost'], timeout=30)