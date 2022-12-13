from modules.db.mongo.models.driver import Driver


class DriverRepository:
    @staticmethod
    def create(payload):
        driver = Driver(**payload)
        return driver.save(payload) 