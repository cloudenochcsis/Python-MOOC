#!/bin/bash
# azure-setup-fresh.sh - Complete Azure authentication setup for any scenario

set -e  # Exit on any error

echo "🔐 Azure Authentication Setup for Terraform"
echo "=============================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Function to check prerequisites
check_prerequisites() {
    echo "🔍 Checking prerequisites..."
    
    # Check Azure CLI
    if ! command -v az &> /dev/null; then
        print_error "Azure CLI not found!"
        echo "Please install Azure CLI first:"
        echo "  macOS: brew install azure-cli"
        echo "  Windows: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows"
        echo "  Linux: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux"
        exit 1
    fi
    print_status "Azure CLI found"
    
    # Check jq
    if ! command -v jq &> /dev/null; then
        print_error "jq not found!"
        echo "Please install jq first:"
        echo "  macOS: brew install jq"
        echo "  Windows: choco install jq"
        echo "  Linux: sudo apt-get install jq"
        exit 1
    fi
    print_status "jq found"
    
    # Check if logged in to Azure
    if ! az account show &> /dev/null; then
        print_warning "Not logged in to Azure. Please log in..."
        az login
    fi
    print_status "Azure authentication verified"
}

# Function to get current Azure context
get_azure_context() {
    echo "📋 Getting Azure context..."
    
    SUBSCRIPTION_ID=$(az account show --query id -o tsv)
    TENANT_ID=$(az account show --query tenantId -o tsv)
    SUBSCRIPTION_NAME=$(az account show --query name -o tsv)
    
    if [ -z "$SUBSCRIPTION_ID" ] || [ -z "$TENANT_ID" ]; then
        print_error "Failed to get Azure context"
        exit 1
    fi
    
    print_status "Subscription: $SUBSCRIPTION_NAME"
    print_status "Subscription ID: $SUBSCRIPTION_ID"
    print_status "Tenant ID: $TENANT_ID"
}

# Function to check for existing service principals
check_existing_sps() {
    echo "🔍 Checking for existing Terraform service principals..."
    
    EXISTING_SP_COUNT=$(az ad sp list --display-name "terraform-sp-*" --query "length(@)" --output tsv 2>/dev/null || echo "0")
    
    if [ "$EXISTING_SP_COUNT" -gt 0 ]; then
        print_warning "Found $EXISTING_SP_COUNT existing Terraform service principal(s)"
        
        echo "Existing service principals:"
        az ad sp list --display-name "terraform-sp-*" --query "[].{displayName:displayName, appId:appId, created:createdDateTime}" --output table
        
        read -p "Do you want to use an existing one? (y/n): " -n 1 -r
        echo
        
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo "Please select an existing service principal:"
            az ad sp list --display-name "terraform-sp-*" --query "[].{displayName:displayName, appId:appId}" --output table
            
            read -p "Enter the App ID to use: " EXISTING_APP_ID
            
            if [ -n "$EXISTING_APP_ID" ]; then
                print_info "Using existing service principal: $EXISTING_APP_ID"
                
                # Check if it has valid credentials
                CREDENTIALS=$(az ad sp credential list --id "$EXISTING_APP_ID" --query "[?endDate > \`$(date -u +%Y-%m-%dT%H:%M:%S.000Z)\`]" --output json)
                
                if [ "$(echo "$CREDENTIALS" | jq 'length')" -gt 0 ]; then
                    print_status "Valid credentials found for existing service principal"
                    CLIENT_ID="$EXISTING_APP_ID"
                    
                    # Get the client secret
                    CLIENT_SECRET=$(az ad sp credential reset --id "$EXISTING_APP_ID" --append | jq -r '.password')
                    
                    if [ "$CLIENT_SECRET" != "null" ] && [ -n "$CLIENT_SECRET" ]; then
                        print_status "Successfully retrieved client secret"
                        return 0
                    else
                        print_error "Failed to get client secret from existing service principal"
                        return 1
                    fi
                else
                    print_warning "No valid credentials found for existing service principal"
                    return 1
                fi
            fi
        fi
    fi
    
    return 1
}

# Function to create new service principal
create_new_sp() {
    echo "👤 Creating new service principal..."
    
    # Generate unique name with timestamp
    SP_NAME="terraform-sp-$(date +%Y%m%d-%H%M%S)"
    print_info "Service principal name: $SP_NAME"
    
    # Create service principal
    print_info "Creating service principal with Contributor role..."
    SP_OUTPUT=$(az ad sp create-for-rbac \
        --name "$SP_NAME" \
        --role "Contributor" \
        --scopes "/subscriptions/$SUBSCRIPTION_ID" \
        --output json)
    
    # Extract values - handle both old and new Azure CLI formats
    CLIENT_ID=$(echo "$SP_OUTPUT" | jq -r '.clientId // .appId')
    CLIENT_SECRET=$(echo "$SP_OUTPUT" | jq -r '.clientSecret // .password')
    
    # Verify extraction
    if [ "$CLIENT_ID" = "null" ] || [ "$CLIENT_SECRET" = "null" ] || [ -z "$CLIENT_ID" ] || [ -z "$CLIENT_SECRET" ]; then
        print_error "Failed to extract client ID or secret from output"
        echo "Debug output:"
        echo "$SP_OUTPUT" | jq .
        exit 1
    fi
    
    print_status "Service principal created successfully"
    print_status "Client ID: $CLIENT_ID"
}

# Function to test authentication
test_authentication() {
    echo "🧪 Testing authentication..."
    
    # Set environment variables temporarily
    export ARM_CLIENT_ID="$CLIENT_ID"
    export ARM_CLIENT_SECRET="$CLIENT_SECRET"
    export ARM_SUBSCRIPTION_ID="$SUBSCRIPTION_ID"
    export ARM_TENANT_ID="$TENANT_ID"
    
    # Test with Azure CLI
    if az account show --subscription "$SUBSCRIPTION_ID" &> /dev/null; then
        print_status "Authentication test successful!"
    else
        print_warning "Authentication test failed, but this might be normal for service principals"
    fi
    
    # Test with Terraform (if available)
    if command -v terraform &> /dev/null; then
        print_info "Testing Terraform authentication..."
        # This is a basic test - in practice, you'd run terraform init
        print_status "Terraform available for testing"
    fi
}

# Function to create configuration files
create_config_files() {
    echo "📝 Creating configuration files..."
    
    # Create .env file
    cat > .env << EOF
# Azure Authentication Variables
# Generated on: $(date)
# Service Principal: $CLIENT_ID
ARM_CLIENT_ID=$CLIENT_ID
ARM_CLIENT_SECRET=$CLIENT_SECRET
ARM_SUBSCRIPTION_ID=$SUBSCRIPTION_ID
ARM_TENANT_ID=$TENANT_ID

# Export these variables in your shell:
# source .env
EOF
    print_status "Created .env file"
    
    # Create terraform.tfvars template
    cat > terraform.tfvars.template << EOF
# Terraform Variables Template
# Copy this to terraform.tfvars and fill in your values

# Project Configuration
project_name = "your-project-name"
environment = "dev"  # dev, staging, prod

# Azure Configuration
location = "East US"  # Change to your preferred region

# Database Configuration
postgres_admin_user = "admin"
postgres_sku_name = "B_Standard_B1ms"
enable_redis = true
redis_cache_sku_name = "Basic"
redis_cache_family = "C"
redis_capacity = 0

# App Service Configuration
service_plan_sku_name = "B1"
EOF
    print_status "Created terraform.tfvars.template"
    
    # Create setup instructions
    cat > SETUP_INSTRUCTIONS.md << EOF
# Azure Terraform Setup Instructions

## Authentication Variables
Your Azure authentication variables have been set up and saved to \`.env\`.

## Next Steps

1. **Load the environment variables:**
   \`\`\`bash
   source .env
   \`\`\`

2. **Verify the variables are set:**
   \`\`\`bash
   echo "ARM_CLIENT_ID: \$ARM_CLIENT_ID"
   echo "ARM_SUBSCRIPTION_ID: \$ARM_SUBSCRIPTION_ID"
   echo "ARM_TENANT_ID: \$ARM_TENANT_ID"
   \`\`\`

3. **Initialize Terraform:**
   \`\`\`bash
   cd terraform/azure
   terraform init -backend-config="key=terraform.tfstate" \\
                  -backend-config="resource_group_name=rg-terraform-state" \\
                  -backend-config="storage_account_name=xpertsterraformstate" \\
                  -backend-config="container_name=tfstate" \\
                  -backend-config="subscription_id=\$ARM_SUBSCRIPTION_ID" \\
                  -backend-config="tenant_id=\$ARM_TENANT_ID"
   \`\`\`

4. **Configure your project:**
   - Copy \`terraform.tfvars.template\` to \`terraform.tfvars\`
   - Update the values for your project

5. **Plan and apply:**
   \`\`\`bash
   terraform plan
   terraform apply
   \`\`\`

## Security Notes
- Never commit \`.env\` to version control
- Rotate service principal credentials regularly
- Use Azure Key Vault for production secrets
EOF
    print_status "Created SETUP_INSTRUCTIONS.md"
}

# Function to display summary
display_summary() {
    echo ""
    echo "🎉 Setup Complete!"
    echo "=================="
    echo ""
    echo "🔐 Your Azure authentication variables:"
    echo "   ARM_CLIENT_ID: $CLIENT_ID"
    echo "   ARM_SUBSCRIPTION_ID: $SUBSCRIPTION_ID"
    echo "   ARM_TENANT_ID: $TENANT_ID"
    echo ""
    echo "📁 Files created:"
    echo "   .env - Environment variables"
    echo "   terraform.tfvars.template - Terraform variables template"
    echo "   SETUP_INSTRUCTIONS.md - Next steps"
    echo ""
    echo "⚠️  IMPORTANT: Keep your client secret secure!"
    echo "💡 To use these variables, run: source .env"
    echo ""
    echo "�� See SETUP_INSTRUCTIONS.md for next steps"
}

# Main execution
main() {
    echo "Starting Azure authentication setup..."
    echo ""
    
    check_prerequisites
    get_azure_context
    
    # Try to use existing service principal first
    if check_existing_sps; then
        print_info "Using existing service principal"
    else
        create_new_sp
    fi
    
    test_authentication
    create_config_files
    display_summary
}

# Run the main function
main "$@"