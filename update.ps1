param(
    [Parameter(Mandatory=$true)]
    [string]$m
)

git add .
git commit -m $m
git push 

if ($LASTEXITCODE -eq 0) {
    Write-Host "Changes successfully pushed to GitHub! :)" -ForegroundColor Green
} else {
    Write-Host "Push failed! Did you forget to do something first?" -ForegroundColor Red
}

# ---------------------------------

Start-Sleep -Seconds 5
Clear-Host

function Close-CommonApps {

    Stop-Process -Name chrome -Force -ErrorAction SilentlyContinue
    Stop-Process -Name code -Force -ErrorAction SilentlyContinue

}

$answer = Read-Host -Prompt "Wanna continue"

if ($answer -match "^no") {

    Close-CommonApps

    Write-Host "Have a nice day :)"

    Start-Sleep -Seconds 2

    exit
}

Write-Host "Good. What else do you want to do today?"
