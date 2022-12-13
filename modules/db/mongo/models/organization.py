from ..connector import db
from .base import BaseModel
from datetime import datetime

class Organization(BaseModel):
    user_name = db.StringField(unique=True)
    organisation_name = db.StringField()
    display_name = db.StringField()
    mobile = db.StringField()
    profile_image = db.StringField()
    qr_code_image = db.StringField()
    type = db.StringField(default='OWNER')

    association_name = db.StringField()
    onboarded_association = db.StringField()
    created_by = db.StringField()

    aadhar_number = db.StringField()
    pan_number = db.StringField()
    gst_number = db.StringField()
    country = db.StringField()
    state = db.StringField()
    pin = db.StringField()
    upi = db.StringField()
    cancelled_cheque = db.StringField(default='')

    verify_update_date = db.DateTimeField(default=datetime.now())
    verify_update_by = db.StringField(default='')

    is_verified = db.BooleanField(default=False)
    is_blocked = db.BooleanField(default=False)
    pioneer_badge = db.BooleanField(default=False)
    terms_and_condition = db.BooleanField(default=False)
