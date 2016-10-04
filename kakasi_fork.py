# -*- coding: utf-8 -*-
#  kakasi_fork.py
#
# Copyright 2016 Eana Hufwe <ilove@1a23.com>
#
# Modified version of pyKakasi for word separation support.
#
# Copyright 2011, 2014 Hiroshi Miura <miurahr@linux.com>
#
#  Original Copyright:
# * KAKASI (Kanji Kana Simple inversion program)
# * $Id: jj2.c,v 1.7 2001-04-12 05:57:34 rug Exp $
# * Copyright (C) 1992
# * Hironobu Takahashi (takahasi@tiny.or.jp)
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either versions 2, or (at your option)
# * any later version.
# *
# * This program is distributed in the hope that it will be useful
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with KAKASI, see the file COPYING.  If not, write to the Free
# * Software Foundation Inc., 59 Temple Place - Suite 330, Boston, MA
# * 02111-1307, USA.
# */
__license__ = 'GPL 3'

import re
import sys
import os
from pykakasi.exceptions import *
import pykakasi

try:
    import anydbm as dbm
except:
    import dbm


def do(text):
    from pykakasi.j2h import J2H
    convJ = J2H()
    convJ._kanwa._kanwadict = dbm.open("ipa_kanwa.db", 'r')
    _MAXLEN = 32

    otext = []
    i = 0
    while True:
        if i >= len(text):
            break

        if convJ.isRegion(text[i]):
            w = min(i + _MAXLEN, len(text))
            (t, l) = convJ.convert(text[i:w])
            # print(t, l)
            source = text[i:i + l]

            if l <= 0:  # fails to convert
                i += 1  # pragma: no cover
                continue

            i = i + l
            # now i have been incremented..Clarify it by using var j
            j = i
            otext += strip_furigana(source, t)
        else:
            if len(otext) and type(otext[-1]) == str:
                otext[-1] += text[i]
            else:
                otext.append(text[i])
            i += 1

    return otext


def strip_furigana(kkm, kana):
    kanas = re.split("[^ぁ-ゟ]+", kkm)
    kanjis = re.findall("[^ぁ-ゟ]+", kkm)
    query = r"(.+)".join(kanas)
    furis = re.findall(query, kana)
    if not furis:
        print(kkm, kana, kanas, kanjis, query, furis)
        return kana
    furis = furis[0] if type(furis[0]) == tuple else furis
    l = []
    i = 0
    while i < len(kanas):
        if i == len(kanas) - 1:
            l.append(kanas[i])
        else:
            l += [kanas[i], (kanjis[i], furis[i])]
        i += 1
    return [i for i in l if i]
