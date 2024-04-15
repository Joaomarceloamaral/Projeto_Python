$exclude = @("venv", "bot_python.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_python.zip" -Force