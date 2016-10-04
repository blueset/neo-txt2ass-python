#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import kakasi_fork

demo_text = '「さぁ！　始めようか　未来の真贋（しんがん）鑑定を」\n「ああ！　騙されるな　永遠 嘯（うそぶ）く錬金術に」\n\n始まりは　失亡に　呼び覚まされた心猿（しんえん）\nやり直し　組み直し　形変えど　可換に寄り添う終焉\n\n夜を統べる魔物の王は直心（ひたごころ）の呵責（かしゃく）に潰（つい）え\n溶かした禁忌で模（かたど）りし神は　忘却の彼方へ\n電子の並列自我は　星枢（せいすう）の腕に引かれ崩落\n＝　所詮は生命の法則（ルール）逸脱した迷走\n命操る神々でさえ　何（いず）れ消え去る\n\n理（ことわり）　公式\n全ては　裏返される\n\nああ！　世界に生（しるし）偽り付しても\nああ！　破戒の罪代（つみしろ）　積みながらに掻き消える\n求めたのは　延長線ではない\n過去　未来　現在（いま）を　貫く　並行閃光（レイ）\n\n（Lalala...）\n\n持つ者も持たざる者も　何時（いつ）か至る道の果て\n行き止まり　立ち止まり　軌跡頼り　自切（じせつ）という愚（ぐ）犯す\n\n約束された安定は　倦怠（けんたい）が全て食らい尽くす\n0（たんじょう）消失織り成す歌姫（ぶんか）は　見せ掛けの循環\n輪廻の恋愛 譚（たん）は　乱数悪魔の讒構（ざんこう）に堕（お）ちる\n＝　所詮は時架けし法則（ルール）黙殺した遁走（とんそう）\n時を操る神々でさえ　逃れられない　\n\n運命　真実\nすべては　書き換え可能の\n（資質　抑圧　搾取　弾劾　格差　気運…　すら）\n筋書（シナリオ）\n\nああ！　崇めた過去を閉じた円環は\nああ！　やがて焼き切れる儚い短絡回路\n忘れていた　世界という理不尽\n輪を抜け見（まみ）える　理想の　解（かい）\n\nさぁ！　世界を　かたる　鍵を粉砕し\nさぁ！　死灰（しかい）と見紛（みまご）う　虚飾永遠（フェイクループ）に終止符を\n歴史の鎖から　解き放たれた\n我らに続く者達を　望み待とう'
demo_text = """まもなく、7番線の前の方に参ります電車は、
六時四十六分発、阿倍野橋行き、特急さくらライナーの前につなぎます。
一号車、二号車、三号車、四号車でございます。
電車の番号は、前から一号車、二号車の順で、
後ろに、五号車、六号車、七号車、八号車を繋いで、
八両編成となります。
つなぎ終わるまで、しばらくお待ち下さい。
つなぎ終わりましても、四号車と五号車の間は、通り抜け出来ません。
お手持ちの特急券の号車番号の車両に、ご乗車ください。
特急にご乗車の場合は、特急券が必要でございます。
特急券をお買い求めの上、ご乗車ください。
危険ですから、黄色い線までお下がりください。
"""

def strip_furigana(txt):
    # match all patterns that is a furigana
    brackets = {
        "\(": "\)",
        "（": "）"
    }
    furiganas = []
    lines = txt.split('\n')
    pattern = r"([^ \n\u3000ぁ-ゟァ-ヿ]+)%s([ぁ-ゟァ-ヿ]+)%s"
    re_patterns = [re.compile(pattern % (i, brackets[i])) for i in brackets]
    for i in lines:
        line_furi = []
        for j in re_patterns:
            line_furi += [(i.groups(), i.span()) for i in j.finditer(i)]
        line_furi.sort(key=lambda a: a[1])
        if line_furi:
            if i[:line_furi[0][1][0]]:
                ln = kakasi_fork.do(i[:line_furi[0][1][0]])
            else:
                ln = []
        else:
            if i:
                ln = kakasi_fork.do(i)
            else:
                ln = []

        for pos, j in enumerate(line_furi):
            upper = j[1][1]
            lower = len(i) if pos == len(line_furi) - 1 else line_furi[pos + 1][1][0]
            ln.append((j[0][0], j[0][1]))
            if i[upper:lower]:
                ln += kakasi_fork.do(i[upper:lower])

        furiganas.append(ln)
        
    # for i in brackets:
    #     print(i, brackets[i])
    #     furiganas += 
    # separables = txt[:furiganas[0][1][0]].split('\n')
    print(*furiganas, sep="\n")
    # for pos, i in enumerate(furiganas):
    #     upper = i[1][1]
    #     lower = len(txt) if pos == len(furiganas) - 1 else furiganas[pos + 1][1][0]
    #     separables += [(i[0][0], i[0][1])] + [txt[upper:lower]]
    # print(*separables, sep="\n")
    return furiganas

if __name__ == "__main__":
    strip_furigana(demo_text)
