$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "Running Black..."
python -m black .

Write-Host ""
Write-Host "Running Ruff..."
python -m ruff check . --fix

Write-Host ""
Write-Host "Running Pytest..."
python -m pytest

Write-Host ""
Write-Host "Done!"