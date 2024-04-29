import requests
import json
url = "https://eastus2.azure.data.mongodb-api.com/app/data-nzixvpy/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "theaters",
    "database": "sample_mflix",
    "dataSource": "Cluster0",
    "projection": {
        "_id": 1
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': '27g7HFGlKLXxGpfhyf6c4lL6Znsiqrs78nj7Wotqnu8yxbXMTIWi3nAhzo5a2uIh',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
