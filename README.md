# azure-ai-infra-bot
AI-powered infrastructure automation tool that uses Azure OpenAI to generate and deploy Terraform configurations to Azure through a CI/CD pipeline. Built with Python, Terraform, and Azure DevOps.

## overview 
This project bridges the gap between natural language and cloud infrastructure you describe the infrastructure you want and the bot generates valid terraform HCL and saves it. Then deploys it to azure automatically through a Azure devops pipeline.

## Architecture

user prompt --> azure openAI GPT-4o-mini --> Terraform HCL --> Azure DevOps piepline --> Azure Infrastructure

## Tech Stack

-**Cloud:** Microsoft Azure
-**AI** Azure OpenAI GPT-4
-**Infrastructure as code** Terraform (Remote state via Azure Blob Storage)
-**CI/CD** Azure DevOps Pipelines (Yaml)
-**Scripting** python
-**Version control:** Git / GitHUb

Example prompt:
Create a storage account named teststore in East US in a resource group called test-rg
Generated output:
hclresource "azurerm_resource_group" "example" {
  name     = "test-rg"
  location = "East US"
}

resource "azurerm_storage_account" "example" {
  name                     = "teststore"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

## Project Structure
...

azure-ai-infra-bot/
├── terraform/
│   ├── main.tf              # Core Azure infrastructure
│   └── .terraform.lock.hcl  # Provider version lock
├── scripts/
│   └── generate_infra.py    # Azure OpenAI integration script
├── pipeline/
│   └── azure-pipeline.yml   # Azure DevOps CI/CD pipeline
└── README.md

## How it works 

1.User provides a natural language prompt describing desired azure infrastructure.
2.Python script sends the prompt to azure openAi with a system message enforcing valid HCL output
3.Generated terraform config is saved to the terraform directory
4.Azure Devops pipeline triggers automatically on push to main
5.Pipeline runs terraform init, plan and apply to deploy the infrastructure

## Infrastructure Deployed 

- Resource Group   (azure-ai-infra-bot-rg)
- storage Account (aiinfrabotstore)
- Virtual Network (ai-infra-vnet)
- subnet (ai-infra-subnet)
- Remote state managed via Azure blob storage (tfstatematthew)

## Prerequisites 

-Azure subscription
-Azure Openai resource with GPT-4o-mini deployment
-Terraform >= 1.0
-python >= 3.x
-Azure CLI
-AZure Devops organization

## Environment Variables

The following environment variables are requires:

| Variable | Description |
|----------|-------------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI service endpoint |
| `AZURE_OPENAI_KEY` | Azure OpenAI API key |
| `ARM_CLIENT_ID` | Service principal app ID |
| `ARM_CLIENT_SECRET` | Service principal password |
| `ARM_SUBSCRIPTION_ID` | Azure subscription ID |
| `ARM_TENANT_ID` | Azure tenant ID |

## Setup

1. Clone the repository
bash
git clone https://github.com/Matthew2906/azure-ai-infra-bot.git
cd azure-ai-infra-bot

2. Set environment variables
bash
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_KEY="your-key"
$env:ARM_CLIENT_ID="your-client-id"
$env:ARM_CLIENT_SECRET="your-secret"
$env:ARM_SUBSCRIPTION_ID="your-subscription-id"
$env:ARM_TENANT_ID="your-tenant-id"

3. Initialize Terraform
bash
cd terraform
terraform init

4. Run the AI generation script 
'''bash 
cd scripts 
python generate_infra.py

## Author 
Matthew Raphael — [GitHub](https://github.com/Matthew2906) | [LinkedIn](https://linkedin.com/in/matthew-raphael-81a163202)
