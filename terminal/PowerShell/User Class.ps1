enum Perms {
    NONE
    LIMIT
    ALL
}
class Role {

    [Perms]$Permission

    Role([Perms]$perm) {

        $this.Permission = $perm
    }

    [bool]CanCreateFolder() {

        return $this.Permission -eq [Perms]::ALL
    }

    [string]Describe() {

        return "Permission level: $($this.Permission)"
    }
}

class Admin : Role {

    Admin() : base([Perms]::ALL) {}

}

class Employee : Role {

    Employee() : base([Perms]::LIMIT) {}

}

class User {

    hidden [int]$Id
    hidden [Role]$Role

    [string]$Name

    User([string]$name) {

        $this.Name = $name
    }


    [Role]GetRole() {

        return $this.Role
    }

    [string]Describe() {

        return "$($this.Name) : $($this.Role.Describe())"
    }
}

function Show-User {

    param(
        [Parameter(
            ValueFromPipeline=$true,
            ValueFromPipelineByPropertyName=$true
        )]
        [string]$Name
    )

    process {
        Write-Host "Hello  $Name , It is a pleasure to meet ya :)" -ForegroundColor DarkCyan
    }
}

[User]$user=[User]::new("Craice Miller")

get-member -InputObject $user -Force -MemberType Property

#write-output "These are enums values..." -NoEnumerate
#[System.Management.Automation.PSMemberTypes].getEnumValues()

$user.Name | Show-User