from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Role(db.Model):
    __tablename__ = 'role'

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(150), unique=True, nullable=False)

    persons = db.relationship('Person', backref='role')
    
    def __repr__(self):
        return self.role_name


class Mobile(db.Model):
    __tablename__ = 'mobile'

    mobile_number = db.Column(db.Integer, primary_key=True)
    mobile_carrier_id = db.Column(
        db.Integer,
        db.ForeignKey('mobile_carrier.mobile_carrier_id'),
        nullable=False,
        )
    
    persons = db.relationship('Person', backref='mobile', uselist=False)


class MobileCarrier(db.Model):
    __tablename__ = 'mobile_carrier'

    mobile_carrier_id = db.Column(db.Integer, primary_key=True)
    mobile_carrier_name = db.Column(db.String(150), nullable=False)

    mobile = db.relationship('Mobile', backref='mobile_carrier')
    
    def __repr__(self):
        return self.mobile_carrier_name


class RoleRelationBeneficiary(db.Model):
    __tablename__ = 'role_relation_beneficiary'

    role_relation_benef_id = db.Column(db.Integer, primary_key=True)
    role_relation_benef_name = db.Column(db.String(150), nullable=False)

    persons = db.relationship('Person', backref='role_relation_beneficiary')


class StatusApplication(db.Model):
    __tablename__ = 'status_application'

    status_id = db.Column(db.Integer, primary_key=True)
    status_name = db.Column(db.String(150), unique=True, nullable=False)

    applications = db.relationship('Application', backref='status_application')
    
    def __repr__(self):
        return self.status_name


application_person = db.Table('application_person',
    db.Column(
        'application_id',
        db.Integer,
        db.ForeignKey('application.application_id')
    ),
    db.Column(
        'person_document_number',
        db.Integer,
        db.ForeignKey('person.document_number')
    )
)

class Person(db.Model):
    __tablename__ = 'person'

    document_number = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(
        db.Integer,
        db.ForeignKey('role.role_id'),
        nullable=False
    )
    role_relation_benef_id = db.Column(
        db.Integer,
        db.ForeignKey('role_relation_beneficiary.role_relation_benef_id'),
        nullable=True
    )
    mobile_number = db.Column(
        db.Integer,
        db.ForeignKey('mobile.mobile_number'),
        nullable=True
    )
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)

    applications = db.relationship(
        'Application',
        secondary=application_person,
        back_populates='persons'
    )


class Application(db.Model):
    __tablename__ = 'application'

    application_id = db.Column(db.UUID(as_uuid=True), primary_key=True)
    mobile_number = db.Column(
        db.BigInteger,
        db.ForeignKey('mobile.mobile_number'),
        nullable=False,
        unique=True
    )
    role_mandatory_parent_or_guardian = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )
    beneficiary_id = db.Column(
        db.Integer,
        db.ForeignKey('person.document_number'),
        nullable=True
    )
    parent_or_guardian_id = db.Column(
        db.Integer,
        db.ForeignKey('person.document_number'),
        nullable=True
    )
    status_id = db.Column(
        db.Integer, 
        db.ForeignKey('status_application.status_id'),
        nullable=False
    )
    creation_date = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    last_top_up = db.Column(db.Date, nullable=True)

    persons = db.relationship(
        'Person',
        secondary=application_person,
        back_populates='applications'
    )