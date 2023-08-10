# Toggler

Toggler simplifies the process of configuring toggle commands for intricate settings such as Invisibles, Indent Guides, Rulers, and more. You also have the freedom to create your own custom toggles.

Access all toggle commands conveniently through the command palette. For more advanced utilization, refer to the [Settings](#Settings) section.

## Installation

**Method 1: Manual Installation**

1. Visit the [Toggler GitHub repository](https://github.com/gerardroche/sublime-toggler).
2. Click on the "Code" button and select "Download ZIP."
3. Extract the downloaded ZIP file.
4. Open Sublime Text and go to `Preferences -> Browse Packages...` to open the Packages folder.
5. Copy the "Toggler" folder from the extracted ZIP and paste it into the Packages folder.

**Method 2: Manual Git Repository Installation**

1. Open a terminal or command prompt.
2. Navigate to the Sublime Text Packages directory:
    - On Windows: `%APPDATA%\Sublime Text\Packages`
    - On macOS: `~/Library/Application Support/Sublime Text/Packages`
    - On Linux: `~/.config/sublime-text/Packages`
3. Clone the plugin repository directly into the Packages directory using Git:
   ```
   git clone https://github.com/gerardroche/sublime-toggler.git Toggler
   ```

## Commands

| Command                     | Type      | Setting                   | Default on/off
| :------                     |:--------- | :------------------------ |: -------------
| Toggle Fold Buttons         | Boolean   | `fold_buttons`            |
| Toggle Gutter               | Boolean   | `gutter`                  |
| Toggle Highlight Line       | Boolean   | `highlight_line`          |
| Toggle Indent Guides        | List      | `indent_guide_options`    | `["draw_normal", "draw_active"]` / `[]`
| Toggle Invisibles           | List      | `draw_white_space`        | `["all"]` / `["selection"]`
| Toggle Line Numbers         | Boolean   | `line_numbers`            |
| Toggle Preview on Click     | Boolean   | `preview_on_click`        |
| Toggle Rulers               | List      | `rulers`                  | `[80, 120]` / `[]`
| Toggle Save on Focus Lost   | Boolean   | `save_on_focus_lost`      |
| Toggle Spell Check          | Boolean   | `spell_check`             |

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
