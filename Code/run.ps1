Get-ChildItem -Filter *.py | Foreach-Object {
    $_.Name
    python $_.FullName
    '---------------'
}