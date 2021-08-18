$ErrorActionPreference = "Stop";

if (!$PSScriptRoot) {
  $PSScriptRoot = Split-Path $MyInvocation.MyCommand.Path -Parent
}
. "$PSScriptRoot\helper.ps1"

$version      = "1.0.31"

if (!(IsVersionAlreadyInstalled $version)) {
  $stop_habbbo = if (Get-Process -Name Habbo -ErrorAction SilentlyContinue) { $false } else { $true }

  $packageArgs  = @{
    packageName     = $env:ChocolateyPackageName
    softwareName    = "habbo"
    url             = "https://images.habbo.com/habbo-native-clients/launcher/HabboLauncher-Setup-$version.exe"
    fileType        = "exe"
    silentArgs      = "/s"
    validExitCodes  = @(0, 1641, 3010)
  }

  Install-ChocolateyPackage @packageArgs

  if ($stop_habbbo -and (Get-Process -Name Habbo -ErrorAction SilentlyContinue)) {
    Stop-Process -processname Habbo
  }
} else {
  Write-Host "Habbo $version is already installed."
}
