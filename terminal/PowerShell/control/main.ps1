
class Runner {

    hidden [string]$VERSION="0.0.1"
    [string[]]$startApps = @()
    [string]$name = ""

    

    $greetings = @(
        "Hello there! Ready to get to work?",
        "Greetings, Earthling. How can I assist today?",
        "System online. Welcome back, Admin.",
        "Hey! Hope your coffee is strong and your bugs are few.",
        "Salutations! Let's automate something awesome.",
        "Hi! Processing your request with 99.9% enthusiasm.",
        "Ahoy! Navigation systems are ready for input.",
        "Top of the morning to you!"
    )



    hidden [hashtable]$profiles

    Runner() {

        $this.profiles = @{

            Learning = @(
                "chrome",
                "code"
            )

            Work = @(
                "outlook",
                "excel"
            )

            Maintenance = @(
                "cleanmgr"
            )
        }
    }

    [void] StartProfile([string]$profileName) {

        if (-not $this.profiles.ContainsKey($profileName)) {

            Write-Host "Profile not found"
            return
        }

        foreach ($app in $this.profiles[$profileName]) {

            Start-Process $app
        }

        Write-Host "$profileName profile ready $($this.name)"
    }


    [void] CloseProfile([string]$profileName) {

        if (-not $this.profiles.ContainsKey($profileName)) {
            write-host "That Profile does not exist, sorry my dear $($this.name)"
            return
        }

        foreach ($app in $this.profiles[$profileName]) {
            Write-Host "Closing << $($app) >>"

            Stop-Process -Name $app -Force -ErrorAction SilentlyContinue
        }
    }

    [void] ShowProfiles() {

        Write-Host ""
        Write-Host "Available profiles:"

        foreach ($profile in $this.profiles.Keys) {

            Write-Host "- $profile"
        }
    }





    [void] greet(){
        $pick = $this.greetings | Get-Random
        Write-Host "[$((Get-Date).ToShortTimeString())] $pick" 
    }


    [void] InvalidOption() {
        Write-Host "My dear $($this.name) you have picked an option I cannot do... please pador me" -ForegroundColor Cyan
    }


    [void] Update() {
        $path = Join-Path $PSScriptRoot "update.ps1"
    
        Start-Process powershell `
            -ArgumentList "-ExecutionPolicy Bypass -File `"$path`""
    }

    [void] EndProgram() {


        $keys = $this.profiles.Keys
        foreach ($k in $keys) {
            $this.CloseProfile($k)
            
        }

        Write-Host "Have a nice day :) $($this.name)"
        Start-Sleep -Seconds 5
    }

    [void] Run() {
        $choice = $null

        do {
            Clear-Host
            Write-Host "--- SYSTEM PERSONAL INTERFACE  V.$($this.VERSION) ---" -ForegroundColor Yellow
            Write-Host "What are you planning to do, $($this.name)?"
            write-host ""
            
            Write-Host "1. Learning Mode"
            Write-Host "2. Work Mode"
            Write-Host "3. Show Profiles"
            Write-Host "4. Update Git"
            Write-Host "5. End section for today"
        
            write-host ""
            $choice = Read-Host "Select option"
        
            switch ($choice) {

                "1" { $this.StartProfile("Learning")}
                "2" { $this.StartProfile("Work")}
                "3" { $this.ShowProfiles()}
                "4" { $this.Update() }
                "5" { $this.EndProgram()}

                default { $this.InvalidOption() }
            }

            Start-Sleep -seconds 5

            Pause

        } until ($choice -eq "5")
    }
}


$r = [Runner]::new()
$r.name = "Craice Miller"

$r.greet()
Start-Sleep -seconds 5
$r.Run()
