from flask import Blueprint
from flask_restful import Api
from resources.organization import OrganizationResource, OrganizationResourceById

ORGANIZATION_BLUEPRINT = Blueprint('Organization', __name__)
Api(ORGANIZATION_BLUEPRINT).add_resource(OrganizationResource, '/onboarding_organization')

ORGANIZATIONS_BLUEPRINT = Blueprint('Organizations', __name__)
Api(ORGANIZATIONS_BLUEPRINT).add_resource(OrganizationResourceById, '/org/<string:id>')