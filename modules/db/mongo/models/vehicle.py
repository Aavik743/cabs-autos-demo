from ..connector import db
from .base import BaseModel
from .organization import Organization
    
class Vehicle(BaseModel):
    organization_id = db.ReferenceField(Organization, required=True)
    vehicle_id = db.StringField(unique=True, required=True)
    license_number = db.StringField()
    category = db.StringField(choices=db.ListField(db.StringField(),
                                           choices=['CAB', 'AUTO']))
    profile_image = db.StringField(default='')
    model = db.StringField(default='')  
    make =  db.StringField(default='')
    colour = db.StringField(default='') 
                                       
