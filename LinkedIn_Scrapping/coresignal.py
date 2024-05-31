import requests
import json

url = "https://api.coresignal.com/cdapi/v1/linkedin/job/search/filter"

payload = json.dumps(
    {"title": "(Associate Sales Manager) OR (Branch Sales Manager) OR (Business Developer)",
     "country": "(United States)", "industry": "(Information Technology & Services)"}
)
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJFZERTQSIsImtpZCI6ImJiNjM0MGYzLWE3MTAtODE5NC02YzUxLTBkY2NiNjU3MWNkZCJ9'
                     '.eyJhdWQiOiJlc3Nway5jb20iLCJleHAiOjE3NDUzMzM3MjcsImlhdCI6MTcxMzc3Njc3NSwiaXNzIjoiaHR0cHM6Ly9vcHMuY29yZXNpZ25hbC5jb206ODMwMC92MS9pZGVudGl0eS9vaWRjIiwibmFtZXNwYWNlIjoicm9vdCIsInByZWZlcnJlZF91c2VybmFtZSI6ImVzc3BrLmNvbSIsInN1YiI6ImZhMGM0YzljLWMyMWMtZmZkZi1jMGI5LTQ4YWVkNWFmOWMxNiIsInVzZXJpbmZvIjp7InNjb3BlcyI6ImNkYXBpIn19.3H8ZLu70I4RaDyZsV4kDSNsgIT1teMDoquAzpTUfFO46hMp6ZtOm42Y5RiP4ve_4KBcDCIWYBOyQD8EsWVf9Cw'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


