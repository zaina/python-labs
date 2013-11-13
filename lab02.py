 #!/usr/local/bin/python

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

