from langchain_aws import ChatBedrockConverse

print("Starting Bedrock test...")

llm = ChatBedrockConverse(
    model="amazon.nova-lite-v1:0",
    region_name="us-east-1"
)

print("Sending request...")

response = llm.invoke("Say hello in one short sentence.")

print("Response received:")
print(response.content)