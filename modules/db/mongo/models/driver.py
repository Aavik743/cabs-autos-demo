from ..connector import db
from .base import BaseModel
from .organization import Organization
    
class Driver(BaseModel):
    organization_id = db.ReferenceField(Organization, required=True)
    driver_username = db.StringField(unique=True)
    first_name = db.StringField(default='')
    last_name = db.StringField(default='')
    profile_image = db.StringField(default='')
    contact_number = db.StringField(default='')
    state = db.StringField(default='')
    city = db.StringField(default='')
    country = db.StringField(default='')
    aadhar_number = db.StringField(default='')
    pan_number = db.StringField(default='')
    driving_licence_number = db.StringField(default='')