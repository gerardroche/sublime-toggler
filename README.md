# Toggler

Toggle complex settings at the speed of thought.

## Installation

### Manual installation

Close Sublime Text, then download or clone this repository to a directory named **Toggler** in the Sublime Text Packages directory for your platform:

**Linux**

`git clone https://github.com/gerardroche/sublime-toggler.git ~/.config/sublime-text-3/Packages/Toggler`

**OSX**

`git clone https://github.com/gerardroche/sublime-toggler.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Toggler`

**Windows**

`git clone https://github.com/gerardroche/sublime-toggler.git %APPDATA%\Sublime/ Text/ 3/Packages/Toggler`

## Commands

Command                     | Description
:------                     | :----------
Toggle Fold Buttons         | Toggle `fold_buttons`
Toggle Highlight Line       | Toggle `highlight_line`
Toggle Indent Guides        | Toggle `indent_guide_options`; on: `["draw_normal", "draw_active"]`, off: `[]`
Toggle Invisibles           | Toggle `draw_white_space`; on: `"all"`, off: `"selection"`
Toggle Line Numbers         | Toggle `line_numbers`
Toggle Preview on Click     | Toggle `preview_on_click`
Toggle Rulers               | Toggle `rulers`; on: `[80, 120]`, off: `[]`
Toggle Save on Focus Lost   | Toggle `save_on_focus_lost`

## Settings

User settings can override the default on and off values for complex settings by appending `"_toggle_on"` and `"_toggle_off"` to the setting name.

For instance to customize the "off" value for Invisibles:

```js
"draw_white_space_toggle_off":
[
    "leading_mixed",
    "selection",
    "trailing",
    "isolated"
],
```

Another example customizing the "on" value for Indent Guides:

```js
"indent_guide_options_toggle_on":
[
    "draw_normal",
    "solid",
    "draw_active"
],
```

## Custom Commands

Command name: `toggler`

Argument  | Type     | Default  | Description
:-------- | :------- | :------- | :----------
`setting` | `string` |          | Setting name
`on`      |          | `true`   | Default on value
`off`     |          | `false`  | Default off value

**Example**

```json
{
    "caption": "Toggle Indent Guides",
    "command": "toggler",
    "args": {
        "setting": "indent_guide_options",
        "on": ["draw_normal", "draw_active"],
        "off": []
    }
}
```

## License

Released under the [GPL-3.0-or-later License](LICENSE).
