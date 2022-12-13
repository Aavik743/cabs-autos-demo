from modules.db.mongo.models.vehicle import Vehicle


class VehicleRepository:
    @staticmethod
    def create(payload):
        vehicle = Vehicle(**payload)
        return vehicle.save(payload) 