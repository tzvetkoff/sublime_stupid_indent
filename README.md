# Stupid Indent for Sublime Text 2

A Sublime Text 2 plugin to determine indentation settings based on filename rather than current indentation.

## Installation
If you're using the [Sublime Package Control](http://wbond.net/sublime_packages/package_control) plugin, you can install the plugin just like any other - `⌘⇧P`, `Install Package`, `Stupid Indent`.

The other way around is to manually clone the repository:

``` bash
# WARNING: This instructions apply only to Mac OS X
cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
git clone https://github.com/tzvetkoff/sublime_stupid_indent sublime_stupid_indent
```

## Configuration
Open your local preferences (`⌘,`), then drop a key like this:

``` json
{

    "stupid_indent": [
        {
            "patterns": ["Gemfile", "*.rb", "*.erb", "*.scss", "*.coffee"],
            "tab_size": 2,
            "translate_tabs_to_spaces": true
        },
        {
            "patterns": ["*.html", "*.js", "*.css"],
            "tab_size": 2,
            "translate_tabs_to_spaces": true
        },
        {
            "patterns": ["*.php"],
            "tab_size": 4,
            "translate_tabs_to_spaces": false
        },
        {
            "patterns": ["*.md", "*.markdown"],
            "tab_size": 4,
            "translate_tabs_to_spaces": true
        }
    ]

}
```
