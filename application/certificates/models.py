from application import db
from application.project.models import BaseModel

class CertificateType(db.Model, BaseModel):

    __tablename__ = "certificate_types"
    id = db.Column(db.Integer, primary_key=True)


class Cretificate(db.Model, BaseModel):

    __tablename__ = 'certificates'
    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        return f''
    