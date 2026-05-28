# SmartKeyboard

`SmartKeyboard` is a dynamic inline keyboard constructor for the aiogram framework.  
It provides a flexible and convenient way to build different kinds of `InlineKeyboardMarkup` objects (`aiogram.types.InlineKeyboardMarkup`).

The module works as an advanced wrapper around `InlineKeyboardBuilder` (`aiogram.utils.keyboard.InlineKeyboardBuilder`) and extends its functionality with powerful keyboard generation features.

---

## Features

### Standard Inline Keyboards

Create regular inline keyboards with a simple and clean API.

---

### Dynamic Multi-Page Keyboards

Build complex inline keyboards with automatic pagination support.

The module can automatically generate **"Next"** and **"Back"** navigation buttons, allowing users to switch between multiple keyboard pages seamlessly.

The pagination system is highly flexible and correctly handles complex keyboard layouts, including:

- rows with different numbers of buttons
- completely custom keyboard structures
- pages with unique layouts
- automatically adjusted navigation controls

For example:

- one page may contain:
  - a row with 3 buttons
  - a row with 5 buttons
  - a row with 4 buttons
- while another page may contain only a single row

The navigation logic adapts automatically to every layout configuration.

---

## Advantages

- Flexible keyboard generation
- Automatic pagination
- Fully customizable layouts
- Clean abstraction over aiogram keyboard builder
- Suitable for both small and large Telegram bots

---

## Based On

- `aiogram`
- `InlineKeyboardBuilder`
- `InlineKeyboardMarkup`

---
