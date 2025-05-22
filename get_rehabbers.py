import requests
import json

url = "https://appfactory.dec.ny.gov/SpecialLicensesSearchSystem/screenservices/SpecialLicensesSearchSystem/MainFlow/Rehab/DataActionGetRehabResults"

headers = {
    "Host": "appfactory.dec.ny.gov",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:138.0) Gecko/20100101 Firefox/138.0",
    "Accept": "application/json",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "OutSystems-locale": "en-US",
    "X-CSRFToken": "T6C+9iB49TLra4jEsMeSckDMNhQ=",
    "Content-Type": "application/json; charset=UTF-8",
    "Origin": "https://appfactory.dec.ny.gov",
    "Connection": "keep-alive",
    "Referer": "https://appfactory.dec.ny.gov/SpecialLicensesSearchSystem/rehab",
    "Cookie": (
        "osVisitor=db8f20ae-8ea7-44af-9caa-fdb3f1f56b4f; "
        "nr1Users=lid%3dAnonymous%3btuu%3d0%3bexp%3d0%3brhs%3dXBC1ss1nOgYW1SmqUjSxLucVOAg%3d%3bhmc%3dkyc02mUbzZOsps8Egah8HwLb0iI%3d; "
        "nr2Users=crf%3dT6C%2b9iB49TLra4jEsMeSckDMNhQ%3d%3buid%3d0%3bunm%3d; "
        "osVisit=e7e28c9e-4ebc-4e6f-bf3c-8710e069e9ef"
    ),
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}

payload = {
    "versionInfo": {
        "moduleVersion": "v0eK_+Y3F4Uy08pmXG3B5A",
        "apiVersion": "4vWEY7gF4613XWtzwX1ong"
    },
    "viewName": "MainFlow.Rehab",
    "screenData": {
        "variables": {
            "SelectedRadioButtonId": "6",
            "ShowIndexPage": False,
            "StartIndex": 0,
            "MaxRecords": 20,
            "TotalCount": 0,
            "RoleID": "131",
            "County_ID": "0",
            "RehabResultList": {
                "List": [],
                "EmptyListItem": {
                    "DISPLAY_NAME": "",
                    "PUBLIC_NAME": "",
                    "CITY": "",
                    "STATE": "",
                    "HOME_PHONE_NUMBER": "",
                    "BUSINESS_PHONE_NUMBER": "",
                    "BUSINESS_PHONE_EXT": "",
                    "EMAIL_ADDRESS": "",
                    "DISTRICT_NAME": "",
                    "COUNTY_OF_RESIDENCE": "0",
                    "rabies_vector": "",
                    "FEDERAL_LICENSE_NUMBER": "",
                    "FEDERAL_LICENSE_EXP_DATE": "1900-01-01T00:00:00",
                    "Phone_Number": ""
                }
            },
            "SpeciesName": "Small Mammals",
            "SpeciesExpertiseCode": "SM",
            "County_Name": "All Counties",
            "TableSort": "DISTRICT_NAME",
            "TableSortColumns": {
                "List": [
                    {"TableColumnSortIndex": 0, "AttributeName": "DISTRICT_NAME", "AttributeDisplayName": "County", "TableSortAttributeTypeId": 2},
                    {"TableColumnSortIndex": 1, "AttributeName": "CITY", "AttributeDisplayName": "City", "TableSortAttributeTypeId": 2},
                    {"TableColumnSortIndex": 2, "AttributeName": "DISPLAY_NAME", "AttributeDisplayName": "Name of Wildlife Rehabilitator", "TableSortAttributeTypeId": 2},
                    {"TableColumnSortIndex": 3, "AttributeName": "PHONE_NUMBER", "AttributeDisplayName": "Business Phone", "TableSortAttributeTypeId": 2},
                    {"TableColumnSortIndex": 4, "AttributeName": "EMAIL_ADDRESS", "AttributeDisplayName": "Email", "TableSortAttributeTypeId": 2}
                ]
            }
        }
    }
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
