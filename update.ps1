param(
    [Parameter(Mandatory=$true)]
    [string]$m
)

git add .
git commit -m $m
git push 

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Changes successfully pushed to GitHub!" -ForegroundColor Green
} else {
    Write-Host "❌ Push failed! Did you forget to do something first?" -ForegroundColor Red
}
