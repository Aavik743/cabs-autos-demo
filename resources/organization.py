from flask_restful import Resource
from flask import request
import json
# from utils import JSONEncoder
from bson import ObjectId
from repositories.organization import OrganizationRepository
from repositories.vehicle import VehicleRepository
from repositories.driver import DriverRepository
from schema.organization import OrganizationInputSchema, organization_output_schema
from utils.response import success_response, failure_response





class OrganizationResource(Resource):

    @staticmethod
    def post():
        try:
            payload = request.get_json()
            schema = OrganizationInputSchema()
            schema.load(payload["organization"])
            if payload["organization"]:
                organization = OrganizationRepository.create(payload["organization"])
            if payload["vehicle"]: 
                payload["vehicle"]["organization_id"] = organization["id"]      
                VehicleRepository.create(payload["vehicle"])
            if payload["driver"]: 
                payload["driver"]["organization_id"] = organization["id"]      
                DriverRepository.create(payload["driver"])
            return success_response(message="Successfully created", status_code=201)
        except Exception as err:
            return failure_response(str(err))

    # @staticmethod
    # def get():
    #     try:
    #         organization_list = OrganizationRepository.get_all_organizations({"is_deleted": False})
    #         org_list = []
    #         for item in organization_list:
    #             #org_dict = {"id": item.id, "user_name": item.user_name, "type":item.type}
    #             breakpoint()
    #             org_list.append(item)   
    #         return success_response(message="Successfully fetched", content=json.loads(json.dumps(org_list, cls=JSONEncoder)))
    #     except Exception as err:
    #         return failure_response(str(err))

    @staticmethod
    def get():
        try:
            organization_list = OrganizationRepository.get_all_org()
            org_data = organization_output_schema.dump(organization_list)            
            return success_response(message="Successfully fetched", content=org_data)
        except Exception as err:
            return str(err)

            
class OrganizationResourceById(Resource):

    @staticmethod
    def put(id):
        try:
            payload = request.get_json()
            schema = OrganizationInputSchema()
            payload=schema.load(payload, partial=True)
            org =OrganizationRepository.get_org_by_id(id)
            OrganizationRepository.update(org, payload)
            return success_response(message="Updated successfully")
        except Exception as err:
            return str(err)