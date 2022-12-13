from modules.db.mongo.models.organization import Organization
from bson import ObjectId
# from modules.db.mongo.models.base import BaseModel
# from modules.db.mongo.models import base



class OrganizationRepository:
    @staticmethod
    def create(payload):
        organizations = Organization(**payload)
        return organizations.save(payload)       

    @staticmethod
    def get_org_by_id(id):
        try:
            return Organization.objects.get(id=ObjectId(id), is_deleted=False)
        except Exception as err:
            return str(err)

    @staticmethod
    def get_all_org():
        try:
            query = Organization.objects.aggregate([
                {
                    "$match": {
                        "is_deleted": False
                    }
                },
                {
                    "$project": {
                        "_id": 1,
                        "user_name": 1,
                        "type": 1,
                        "is_deleted": 1,
                        "created_on": 1,
                        "updated_on": 1,
                        "cancelled_cheque": 1,
                        "verify_update_date": 1,
                        "verify_update_by": 1,
                        "is_verified": 1,
                        "is_blocked": 1,
                        "pioneer_badge": 1,
                        "terms_and_condition": 1,

                    }
                }
            ])
            return list(query)
        except:
            return []

    
    # @staticmethod
    # def get_org_by_id(id):
    #     try:
    #         query = Organization.objects.aggregate([
    #             {
    #                 "$match": {
    #                     "is_deleted": False,
    #                     "_id": ObjectId(id)
    #                 }
    #             },
    #             {
    #                 "$project": {
    #                     "_id": 1,
    #                     "user_name": 1,
    #                     "type": 1,
    #                     "is_deleted": 1,
    #                     "created_on": 1,
    #                     "updated_on": 1,
    #                     "cancelled_cheque": 1,
    #                     "verify_update_date": 1,
    #                     "verify_update_by": 1,
    #                     "is_verified": 1,
    #                     "is_blocked": 1,
    #                     "pioneer_badge": 1,
    #                     "terms_and_condition": 1,

    #                 }
    #             }
    #         ])
    #         return query
    #     except:
    #         return []


    @staticmethod
    def update(org, payload):
        try:
            if 'type' in payload:
                org['type'] = payload['type']
            return org.update_temp()
            # update_obj={}
            # if 'type' in payload:
            #     update_obj['type'] = payload['type']
            # if 'cancelled_cheque' in payload:
            #     update_obj['cancelled_cheque'] = payload['cancelled_cheque']
            # return org.update(**update_obj)    
        except Exception as err:
            return str(err)

    @staticmethod
    def update_by_id(id, payload):
        try:
           org = OrganizationRepository.get_org_by_id(id)
           return OrganizationRepository.update(org, payload)
             
        except Exception as err:
            return str(err)