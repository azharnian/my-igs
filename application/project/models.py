from application import db

class BaseModel:

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.remove(self)
        db.session.commit()

    def update(self):
        db.session.commit()