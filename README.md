# Toggler

Toggler helps you configure toggle commands for complex settings like Invisibles, Indent Guides, Rulers, etc. You can create your own too.

All toggle commands are available from the command palette. For advanced usage see [Settings](#Settings).

## Installation

Close Sublime Text, then download or clone this repository to a directory named **Toggler** in the Sublime Text Packages directory for your platform:

**Linux**

`git clone https://github.com/gerardroche/sublime-toggler.git ~/.config/sublime-text-3/Packages/Toggler`

**OSX**

`git clone https://github.com/gerardroche/sublime-toggler.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Toggler`

**Windows**

`git clone https://github.com/gerardroche/sublime-toggler.git %APPDATA%\Sublime/ Text/ 3/Packages/Toggler`

## Commands

Command                     | Type      | Setting                   | Default on/off
:------                     |:--------- | :------------------------ |: -------------
Toggle Fold Buttons         | `boolean` | `fold_buttons`            |
Toggle Highlight Line       | `boolean` | `highlight_line`          |
Toggle Indent Guides        | `list`    | `indent_guide_options`    | `["draw_normal", "draw_active"]` / `[]`
Toggle Invisibles           | `list`    | `draw_white_space`        | `["all"]` / `["selection"]`
Toggle Line Numbers         | `boolean` | `line_numbers`            |
Toggle Preview on Click     | `boolean` | `preview_on_click`        |
Toggle Rulers               | `list`    | `rulers`                  | `[80, 120]` / `[]`
Toggle Save on Focus Lost   | `boolean` | `save_on_focus_lost`      |

## Settings

To set on and off defaults for a setting, appending `"_toggle_on"` and `"_toggle_off"` to the setting.

**Example:** Set on/off defaults for the `draw_white_space` setting

```json
{
    "draw_white_space_toggle_on": ["all"],
    "draw_white_space_toggle_off": ["leading_mixed", "selection", "trailing", "isolated"],
}
```

**Example:** Set on/off defaults for the `indent_guide_options` setting

```json
{
    "indent_guide_options_toggle_on": ["draw_normal", "solid", "draw_active"],
    "indent_guide_options_toggle_off": [],
}
```

## Custom Commands

You can create your own toggle commands.

The command name is **`toggler`**.

The available arguments are as follows:

Argument  | Type                                    | Default
:-------- | :-------------------------------------- | :-------
`setting` | `string`                                |
`on`      | `boolean`, `integer`, `string`, `list`  | `true`
`off`     | `boolean`, `integer`, `string`, `list`  | `false`

If the `{on}` or `{off}` arguments are not provided the option is assumed to be boolean.

**Example Command**

Find your User directory via Menu → Browse Packages.

> User/Default.sublime-commands

```json
[
    {
        "caption": "Toggle Indent Guides",
        "command": "toggler",
        "args": {
            "setting": "indent_guide_options",
            "on": ["draw_normal", "draw_active"],
            "off": []
        }
    }
]
```

**Example Key Binding**

Menu → Preferences → Key Bindings

```json
[
    {
        "keys": ["ctrl+n"],
        "command": "toggler",
        "args": {
            "setting": "indent_guide_options",
            "on": ["draw_normal", "draw_active"],
            "off": []
        }
    },
]
```

## License

Released under the [GPL-3.0-or-later License](LICENSE).
