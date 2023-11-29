from application import db
from application.project.models import BaseModel

class CertificateType(db.Model, BaseModel):

    __tablename__ = "certificate_types"
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(32), nullable = False)
    online        = db.Column(db.Bool, default = False)
    level         = db.Column(db.String(32), nullable = False)
    status        = db.Column(db.bool, nullable = False)
    created_date  = db.Column(db.DateTime, nullable = False)

    certi_type    = db.relationship("Certificate", foreign_keys="Certificate.certi_type_id", backref="type", lazy=True)

class Certificate(db.Model, BaseModel):

    __tablename__ = 'certificates'
    id            = db.Column(db.Integer, primary_key=True)
    awardee_id    = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    certi_type_id = db.Column(db.Integer, db.ForeignKey("certificate_types.id"), nullable = False)
    score         = db.Column(db.Integer, nullable = False)
    input_by      = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    description   = db.Column(db.String(256), nullable = False)
    started_date  = db.Column(db.DateTime, nullable = False)
    expired_date  = db.Column(db.DateTime, nullable = False)

    def __repr__(self):
        return f'{self.id} - {self.awardee} - {self.type} - {self.score}'