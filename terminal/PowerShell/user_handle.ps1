enum Perms {
    NONE
    LIMIT
    ALL
}



class Logger {

    static [string]$LogFile = ".\activity.log"

    static [void] Write([string]$message) {

        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss" 

        "$timestamp - $message" | Out-File `
            -Append `
            -FilePath ([Logger]::LogFile)
    }
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

    [void]SetRole([Role]$role) {

        $this.Role = $role

        [Logger]::Write("Role assigned to $($this.Name)")
    }

    [Role]GetRole() {

        return $this.Role
    }

    [string]Describe() {

        return "$($this.Name) : $($this.Role.Describe())"
    }
}

class AccessController {

    hidden [string[]]$AdminList

    AccessController() {

        $this.AdminList = @(
            "Craice Miller",
            "Ana Lopez"
        )
    }

    [bool]Verify([User]$user) {

        return $user.Name -in $this.AdminList
    }
}

class FolderManager {

    static [void]CreateFolder(
        [User]$user,
        [string]$path,
        [string]$name
    ) {

        if ($user.GetRole().CanCreateFolder()) {

            try {

                $fullPath = Join-Path $path $name

                New-Item `
                    -Path $fullPath `
                    -ItemType Directory `
                    -ErrorAction Stop

                [Logger]::Write(
                    "Folder created by $($user.Name)"
                )

            }
            catch {

                [Logger]::Write(
                    "Error creating folder: $_"
                )
            }
        }
        else {

            [Logger]::Write(
                "Permission denied for $($user.Name)"
            )
        }
    }
}

function Export-UserReport {

    param(
        [User[]]$Users
    )

    $Users |
    Select-Object Name |
    Export-Csv `
        -Path ".\users.csv" `
        -NoTypeInformation

    [Logger]::Write("User report exported")
}

function Load-Config {

    param(
        [string]$Path
    )

    if (Test-Path $Path) {

        return Get-Content $Path |
        ConvertFrom-Json
    }

    return $null
}

function Save-Config {

    param(
        $Object,
        [string]$Path
    )

    $Object |
    ConvertTo-Json |
    Out-File $Path
}

$config = Load-Config ".\config.json"

if (-not $config) {

    $config = @{
        DefaultPath = ".\Workspace"
    }

    Save-Config $config ".\config.json"
}

$controller = [AccessController]::new()

$user = [User]::new("Craice Miller")

if ($controller.Verify($user)) {

    $user.SetRole([Admin]::new())

}
else {

    $user.SetRole([Employee]::new())

}

Write-Host $user.Describe()

[FolderManager]::CreateFolder(
    $user,
    $config.DefaultPath,
    "Reports"
)

Export-UserReport @($user)