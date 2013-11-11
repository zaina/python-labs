 #!/usr/local/bin/python

"""
LAB02 Learning Objective: Learn to navigate a JSON file and convert to a 
      python object.

::

 a. Based on a sample Openstack authentication response file, what python 
   syntax would you use to access items in the serviceCatalog? 

   What path would access the publicURL for the DFW CloudServersOpenStack endpoint?

 b. Provide a new dict called compute_api_info and add keys auth_response,
   image_ID, and flavor_ID. Use None for values. Dump compute_api_info 
   to a file in JSON format

 c. Based on analysis of the sample authentication response file, provide 
   the following functions in a new module named compute_api_json.py:
     i. get_token_id() 
     ii. get_tenant_id()
     iii. get_compute_public_URL(region) # solve this programmatically 
                                         # i.e. don't hard code

 d. Also provide these functions using the information given in class:
     i. get_image_ID()  # use an ID of your choosing
     ii. get_flavor_ID()  # return 2
     iv. update_cached_auth_response(auth_object)
"""

from pprint import pprint 
import pickle
import json    

compute_api_info = {"auth_response" : None, "image_ID":None, "flavor_ID.":None}
print compute_api_info

#pickle.dump( compute_api_info, open( "compute_api_info.json", "wb" ) )
json_string = json.dumps(compute_api_info, indent=4)
print json_string


json_data = open('auth_sample').read()
data = json.load(open('auth_sample'))

#print data["access"]["token"]["id"]
#print json_data
#pprint(json_data)
#pprint(url)

def get_token_id():
    token_id = data["access"]["token"]["id"]
    return token_id

def get_tenant_id():
    tenant_id = data["access"]["token"]["tenant"]["id"]
    return tenant_id

def get_compute_public_URL(region):

    services = data["access"]["serviceCatalog"]
    for service in services:
        if service["name"] == "cloudServersOpenStack":
            compute_endpoints = service["endpoints"]
            for endpoint in compute_endpoints:
                if endpoint["region"] == region:
                    compute_public_URL = endpoint["publicURL"]
                    break
    return compute_public_URL

print get_token_id()
print get_tenant_id()
print get_compute_public_URL("DFW")

