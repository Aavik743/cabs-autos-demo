# import decimal

# import json

# import os

# from datetime import datetime

# from os import path



# from bson import ObjectId




# def dir_exists(dir_name):

#     if not path.exists(dir_name):

#         os.mkdir(dir_name)




# class JSONEncoder(json.JSONEncoder):

#     def default(self, o):

#         if isinstance(o, ObjectId):

#             return str(o)

#         if isinstance(o, datetime):

#             return o.strftime("%Y-%m-%d %H:%M:%S")

#         if isinstance(o, decimal.Decimal):

#             return float(o)

#         return json.JSONEncoder.default(self, o)