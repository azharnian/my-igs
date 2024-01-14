from application import db
from application.project.models import BaseModel
from datetime import datetime

class CertificateType(db.Model, BaseModel):

    __tablename__ = "certificate_types"
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(32), nullable = False)
    is_online     = db.Column(db.Boolean, default = False)
    level         = db.Column(db.String(32), nullable = False)
    status        = db.Column(db.Boolean, default = True)
    created_date  = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    
    certi_type    = db.relationship("Certificate", backref="type", lazy=True)

class Certificate(db.Model, BaseModel):

    __tablename__ = 'certificates'
    id             = db.Column(db.Integer, primary_key=True)
    awardee_id     = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    certi_type_id  = db.Column(db.Integer, db.ForeignKey("certificate_types.id"), nullable = False)
    score          = db.Column(db.Integer, nullable = False)
    description    = db.Column(db.String(256), nullable = False)
    start_date     = db.Column(db.DateTime, nullable = False)
    expired_date   = db.Column(db.DateTime, nullable = False)

    certi         = db.relationship("CertificateRevision", backref="revision", lazy=True)


    def __repr__(self):
        return f'{self.id} - {self.awardee} - {self.type} - {self.score}'
    
class CertificateRevision(db.Model, BaseModel):
    __tablename__ = 'certificate_revisions'
    id             = db.Column(db.Integer, primary_key=True)
    certif_id      = db.Column(db.Integer, db.ForeignKey("certificates.id"), nullable = False)
    created_by     = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    created_date   = db.Column(db.DateTime, nullable = False)
    comment        = db.Column(db.String(256), nullable = False)