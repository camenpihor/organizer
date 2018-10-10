import os

import boto3
import psycopg2

PG_URL = os.environ['PG_URL']
BUCKET = 'organizer-app'


def export_postgres_table(table_name):
    return


def build_postgres_table(table_name):
    s3 = boto3.resource('s3')
    
    return