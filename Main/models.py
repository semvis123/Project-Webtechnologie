from Main import db

class Docent(db.Model):

    __tablename__ = 'docenten'
    id = db.Column(db.Integer,primary_key = True)
    naam = db.Column(db.Text)
    student = db.relationship('Student',backref='docent',uselist=False)

    def __init__(self,naam):
        self.naam = naam

    def __repr__(self):
        if self.student:
            return f"Docent {self.naam} is mentor van {self.student.naam}"
        else:
            return f"Docent {self.naam} heeft geen studenten als mentor te begeleiden."

class Student(db.Model):

    __tablename__ = 'studenten'

    id = db.Column(db.Integer,primary_key= True)
    naam = db.Column(db.Text)
    docent_id = db.Column(db.Integer,db.ForeignKey('docenten.id'))

    def __init__(self,naam,docent_id):
        self.naam = naam
        self.docent_id = docent_id

    def __repr__(self):
        return f"Deze student heet {self.name}"