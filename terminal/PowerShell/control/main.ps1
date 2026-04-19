
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




    Runner([string[]]$apps){
        $this.startApps = $apps
    }

    [void] greet(){
        $pick = $this.greetings | Get-Random
        Write-Host "[$((Get-Date).ToShortTimeString())] $pick" 
    }

    [void] CloseCommonApps() {
        foreach ($item in $this.startApps) {
            Stop-Process -Name $item -Force -ErrorAction SilentlyContinue
        }
    }

    [void] InvalidOption() {
        Write-Host "Invalid option"
    }

    [void] StartLearning() {
        foreach ($item in $this.startApps) {
            Start-Process $item
        }

        Write-Host "Everything is ready $($this.name)"
    }

    [void] Update() {
        $path = Join-Path $PSScriptRoot "update.ps1"
    
        Start-Process powershell `
            -ArgumentList "-ExecutionPolicy Bypass -File `"$path`""
    }

    [void] EndProgram() {

        $this.CloseCommonApps()

        Write-Host "Have a nice day :) $($this.name)"
        
    
        Start-Sleep -Seconds 5
    }

    [void] Run() {
        $choice = $null

        do {
            Clear-Host
            Write-Host "--- SYSTEM MESSAGE $($this.VERSION) ---" -ForegroundColor Yellow
            Write-Host "What are you planning to do, $($this.name)?"
        
            Write-Host "=== Daily Control Panel ==="
            Write-Host "1. Start Learning"
            Write-Host "2. Update Git"
            Write-Host "4. Exit"
        
            $choice = Read-Host "Select option"
        
            switch ($choice) {

                "1" { $this.StartLearning() }

                "2" { $this.Update() }

                "4" { $this.EndProgram() }

                default { $this.InvalidOption() }
            }

            Start-Sleep -seconds 5

            Pause

        } until ($choice -eq "4")
    }
}

$apps = @("chrome", "code")
$r = [Runner]::new($apps)
$r.name = "Craice Miller"

$r.greet()
Start-Sleep -seconds 5
$r.Run()
