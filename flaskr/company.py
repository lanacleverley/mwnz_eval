from flask import Blueprint, make_response
import json
import requests
import xml.etree.ElementTree as ET

company = Blueprint("company", __name__)

api_url = "https://raw.githubusercontent.com/MiddlewareNewZealand/evaluation-instructions/main/xml-api/"

@company.route('/')
def hello():
    return 'Hello, World!'

@company.route('/<id>')
def get_company(id):
    if(valid_company_id(id)):
        company_info_xml = get_company_info(id).text
        if(valid_xml(company_info_xml)):
            company_info = convert_company_xml_to_json(company_info_xml)
            if(company_info == invalid_company):
                return make_response(company_info, 404)
            else:
                return make_response(company_info, 200)
    
    return make_response(companyNotFound, 404)



def convert_company_xml_to_json(xml):
    try:
        root = ET.fromstring(xml)

        data = {}
        for el in root:
                data.update({el.tag: el.text})
        
        #TODO: Company Schema check
        if("id" in data.keys()):
            company_json = json.dumps(data)
            return company_json
        
        return invalid_company
    
    except:
        return invalid_company

def get_company_info(id):
    company_url = api_url + id + ".xml"
    company_xml = requests.get(company_url)
    return company_xml

def valid_company_id(id):
    return id.isdigit()

def valid_xml(xml):
    #TODO: Implement XML Schema Check
    return xml.startswith("<?xml version=")

class error:
    def __init__(self, error, error_description):
        self.error = error
        self.error_description = error_description

    def toJson(self):
        return json.dumps({self.error: self.error_description})
    
companyNotFound = error("CompanyNotFound", "Company was not found").toJson()
invalid_company = error("Invalid Company", "Company data does not meet company schema")