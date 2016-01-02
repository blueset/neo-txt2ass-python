# neo-txt2ass-python
## Need to check
* [ ] Check font list and font name compatibility between web(js), python, and .ass file.
* [ ] Contact author of rhythmicalyrics for support suwa.mizushiki@gmail.com
 
## Basic functions
* parse RhythmicaLyrics lyric files and ruby
    * Create a data format for timetag, ruby, ruby timetag, inline line-number and style configurations
* Video meta
    * Video size
    * time offset
    * prepend and append time for lines (logic included)
* Karaoke style settings
    * Positions (margin)
        * ruby padding
        * ruby style
    * Font face style and size:
        * Basic, ruby, song name (always on top)
    * Colors
        * Before wipe/After wipe: border/shadow/color
* Karaoke processing
    * Auto line wrap (on python)

## File format
### What do we need?
* Main format: JSON
* Song meta: Song name, info lines
* Ruby styles `[start, center, space-between, space-around]`
* Individual styles:
    * Style name, mode (normal, customize)
    * Normal: [Before&After wipe] Border, shadow, color
    * Customize: ASS templates
    * Script: Border, Shadow, Color
* Lyrics proceeding
* For every screen
    * number of lines
    * For every line
        * For every character set
            * Character(s)
            * Style
            * Begin time
            * End time
            * Ruby (For every ruby character set)
                * Characters
                * begin time
                * end time

### Sample
```json
{
    "song-name": "初音ミクの消失 Demo ver",
    "song-info": "词曲：cosMo@暴走P\nアレンジ：Eana Hufwe\nPV: Eana Hufwe",
    "ruby-style": "space-between",
    "video": {
        "width": 1024,
        "height": 768
    },
    "offset": -50,
    "prepend": 2000,
    "append": 1000,
    "fade-in": true,
    "fade-out": true,
    "font": {
        "font-family": "Source Han Sans JP",
        "font-variant": "Normal",
        "font-size": 20,
        "ruby-family": "Source Han Sans JP",
        "ruby-variant": "Normal",
        "ruby-size": 10,
        "ruby-margin-bottom": 10
    },
    "padding": {
        "bottom": 10,
        "left": 10,
        "right": 10
    },
    "styles": {
        "miku": {
            "mode": "normal",
            "before-border": "000000ff", // RGBA
            "before-shadow": "ffffff00",
            "before-color": "0000ffff",
            "after-border": "0000ffff",
            "after-shadow": "00000000",
            "after-color": "ffffffff"
        },
        "tianyi": {
            "mode": "normal",
            "before-border": "000000ff",
            "before-shadow": "ffffff00",
            "before-color": "66ccffff",
            "after-border": "66ccffff",
            "after-shadow": "00000000",
            "after-color": "ffffffff"
        }
    },
    "screens": [
        { // screen starts
            "line-count": 2,
            "lines": [
                [ // line starts
                    {
                        "char": "信",
                        "style": "miku",
                        "begin": 1300, // milliseconds
                        "end": 1500,
                        "ruby": [
                            {
                                "char": "し",
                                "begin": 1300,
                                "end": 1340
                            },
                            {
                                "char": "ん",
                                "begin": 1340,
                                "end": 1350
                            }
                        ]
                    },
                    {
                        "char": "じ",
                        "style": "miku",
                        "begin": 1500, // milliseconds
                        "end": 1600,
                        "ruby": []
                    },
                    {
                        "char": "た",
                        "style": "miku",
                        "begin": 1600, // milliseconds
                        "end": 1700,
                        "ruby": []
                    },
                    {
                        "char": "も",
                        "style": "miku",
                        "begin": 1700, // milliseconds
                        "end": 1800,
                        "ruby": []
                    },
                    {
                        "char": "の",
                        "style": "miku",
                        "begin": 1800, // milliseconds
                        "end": 1900,
                        "ruby": []
                    },
                    {
                        "char": "は",
                        "style": "miku",
                        "begin": 1900, // milliseconds
                        "end": 2000,
                        "ruby": []
                    }
                ],
                [ // line starts
                    {
                        "char": "都合",
                        "style": "miku",
                        "begin": 2300, // milliseconds
                        "end": 2500,
                        "ruby": [
                            {
                                "char": "つ",
                                "begin": 2300,
                                "end": 2340
                            },
                            {
                                "char": "ごう",
                                "begin": 2340,
                                "end": 2500
                            }
                        ]
                    },
                    {
                        "char": "の",
                        "style": "miku",
                        "begin": 2500, // milliseconds
                        "end": 2600,
                        "ruby": []
                    },
                    {
                        "char": "い",
                        "style": "miku",
                        "begin": 2600, // milliseconds
                        "end": 2700,
                        "ruby": []
                    },
                    {
                        "char": "い",
                        "style": "miku",
                        "begin": 2700, // milliseconds
                        "end": 2800,
                        "ruby": []
                    },
                    {
                        "char": "妄",
                        "style": "miku",
                        "begin": 2800, // milliseconds
                        "end": 2900,
                        "ruby": [
                            {
                                "char": "も",
                                "begin": 2800,
                                "end": 2850
                            },
                            {
                                "char": "う",
                                "begin": 2850,
                                "end": 2900
                            }

                        ]
                    },
                    {
                        "char": "想",
                        "style": "miku",
                        "begin": 2900, // milliseconds
                        "end": 3000,
                        "ruby": [
                            {
                                "char": "そ",
                                "begin": 2900,
                                "end": 2950
                            },
                            {
                                "char": "う",
                                "begin": 2950,
                                "end": 3000
                            }

                        ]
                    },
                    {
                        "char": "を",
                        "style": "miku",
                        "begin": 3000, // milliseconds
                        "end": 3100,
                        "ruby": []
                    }
                ]
            ]
        },
        { // screen starts
            "line-count": 1,
            "lines": [
                [ // line starts
                    {
                        "char": "信",
                        "style": "miku",
                        "begin": 1300, // milliseconds
                        "end": 1500,
                        "ruby": [
                            {
                                "char": "し",
                                "begin": 1300,
                                "end": 1340
                            },
                            {
                                "char": "ん",
                                "begin": 1340,
                                "end": 1350
                            }
                        ]
                    },
                    {
                        "char": "じ",
                        "style": "miku",
                        "begin": 1500, // milliseconds
                        "end": 1600,
                        "ruby": []
                    },
                    {
                        "char": "た",
                        "style": "miku",
                        "begin": 1600, // milliseconds
                        "end": 1700,
                        "ruby": []
                    },
                    {
                        "char": "も",
                        "style": "miku",
                        "begin": 1700, // milliseconds
                        "end": 1800,
                        "ruby": []
                    },
                    {
                        "char": "の",
                        "style": "miku",
                        "begin": 1800, // milliseconds
                        "end": 1900,
                        "ruby": []
                    },
                    {
                        "char": "は",
                        "style": "miku",
                        "begin": 1900, // milliseconds
                        "end": 2000,
                        "ruby": []
                    }
                ]
            ]
        }
    ]
}

```
## Section 1: Web interface
Used to generate JSON request.
## Section 2: Python engine
Used to generate `.ass` subtitle file.
