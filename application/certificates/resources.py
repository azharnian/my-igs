import logging

from application import db
from application.project.utils import log_activity
from application.certificates.models import *

@log_activity
def create_certificate(certificate_data):
    try:
        certificate = Certificate(
            created_by = certificate_data['score'],
            desc = certificate_data['description'],
            start = certificate_data['started_date'],
            expired = certificate_data['expired_date']
        )
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    certificate.save()
    return {'success' : True}

@log_activity
def get_all_certificates():
    try:
        ress = Certificate.query.all()
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    
    return ress

@log_activity
def get_certificate_by_id(certificate_id):
    try:
        res = Certificate.query.get(int(certificate_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e

    return res

@log_activity
def update_certificate(certificate_id, new_certificate_data):
    try:
        certificate = Certificate.query.get(int(certificate_id))
        certificate['created_by'] = new_certificate_data['created_by'],
        certificate['description'] = new_certificate_data['description'],
        certificate['started_date'] = new_certificate_data['started_date'],
        certificate['expired_date'] = new_certificate_data['expired_date']
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    certificate.update()
    return {'success' : True}

@log_activity
def remove_certificate(certificate_id):
    try:
        certificate = Certificate.query.get(int(certificate_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    certificate.remove()
    return {'success' : True}

@log_activity
def disable_certificate(certificate_id):
    try:
        certificate = Certificate.query.get(int(certificate_id))
    except Exception as e:
        logging.error(f"{str(e)}")
        raise e
    certificate.is_active = False
    certificate.update()
    return {'success' : True}