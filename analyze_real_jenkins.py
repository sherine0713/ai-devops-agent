import requests
from ai_analyzer import analyze_logs

JENKINS_URL = "http://52.91.159.237:8080"
JOB_NAME = "ai-devops-pipeline"

USERNAME = "admin"
API_TOKEN = "1169ad2f515dbb3c28d784a2f14eb254fd"

url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/consoleText"

response = requests.get(
    url,
    auth=(USERNAME, API_TOKEN)
)

logs = response.text[-4000:]

result = analyze_logs(logs)

print("\n===== AI ANALYSIS =====\n")
print(result)