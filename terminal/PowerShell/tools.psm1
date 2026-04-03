enum Role {
    admin
    employee
    tester
}

class User {
    [string]$Name
    [int]$Age
    [Role]$role

    User([string]$name, [int]$age, [Role]$role) {
        $this.Name = $name
        $this.Age = $age
        $this.role = $role
    }
}

function Test-Admin {
    [OutputType([bool])]
    param([User]$user) # It will now use the Class defined above

    if ($user.role -ne [Role]::admin) {
        Write-Host "You are not allowed to do this..." -ForegroundColor Red
        return $false
    }
    Write-Host "Perm granted" -ForegroundColor Green
    return $true
}

Export-ModuleMember -Function Test-Admin