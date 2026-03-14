import os
import subprocess
from openai import AzureOpenAI

# Azure OpenAI configuration
client = AzureOpenAI(
    azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
    api_key=os.environ.get("AZURE_OPENAI_KEY"),
    api_version="2024-02-01"
)

def generate_terraform(prompt):
    """Send a prompt to Azure OpenAI and get Terraform config back"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": """You are an Azure infrastructure expert. 
                When given a description of infrastructure, respond ONLY with 
                valid Terraform HCL code. No explanations, no markdown, just 
                the raw Terraform code."""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

def save_terraform(tf_code, filename="generated.tf"):
    """Save generated Terraform code to the terraform folder"""
    output_path = os.path.join("..", "terraform", filename)
    with open(output_path, "w") as f:
        f.write(tf_code)
    print(f"Terraform config saved to {output_path}")

def run_terraform_plan():
    """Run terraform plan on the generated config"""
    terraform_dir = os.path.join("..", "terraform")
    result = subprocess.run(
        ["terraform", "plan"],
        cwd=terraform_dir,
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        print("Terraform plan failed:")
        print(result.stderr)
    return result.returncode

if __name__ == "__main__":
    prompt = input("Describe the Azure infrastructure you want to create: ")
    print("\nGenerating Terraform configuration...\n")
    tf_code = generate_terraform(prompt)
    print("Generated Terraform:\n")
    print(tf_code)
    save_terraform(tf_code)
    print("\nRunning terraform plan...\n")
    run_terraform_plan()