# CLAUDE.md — SunFounder PiDog Documentation

## Repository Overview

This is the **SunFounder PiDog Kit** documentation repository, built with **Sphinx** using the
**Read the Docs** theme. The documentation lives entirely under `docs/source/` as RST files.

- **GitHub**: https://github.com/sunfounder/pidog
- **Shared submodule**: https://github.com/sunfounder/sf-shared (at `docs/source/_shared`)
- **Build system**: Sphinx (`docs/Makefile`, `docs/requirements.txt`)
- **License**: GPL-2.0

## Quick Start

```bash
# After cloning the repo, init the shared submodule
git submodule update --init

# Install Python deps and build
pip install -r docs/requirements.txt
cd docs && make html
```

The `.gitignore` contains `build*` — **never read, edit, or commit anything under
`docs/build/`**. That folder is build output only.

## Branch & Language Architecture

`docs-en` is the **source of truth**. All other language branches are translations that
must mirror `docs-en` in file structure, toctrees, section counts, and RST directives
exactly — differing only in the natural language of their prose.

| Branch | Language | `conf.py` setting | sf-shared branch |
|--------|----------|--------------------|------------------|
| `docs-en`  | English    | `language = 'en'` | `main`        |
| `docs-es`  | Spanish    | `language = 'es'` | `docs-es`     |
| `docs-de`  | German     | `language = 'de'` | (language)    |
| `docs-ja`  | Japanese   | `language = 'ja'` | (language)    |
| `docs-it`  | Italian    | `language = 'it'` | (language)    |
| `docs-fr`  | French     | `language = 'fr'` | (language)    |
| `docs-zh-cn` | Chinese  | `language = 'zh_CN'` | (language)  |
| `master` / `main` | (legacy) | — | — |

The `.gitmodules` file on each language branch points `docs/source/_shared` to the
corresponding branch of `sunfounder/sf-shared`. When switching branches, run
`git submodule update` to sync the submodule to the correct commit.

## Sync Protocol: `docs-en` → Other Languages

When `docs-en` is updated, every other language branch must be brought into parity.
The check-list for each translation branch:

1. **File existence**: every `.rst` file under `docs/source/` that exists in `docs-en`
   (excluding `_shared/` and `build/`) must also exist in the translation branch.
2. **Toctrees**: every `.. toctree::` directive must list the same entries in the same order.
3. **Section structure**: headings, sub-headings, `.. note::`, `.. important::`,
   `.. code-block::`, `.. list-table::` directives must match present-for-present.
4. **Images & videos**: image paths and `.. raw:: html` embeds are shared across
   languages — do NOT change paths during translation. Add new images to the same
   relative paths as `docs-en`.
5. **RST anchors**: labels like `.. _play_python:` must be identical across all languages
   (they are used for cross-references).
6. **Heading underlines**: `===` / `---` must be longer than the heading text (translations
   tend to be longer than English).
7. **Inline markup + CJK**: `**bold**`, `` `code` ``, `|subref|` followed by a CJK letter
   or `（` need a `\ ` escape (see Inline Markup and CJK Characters section above).

The only thing that should differ is the human-language prose.

## RST Heading Conventions

This is a hard rule for ALL rst files:

> **The underline (`===`, `---`, `~~~`, `^^^`) on the line immediately below a heading
> MUST be longer than the heading text itself.**

```
✅ Good:
A Very Long Section Title
==========================

✅ Good:
Short Title
------------

❌ Bad:
A Very Long Section Title
=========================

❌ Bad:
Short Title
-----------
```

### Heading hierarchy in use

| Level | Character | Used for |
|-------|-----------|----------|
| 1     | `=` | Document / chapter title |
| 2     | `-` | Section within a document |
| 3+    | `~` or `^` | Sub-sections (if needed) |

Examples from the codebase:

```rst
SunFounder Raspberry Pi Robot - PiDog
=================================================

Hardware
==================

21. Using OpenClaw to Control PiDog
========================================

1. Wake Up
===============

Quick Start OpenClaw
------------------------------

Installing PiDog Skill
------------------------------
```

## RST Style Rules

### Conditional / commented-out blocks
Use `..` prefix for developer notes and commented-out toctrees:
```rst
..  PiDog skill 短说明

..  把整个目录放到：
..  ~/.openclaw/workspace/skills/pidog-control/
```

### Community ad note
Most RST files start with a `.. note::` block containing the community Facebook ad.
Translate the ad into the target language. (Some files like `faq.rst` in `docs-es` have
an ad while `docs-en` doesn't — this is acceptable; don't add/remove ads to force
alignment on this cosmetic item.)

### Code blocks
Always specify the language:
```rst
.. code-block:: bash

.. code-block:: json

.. code-block:: python
```

### Cross-references
Use `:ref:` with anchor labels defined via `.. _label_name:`:
```rst
:ref:`quick_guide_python`
```
Labels must be identical across all language branches.

### Inline Markup and CJK Characters

RST inline markup — `**bold**`, `` `code` ``, ` ``code`` `, `|substitution|` — requires
the **closing delimiter** to be immediately followed by **whitespace, punctuation, or
end-of-line**. When translating to Chinese (or any CJK language), this rule is frequently
broken because:

- CJK characters are **letters**, not punctuation — they do NOT count as valid terminators
- Full-width punctuation like `，` `。` `：` `、` `）` IS recognized, but `（` (full-width
  left paren, Unicode Ps category) may NOT be recognized by all RST parsers

**Patterns that need `\ ` (backslash-escaped space) after the closing delimiter:**

| Pattern | Fix | Example |
|---------|-----|---------|
| `**text**CJK` | `**text**\ CJK` | `**not**compatible` → `**not**\ compatible` |
| `**text**（` | `**text**\ （` | `**Piper**（offline）` → `**Piper**\ （offline）` |
| `` `code`CJK `` | `` `code`\ CJK `` | same pattern |
| ` ``code``CJK ` | ` ``code``\ CJK ` | ` ``llama``模型` → ` ``llama``\ 模型` |
| ` ``code``（ ` | ` ``code``\ （ ` | ` ``llama``（模型）` → ` ``llama``\ （模型）` |
| `|subref|CJK` | `|subref|\ CJK` | same pattern |
| `|subref|（` | `|subref|\ （` | `|link_aliyun|（控制台）` → `|link_aliyun|\ （控制台）` |

**Patterns that are safe (no fix needed):**

| Pattern | Reason |
|---------|--------|
| `**text**：` | Full-width colon is punctuation |
| `**text**，` | Full-width comma is punctuation |
| `**text**。` | Full-width period is punctuation |
| `**text**、` | Full-width enumeration comma is punctuation |
| `**text**）` | Full-width right paren is punctuation |

**Post-translation check-list for each file:**
1. Search for `**` followed by a CJK letter or `（` → add `\ ` escape
2. Search for `` ` `` or ` `` ` followed by a CJK letter or `（` → add `\ ` escape
3. Search for `|xxx|` followed by a CJK letter or `（` → add `\ ` escape
4. Do NOT add `\ ` after punctuation characters (`：，。、）`)

### Images
```rst
.. image:: img/pidog.jpg
    :width: 300
    :align: center
```
Images are stored in `docs/source/img/` (project-wide) and `docs/source/<section>/img/`
(section-specific). Images shared across languages — do NOT rename or translate image
paths.

### Videos
Embedded via `.. raw:: html` with iframe — copy verbatim from `docs-en`.

## File Structure (55 owned RST files)

```
docs/
├── Makefile
├── requirements.txt          # sphinx==7.3.7, sphinx_rtd_theme==3.0.1, sphinx_copybutton
├── source/
│   ├── conf.py               # Language-specific (differs per branch)
│   ├── index.rst             # Root toctree
│   ├── appendix.rst
│   ├── assemble_video.rst
│   ├── faq.rst
│   ├── openclaw.rst
│   ├── ai_interaction/
│   │   ├── ai_interaction.rst
│   │   ├── python_ai_robot.rst
│   │   ├── python_llm_ollama.rst
│   │   ├── python_local_chatbot.rst
│   │   ├── python_online_llms.rst
│   │   ├── python_stt_vosk.rst
│   │   ├── python_tts_espeak_pico2wave.rst
│   │   └── python_tts_piper_openai.rst
│   ├── hardware/
│   │   ├── cpn_hardware.rst
│   │   ├── cpn_6dof_imu.rst
│   │   ├── cpn_battery.rst
│   │   ├── cpn_camera.rst
│   │   ├── cpn_dual_touch.rst
│   │   ├── cpn_rgb_board.rst
│   │   ├── cpn_robot_hat.rst
│   │   ├── cpn_sound_direction.rst
│   │   └── cpn_ultrasonic.rst
│   ├── python/
│   │   ├── play_with_python.rst
│   │   ├── py_0_calibrate.rst
│   │   ├── py_1_wakeup.rst
│   │   ├── py_2_function_demonstration.rst
│   │   ├── py_3_patrol.rst
│   │   ├── py_4_response.rst
│   │   ├── py_5_rest.rst
│   │   ├── py_6_be_picked_up.rst
│   │   ├── py_7_face_track.rst
│   │   ├── py_8_pushup.rst
│   │   ├── py_9_howling.rst
│   │   ├── py_10_balance.rst
│   │   ├── py_11_keyboard_control.rst
│   │   ├── py_12_app_control.rst
│   │   ├── py_13_ball_track.rst
│   │   ├── py_b1_init.rst
│   │   ├── py_b2_leg_move.rst
│   │   ├── py_b3_head_move.rst
│   │   ├── py_b4_tail_move.rst
│   │   ├── py_b5_stop_action.rst
│   │   ├── py_b6_preset_action.rst
│   │   ├── py_b7_speak.rst
│   │   ├── py_b8_read_distance.rst
│   │   ├── py_b9_rgb.rst
│   │   ├── py_b10_imu.rst
│   │   ├── py_b11_sound_direction.rst
│   │   ├── py_b12_dual_touch.rst
│   │   ├── py_b13_more.rst
│   │   ├── py_easy_coding.rst
│   │   ├── py_fun_project.rst
│   │   └── python_start/
│   │       ├── quick_guide_on_python.rst
│   │       ├── install_all_modules.rst
│   │       └── py_servo_adjust.rst
│   ├── img/                   # Project-wide images (shared across languages)
│   │   ├── pidog.jpg
│   │   ├── pidog_v1_box.png
│   │   ├── pidog_v2_box.png
│   │   └── openclaw/          # 18 OpenClaw screenshots
│   └── _shared/               # Git submodule (sunfounder/sf-shared)
│       ├── appendix/          # blynk_app, filezilla, remote_desktop, etc.
│       └── component/         # 54 component docs (cpn_*.rst)
```

## conf.py — Per-Branch Settings

The only line that MUST differ between language branches is:
```python
language = 'XX'
```

Everything else (extensions, html_theme, rst_epilog links, etc.) stays identical to
`docs-en`. The `rst_epilog` contains replacement strings like `|link_PiDog|` and
`|link_en_tutorials|` — these HTML links point to language-specific URLs but the
substitution names remain the same across branches.

## Requirements

```
sphinx==7.3.7
sphinx_rtd_theme==3.0.1
sphinx_copybutton
```

## Working on This Repo

### Before starting any task
1. Confirm which branch you're on (`git branch --show-current`)
2. If working on a translation, identify the baseline `docs-en` commit to track against
3. Run `git submodule update --init` if `_shared/` is empty

### When translating new content from `docs-en`
1. Copy the new/changed `.rst` files from `docs-en`
2. Translate the prose — do NOT change toctrees, anchors, image paths, or code blocks
3. Verify heading underlines are longer than their heading text
4. Check inline markup: `**`, `` ` ``, `|sub|` followed by CJK letters or `（` need `\ ` escape
5. Build to check for Sphinx warnings: `cd docs && make html 2>&1 | head -50`

### When adding new features to `docs-en`
1. Make changes to `docs-en` first
2. Verify with `cd docs && make html`
3. Then propagate the structural changes to each language branch

### Commit message style
Use conventional commits with `docs:` or `docs(LANG):` prefix:
```
docs: add OpenClaw troubleshooting section
docs(es): sync openclaw.rst with EN version
refactor(docs): restructure appendix to use shared submodule
```
