from bson import ObjectId
from marshmallow import Schema, fields, validate

from modules.schema.connector import ma
Schema.TYPE_MAPPING[ObjectId] = fields.String


class OrganizationInputSchema(Schema):
    user_name = fields.String()
    type = fields.String()
    

class OrganizationOutputSchema(ma.Schema):

    class Meta:
        fields = ('_id', 'id', 'created_on', 'updated_on', 'is_deleted', 'user_name', 'type', 'cancelled_cheque','verify_update_date', 'verify_update_by', 'is_verified', 'is_blocked', 'pioneer_badge', 'terms_and_condition')


organization_output_schema= OrganizationOutputSchema(many=True)