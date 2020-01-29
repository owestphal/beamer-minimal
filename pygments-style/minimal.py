# -*- coding: utf-8 -*-
"""
    pygments.styles.minimal
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    style based on solarized-dark
"""

from pygments.style import Style
from pygments.token import Comment, Error, Generic, Keyword, Name, Number, \
    Operator, String, Token


def make_style(colors):
    return {
        Token:               colors['base0'],

        Comment:             'italic ' + colors['base01'],
        Comment.Hashbang:    colors['base01'],
        Comment.Multiline:   colors['base01'],
        Comment.Preproc:     'noitalic ' + colors['magenta'],
        Comment.PreprocFile: 'noitalic ' + colors['base01'],

        Keyword:             colors['green'],
        Keyword.Constant:    colors['cyan'],
        Keyword.Declaration: colors['cyan'],
        Keyword.Namespace:   colors['orange'],
        Keyword.Type:        colors['yellow'],

        Operator:            colors['base011'],
        Operator.Word:       colors['green'],

        Name.Builtin:        colors['blue'],
        Name.Builtin.Pseudo: colors['blue'],
        Name.Class:          colors['blue'],
        Name.Constant:       colors['blue'],
        Name.Decorator:      colors['blue'],
        Name.Entity:         colors['blue'],
        Name.Exception:      colors['blue'],
        Name.Function:       colors['blue'],
        Name.Function.Magic: colors['blue'],
        Name.Label:          colors['blue'],
        Name.Namespace:      colors['blue'],
        Name.Tag:            colors['blue'],
        Name.Variable:       colors['blue'],
        Name.Variable.Global:colors['blue'],
        Name.Variable.Magic: colors['blue'],

        String:              colors['cyan'],
        String.Doc:          colors['base01'],
        String.Regex:        colors['orange'],

        Number:              colors['cyan'],

        Generic.Deleted:     colors['red'],
        Generic.Emph:        'italic',
        Generic.Error:       colors['red'],
        Generic.Heading:     'bold',
        Generic.Subheading:  'underline',
        Generic.Inserted:    colors['green'],
        Generic.Strong:      'bold',
        Generic.Traceback:   colors['blue'],

        Error:               'bg:' + colors['red'],
    }


COLORS = {
    'base03':  '#002b36',
    'base02':  '#073642',
    'base01':  '#62729a',
    'base011':  '#b278c2',
    'base00':  '#657b83',
    'base0':   '#839496',
    'base1':   '#93a1a1',
    'base2':   '#eee8d5',
    'base3':   '#fdf6e3',
    'yellow':  '#b58900',
    'orange':  '#cb4b16',
    'red':     '#dc322f',
    'magenta': '#d33682',
    'violet':  '#6c71c4',
    'blue':    '#268bd2',
    'cyan':    '#2aa198',
    'green':   '#859900',
}

class MinimalStyle(Style):
    styles = make_style(COLORS)
    background_color = COLORS['base03']
    highlight_color = COLORS['base02']
