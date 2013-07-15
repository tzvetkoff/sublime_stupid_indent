
# Stupid Indent for Sublime Text

A Sublime Text plugin to determine indentation settings based on filename rather than current indentation.
Supports both Sublime Text 2 and 3.

## Installation
If you're using the [Sublime Package Control](http://wbond.net/sublime_packages/package_control) plugin, you can install the plugin just like any other - `⌘⇧P`, `Install Package`, `Stupid Indent`.

The other way around is to manually clone the repository:

``` bash
# WARNING: This instructions apply only to Mac OS X
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages
# or ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
git clone https://github.com/tzvetkoff/sublime_stupid_indent sublime_stupid_indent
```

## Configuration
Stupid Indent adds settings to the Package Settings menu: `Preferences -> Package Settings -> Stupid Indent`.
To customize them, just copy `Settings -> Default` to `Settings -> User`, or use mines below:
``` json
{
    "configuration":
    [
        {
            "patterns": [ "Gemfile", "Rakefile", "*.rb", "*.erb", "*.scss", "*.coffee", "*.thor", "*.rake", "*.rhtml", "*.less", "*.yaml","*.yml" ],
            "tab_size": 2,
            "translate_tabs_to_spaces": true
        },
        {
            "patterns": [ "*.html", "*.js", "*.css", "*.tpl" ],
            "tab_size": 2,
            "translate_tabs_to_spaces": true
        },
        {
            "patterns": [ "*.php" ],
            "tab_size": 4,
            "translate_tabs_to_spaces": false
        },
        {
            "patterns": [ "*.md", "*.markdown" ],
            "tab_size": 4,
            "translate_tabs_to_spaces": true
        },
        {
            "patterns": [ "*.py" ],
            "tab_size": 4,
            "translate_tabs_to_spaces": false
        }
    ]
}
```
