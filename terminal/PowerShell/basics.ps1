using module ".\tools.psm1"

# We don't define 'class User' here anymore. 
# We just use the one provided by the module.

$craice = [User]::new("Craice Miller", 19, [Role]::admin)
$app = "notepad"

Write-Host "Never give in!" -ForegroundColor Cyan

if (Test-Admin $craice) {
    Start-Process $app
}
#start-process $app
#Get-ChildItem
#Get-verb 

