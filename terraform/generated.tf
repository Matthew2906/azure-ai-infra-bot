resource "azurerm_resource_group" "test_rg" {
  name     = "test-rg"
  location = "East US"
}

resource "azurerm_storage_account" "teststore" {
  name                     = "teststore"
  resource_group_name      = azurerm_resource_group.test_rg.name
  location                 = azurerm_resource_group.test_rg.location
  account_tier            = "Standard"
  account_replication_type = "LRS"
}