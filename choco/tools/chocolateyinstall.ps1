$ErrorActionPreference = 'Stop';
$toolsDir   = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"
$url        = 'https://images.habbo.com/habbo-native-clients/launcher/HabboLauncher-Setup-1.0.31.exe'

$packageArgs = @{
  packageName   = $env:ChocolateyPackageName
  unzipLocation = $toolsDir
  fileType      = 'exe'
  url           = $url

  softwareName  = 'habbo*'

  silentArgs    = "--skip-to-install"
  validExitCodes= @(0, 3010, 1641)
}

Install-ChocolateyPackage @packageArgs
