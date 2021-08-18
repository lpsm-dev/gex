## Development

1. Make changes to the code.

1. Build nupkg:
   ```
   choco pack
   ```

1. Then try install:
   ```
   choco install habbo -dv -s .
   ```

1. Then try uninstall:
   ```
   choco uninstall habbo -dv -s .
   ```

1. Then try push:
   ```
   choco apikey -k [API_KEY_HERE] -source https://push.chocolatey.org/
   choco push .\habbo.1.0.31.nupkg -s https://push.chocolatey.org/
   ```

Then submit a PR!

## Links

- https://docs.chocolatey.org/en-us/create/create-packages-quick-start
