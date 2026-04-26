class Assistant {

    [string]$Name
    [string]$AssistantName = "ORION"
    hidden [string[]]$Greetings = @(
        "Systems online.",
        "Ready when you are.",
        "Awaiting instructions.",
        "Navigation console active.",
        "Environment stable."
    )

    Assistant([string]$userName) {
        $this.Name = $userName
    }

    [void] Greet() {

        $hour = (Get-Date).Hour

        if ($hour -lt 12) { $period = "morning" }
        elseif ($hour -lt 18) { $period = "afternoon" }
        else { $period = "evening" }

        $randomGreeting = $this.Greetings | Get-Random

        Write-Host ""
        Write-Host "Assistant: $($this.AssistantName)"
        Write-Host "Operator: $($this.Name)"
        Write-Host "Time: $(Get-Date)"
        Write-Host ""
        Write-Host "Good $period, $($this.Name)."
        Write-Host $randomGreeting
    }

    [void] InvalidOption() {

        Write-Host "$($this.AssistantName): That option is unavailable."
    }

    [void] ShutdownMessage() {

        Write-Host "$($this.AssistantName): Session closed. Have a productive day, $($this.Name)."
    }
}



class SessionManager {

    hidden [string[]]$ActiveProfiles = @()

    [void] RegisterProfile([string]$profileName) {

        if (-not ($this.ActiveProfiles -contains $profileName)) {

            $this.ActiveProfiles += $profileName
        }
    }

    [void] ShowStatus() {

        if ($this.ActiveProfiles.Count -eq 0) {

            Write-Host "No active profiles."
            return
        }

        Write-Host "Active session profiles:"

        foreach ($profile in $this.ActiveProfiles) {

            Write-Host "• $profile"
        }
    }
}



class ProfileManager {

    hidden [hashtable]$Profiles

    ProfileManager() {

        $this.Profiles = @{

            Learning = @("chrome","code")

            Work = @("outlook","excel")

            Maintenance = @("cleanmgr")
        }
    }

    [void] StartProfile([string]$profileName) {

        if (-not $this.Profiles.ContainsKey($profileName)) {

            Write-Host "Profile not found."
            return
        }

        foreach ($app in $this.Profiles[$profileName]) {

            Write-Host "Launching $app ..."
            Start-Process $app
        }

        Write-Host "$profileName profile ready."
    }


    [void] CloseProfile([string]$profileName) {

        if (-not $this.Profiles.ContainsKey($profileName)) {

            return
        }

        foreach ($app in $this.Profiles[$profileName]) {

            Stop-Process -Name $app -Force -ErrorAction SilentlyContinue
        }
    }


    [void] CloseAllProfiles() {

        foreach ($profile in $this.Profiles.Keys) {

            $this.CloseProfile($profile)
        }
    }


    [void] ShowProfiles() {

        Write-Host ""
        Write-Host "Available profiles:"

        foreach ($profile in $this.Profiles.Keys) {

            Write-Host "- $profile"
        }
    }
}



class Runner {

    hidden [string]$Version = "1.0.0"

    [Assistant]$Assistant
    [ProfileManager]$ProfileManager
    [SessionManager]$SessionManager

    Runner([string]$userName) {

        $this.Assistant = [Assistant]::new($userName)
        $this.ProfileManager = [ProfileManager]::new()
        $this.SessionManager = [SessionManager]::new()
    }


    [void] UpdateScript() {

        $path = ".\update.ps1"

        Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -File $path"
    }

    [void] ShutdownSystem() {

        $confirm = Read-Host "Confirm shutdown? (y/n)"
    
        if ($confirm -match "^yes") {
            $this.ProfileManager.CloseAllProfiles()
    
            Write-Host "Have a lovely rest my dear $($this.name), I am looking foward to be here for you agian :)" -ForegroundColor Cyan
            start-sleep -seconds 10
            Stop-Computer -Force
        }
    }


    [void] Run() {

        $choice = $null

        do {

            Clear-Host

            Write-Host "SYSTEM PERSONAL INTERFACE v$($this.Version)"
            Write-Host ""

            $this.Assistant.Greet()

            Write-Host ""
            Write-Host "1. Learning Mode"
            Write-Host "2. Work Mode"
            Write-Host "3. Show Profiles"
            Write-Host "4. Update Git"
            Write-Host "5. Session Status"
            Write-Host "6. Exit"
            Write-Host "7. Shutdown The computer"
            Write-Host ""

            $choice = Read-Host "Select option: "

            switch ($choice) {

                "1" {

                    $this.ProfileManager.StartProfile("Learning")
                    $this.SessionManager.RegisterProfile("Learning")
                }

                "2" {

                    $this.ProfileManager.StartProfile("Work")
                    $this.SessionManager.RegisterProfile("Work")
                }

                "3" {

                    $this.ProfileManager.ShowProfiles()
                }

                "4" {

                    $this.UpdateScript()
                }

                "5" {

                    $this.SessionManager.ShowStatus()
                }

                "6" {

                    $this.ProfileManager.CloseAllProfiles()
                    $this.Assistant.ShutdownMessage()
                }
                "7"{
                    $this.ShutdownSystem()
                }

                default {

                    $this.Assistant.InvalidOption()
                }
            }

            Pause

        }

        until ($choice -eq "6")
    }
}



$runner = [Runner]::new("Craice Miller")
$runner.Run()