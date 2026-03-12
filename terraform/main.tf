terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }

  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "tfstatematthew"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
  subscription_id = "5c82edde-3f1c-4268-87c4-6cc3d0968c94"
}

resource "azurerm_resource_group" "main" {
  name     = "azure-ai-infra-bot-rg"
  location = "East US"
}