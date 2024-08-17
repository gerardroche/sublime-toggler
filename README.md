# Toggler

Toggler is a Sublime Text plugin that adds various toggle commands.

## Commands

| Command                     | Description
| :-------------------------- | :------------------------
| Toggle Fold Buttons         | `fold_buttons` setting.
| Toggle Gutter               | `gutter` setting.
| Toggle Highlight Line       | `highlight_line` setting.
| Toggle Indent Guides        | `indent_guide_options` setting.
| Toggle Indentation          | `show_indentation` setting.
| Toggle Invisibles           | `draw_white_space` setting.
| Toggle Line Numbers         | `line_numbers` setting.
| Toggle Preview on Click     | `preview_on_click` setting.
| Toggle Rulers               | `rulers` setting.
| Toggle Save on Focus Lost   | `save_on_focus_lost` setting.
| Toggle Spell Check          | `spell_check` setting.
| Toggle Syntax               | `show_syntax` setting.

## Advanced configuration

| Setting                   | Type      | On    | Off
| :------------------------ | :-------- | :---- | ---
| `draw_white_space`        | List      | `["all"]` | `["selection"]`
| `fold_buttons`            | Boolean   | `true` | `false`
| `gutter`                  | Boolean   | `true` | `false`
| `highlight_line`          | Boolean   | `true` | `false`
| `indent_guide_options`    | List      | `["draw_normal", "draw_active"]` | `[]`
| `line_numbers`            | Boolean   | `true` | `false`
| `preview_on_click`        | Boolean   | `true` | `false`
| `rulers`                  | List      | `[80, 120]` | `[]`
| `save_on_focus_lost`      | Boolean   | `true` | `false`
| `show_indentation`        | Boolean   | `true` | `false`
| `show_syntax`             | Boolean   | `true` | `false`
| `spell_check`             | Boolean   | `true` | `false`

### Setting default values

To configure a default value, append `_toggle_on` or `_toggle_off` to the setting:

```js
"draw_white_space_toggle_on": [
    "all"
],

"draw_white_space_toggle_off": [
    "leading_mixed",
    "selection",
    "trailing",
    "isolated"
],

"indent_guide_options_toggle_on": [
    "draw_normal",
    "solid",
    "draw_active"
],
```

### Creating custom commands

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

### Creating custom key bindings

```json
{
    "keys": ["ctrl+n"],
    "command": "toggler",
    "args": {
        "setting": "indent_guide_options",
        "on": ["draw_normal", "draw_active"],
        "off": []
    }
}
```

## Installation

### Git installation

1. Clone into the Sublime Text directory:

   Linux

   ```sh
   git clone https://github.com/gerardroche/sublime-toggler.git ~/.config/sublime-text/Packages/Toggler
   ```

   Mac

   ```sh
   git clone https://github.com/gerardroche/sublime-toggler.git ~/Library/Application Support/Sublime Text/Packages/Toggler
   ```

   Windows

   ```ps
   git clone https://github.com/gerardroche/sublime-toggler.git %APPDATA%\Sublime Text\Packages\Toggler
   ```

1. Restart Sublime Text

## License

Released under the [GPL-3.0-or-later License](LICENSE).
