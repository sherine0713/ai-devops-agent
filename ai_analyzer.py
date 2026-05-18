from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage

llm = ChatBedrock(
    model_id="amazon.nova-lite-v1:0",
    region_name="us-east-1"
)

def analyze_logs(log_text):

    prompt = f"""
    You are an expert DevOps engineer.

    Analyze the Jenkins failure logs below.

    Provide:
    1. Root cause
    2. Failure summary
    3. Suggested fix

    Logs:
    {log_text}
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    return response.content