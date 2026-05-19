import requests
from ai_analyzer import analyze_logs

JENKINS_URL = "http://52.91.159.237:8080"
JOB_NAME = "ai-devops-pipeline-v2"

USERNAME = "admin"
API_TOKEN = "1169ad2f515dbb3c28d784a2f14eb254fd"

url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/consoleText"

response = requests.get(
    url,
    auth=(USERNAME, API_TOKEN)
)

logs = response.text[-4000:]

# Extract only relevant error lines
error_lines = []

for line in logs.splitlines():
    if (
        "ERROR" in line
        or "Exception" in line
        or "Traceback" in line
        or "ModuleNotFoundError" in line
        or "NoCredentialsError" in line
    ):
        error_lines.append(line)

filtered_logs = "\n".join(error_lines)

result = analyze_logs(filtered_logs)

print("\n===== AI ANALYSIS =====\n")
print(result)