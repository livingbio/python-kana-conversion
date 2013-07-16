# -*- coding: utf-8 -*-

# regex patterns for substitutions
XU__PATTERN = ur'ッ(.)'                         # 小さい u'ッ' は直後の文字を２回に変換
LTU_PATTERN = ur'ッ$'                           # 最後の小さい u'ッ' は消去(?)
ER__PATTERN = ur'(.)ー'                         # u'ー'は直前の文字を２回に変換
N___PATTERN = ur'n(b|p)([aiueo])'               # n の後ろが バ行、パ行 なら m に修正
OO__PATTERN = ur'([aiueo])\1'                   # oosaka → osaka
MBA_PATTERN = ur'm(b|p)([aiueo])'               # m の後ろにバ行、パ行のときは u'ン' と変換
XTU_PATTERN = ur'([bcdfghjklmpqrstvwxyz])\1'    # 子音が続く時は u'ッ' と変換
A___PATTERN = ur'([aiueo])\1'                   # 母音が続く時は u'ー' と変換
MBA_SUB_PATTERN = ur'ン\1\2'
XU__SUB_PATTERN = ur'ッ\1'
A___SUB_PATTERN = ur'\1ー'
XTU_SUB_PATTERN = ur'\1\1'
LTU_SUB_PATTERN = ur''
ER__SUB_PATTERN = ur'\1\1'
N___SUB_PATTERN = ur'm\1\2'
OO__SUB_PATTERN = ur'\1'
JOIN_CHAR   = u'|'

# Word mappings
katakana = {
    u'ア':u'あ', u'イ':u'い', u'ウ':u'う', u'エ':u'え', u'オ':u'お',
    u'カ':u'か', u'キ':u'き', u'ク':u'く', u'ケ':u'け', u'コ':u'こ',
    u'サ':u'さ', u'シ':u'し', u'ス':u'す', u'セ':u'せ', u'ソ':u'そ',
    u'タ':u'た', u'チ':u'ち', u'ツ':u'つ', u'テ':u'て', u'ト':u'と',
    u'ナ':u'な', u'ニ':u'に', u'ヌ':u'ぬ', u'ネ':u'ね', u'ノ':u'の',
    u'ハ':u'は', u'ヒ':u'ひ', u'フ':u'ふ', u'ヘ':u'へ', u'ホ':u'ほ',
    u'マ':u'ま', u'ミ':u'み', u'ム':u'む', u'メ':u'め', u'モ':u'も',
    u'ヤ':u'や', u'ユ':u'ゆ', u'ヨ':u'よ', u'ラ':u'ら', u'リ':u'り',
    u'ル':u'る', u'レ':u'れ', u'ロ':u'ろ', u'ワ':u'わ', u'ヲ':u'を',
    u'ン':u'ん',

    u'ガ':u'が', u'ギ':u'ぎ', u'グ':u'ぐ', u'ゲ':u'げ', u'ゴ':u'ご',
    u'ザ':u'ざ', u'ジ':u'じ', u'ズ':u'ず', u'ゼ':u'ぜ', u'ゾ':u'ぞ',
    u'ダ':u'だ', u'ヂ':u'ぢ', u'ヅ':u'づ', u'デ':u'で', u'ド':u'ど',
    u'バ':u'ば', u'ビ':u'び', u'ブ':u'ぶ', u'ベ':u'べ', u'ボ':u'ぼ',
    u'パ':u'ぱ', u'ピ':u'ぴ', u'プ':u'ぷ', u'ペ':u'ぺ', u'ポ':u'ぽ',

    u'ァ':u'ぁ', u'ィ':u'ぃ', u'ゥ':u'ぅ', u'ェ':u'ぇ', u'ォ':u'ぉ',
    u'ャ':u'ゃ', u'ュ':u'ゅ', u'ョ':u'ょ',
    u'ヴ':u'ゔ', u'ッ':u'っ', u'ヰ':u'ゐ', u'ヱ':u'ゑ',
}

# Swap keys / values from kata to create hira dictionary
hiragana = dict([(v, k) for k, v in katakana.items()])

kana_asist = { u'a':u'ァ', u'i':u'ィ', u'u':u'ゥ', u'e':u'ェ', u'o':u'ォ', }

romaji = {
    u'a'  :u'ア', u'i'  :u'イ', u'u'  :u'ウ', u'e'  :u'エ', u'o'  :u'オ',
    u'ka' :u'カ', u'ki' :u'キ', u'ku' :u'ク', u'ke' :u'ケ', u'ko' :u'コ',
    u'sa' :u'サ', u'shi':u'シ', u'su' :u'ス', u'se' :u'セ', u'so' :u'ソ',
    u'ta' :u'タ', u'chi':u'チ', u'tu' :u'ツ', u'te' :u'テ', u'to' :u'ト',
    u'na' :u'ナ', u'ni' :u'ニ', u'nu' :u'ヌ', u'ne' :u'ネ', u'no' :u'ノ',
    u'ha' :u'ハ', u'hi' :u'ヒ', u'fu' :u'フ', u'he' :u'ヘ', u'ho' :u'ホ',
    u'ma' :u'マ', u'mi' :u'ミ', u'mu' :u'ム', u'me' :u'メ', u'mo' :u'モ',
    u'ya' :u'ヤ', u'yu' :u'ユ', u'yo' :u'ヨ',
    u'ra' :u'ラ', u'ri' :u'リ', u'ru' :u'ル', u're' :u'レ', u'ro' :u'ロ',
    u'wa' :u'ワ', u'wo' :u'ヲ', u'n'  :u'ン', u'vu' :u'ヴ',
    u'ga' :u'ガ', u'gi' :u'ギ', u'gu' :u'グ', u'ge' :u'ゲ', u'go' :u'ゴ',
    u'za' :u'ザ', u'ji' :u'ジ', u'zu' :u'ズ', u'ze' :u'ゼ', u'zo' :u'ゾ',
    u'da' :u'ダ', u'di' :u'ヂ', u'du' :u'ヅ', u'de' :u'デ', u'do' :u'ド',
    u'ba' :u'バ', u'bi' :u'ビ', u'bu' :u'ブ', u'be' :u'ベ', u'bo' :u'ボ',
    u'pa' :u'パ', u'pi' :u'ピ', u'pu' :u'プ', u'pe' :u'ペ', u'po' :u'ポ',

    u'kya':u'キャ', u'kyi':u'キィ', u'kyu':u'キュ', u'kye':u'キェ', u'kyo':u'キョ',
    u'gya':u'ギャ', u'gyi':u'ギィ', u'gyu':u'ギュ', u'gye':u'ギェ', u'gyo':u'ギョ',
    u'sha':u'シャ',               u'shu':u'シュ', u'she':u'シェ', u'sho':u'ショ',
    u'ja' :u'ジャ',               u'ju' :u'ジュ', u'je' :u'ジェ', u'jo' :u'ジョ',
    u'cha':u'チャ',               u'chu':u'チュ', u'che':u'チェ', u'cho':u'チョ',
    u'dya':u'ヂャ', u'dyi':u'ヂィ', u'dyu':u'ヂュ', u'dhe':u'デェ', u'dyo':u'ヂョ',
    u'nya':u'ニャ', u'nyi':u'ニィ', u'nyu':u'ニュ', u'nye':u'ニェ', u'nyo':u'ニョ',
    u'hya':u'ヒャ', u'hyi':u'ヒィ', u'hyu':u'ヒュ', u'hye':u'ヒェ', u'hyo':u'ヒョ',
    u'bya':u'ビャ', u'byi':u'ビィ', u'byu':u'ビュ', u'bye':u'ビェ', u'byo':u'ビョ',
    u'pya':u'ピャ', u'pyi':u'ピィ', u'pyu':u'ピュ', u'pye':u'ピェ', u'pyo':u'ピョ',
    u'mya':u'ミャ', u'myi':u'ミィ', u'myu':u'ミュ', u'mye':u'ミェ', u'myo':u'ミョ',
    u'rya':u'リャ', u'ryi':u'リィ', u'ryu':u'リュ', u'rye':u'リェ', u'ryo':u'リョ',
    u'fa' :u'ファ', u'fi' :u'フィ',               u'fe' :u'フェ', u'fo' :u'フォ',
    u'wi' :u'ウィ', u'we' :u'ウェ',
    u'va' :u'ヴァ', u'vi' :u'ヴィ', u've' :u'ヴェ', u'vo' :u'ヴォ',

    u'kwa':u'クァ', u'kwi':u'クィ', u'kwu':u'クゥ', u'kwe':u'クェ', u'kwo':u'クォ',
    u'kha':u'クァ', u'khi':u'クィ', u'khu':u'クゥ', u'khe':u'クェ', u'kho':u'クォ',
    u'gwa':u'グァ', u'gwi':u'グィ', u'gwu':u'グゥ', u'gwe':u'グェ', u'gwo':u'グォ',
    u'gha':u'グァ', u'ghi':u'グィ', u'ghu':u'グゥ', u'ghe':u'グェ', u'gho':u'グォ',
    u'swa':u'スァ', u'swi':u'スィ', u'swu':u'スゥ', u'swe':u'スェ', u'swo':u'スォ',
    u'zwa':u'ズヮ', u'zwi':u'ズィ', u'zwu':u'ズゥ', u'zwe':u'ズェ', u'zwo':u'ズォ',
    u'twa':u'トァ', u'twi':u'トィ', u'twu':u'トゥ', u'twe':u'トェ', u'two':u'トォ',
    u'dwa':u'ドァ', u'dwi':u'ドィ', u'dwu':u'ドゥ', u'dwe':u'ドェ', u'dwo':u'ドォ',
    u'mwa':u'ムヮ', u'mwi':u'ムィ', u'mwu':u'ムゥ', u'mwe':u'ムェ', u'mwo':u'ムォ',
    u'bwa':u'ビヮ', u'bwi':u'ビィ', u'bwu':u'ビゥ', u'bwe':u'ビェ', u'bwo':u'ビォ',
    u'pwa':u'プヮ', u'pwi':u'プィ', u'pwu':u'プゥ', u'pwe':u'プェ', u'pwo':u'プォ',
    u'phi':u'プィ', u'phu':u'プゥ', u'phe':u'プェ', u'pho':u'フォ',
}

romaji_asist = {
    u'si' :u'シ'  , u'ti' :u'チ'  , u'hu' :u'フ' , u'zi':u'ジ',
    u'sya':u'シャ', u'syu':u'シュ', u'syo':u'ショ',
    u'tya':u'チャ', u'tyu':u'チュ', u'tyo':u'チョ',
    u'cya':u'チャ', u'cyu':u'チュ', u'cyo':u'チョ',
    u'jya':u'ジャ', u'jyu':u'ジュ', u'jyo':u'ジョ', u'pha':u'ファ',
    u'qa' :u'クァ', u'qi' :u'クィ', u'qu' :u'クゥ', u'qe' :u'クェ', u'qo':u'クォ',

    u'ca' :u'カ', u'ci':u'シ', u'cu':u'ク', u'ce':u'セ', u'co':u'コ',
    u'la' :u'ラ', u'li':u'リ', u'lu':u'ル', u'le':u'レ', u'lo':u'ロ',

    u'mb' :u'ム', u'py':u'パイ', u'tho': u'ソ', u'thy':u'ティ', u'oh':u'オウ',
    u'by':u'ビィ', u'cy':u'シィ', u'dy':u'ディ', u'fy':u'フィ', u'gy':u'ジィ',
    u'hy':u'シー', u'ly':u'リィ', u'ny':u'ニィ', u'my':u'ミィ', u'ry':u'リィ',
    u'ty':u'ティ', u'vy':u'ヴィ', u'zy':u'ジィ',

    u'b':u'ブ', u'c':u'ク', u'd':u'ド', u'f':u'フ'  , u'g':u'グ', u'h':u'フ', u'j':u'ジ',
    u'k':u'ク', u'l':u'ル', u'm':u'ム', u'p':u'プ'  , u'q':u'ク', u'r':u'ル', u's':u'ス',
    u't':u'ト', u'v':u'ヴ', u'w':u'ゥ', u'x':u'クス', u'y':u'ィ', u'z':u'ズ',
}

zenkaku = {
    u'a': u'ａ', u'b': u'ｂ', u'c': u'ｃ', u'd': u'ｄ', u'e': u'ｅ',
    u'f': u'ｆ', u'g': u'ｇ', u'h': u'ｈ', u'i': u'ｉ', u'j': u'ｊ',
    u'k': u'ｋ', u'l': u'ｌ', u'm': u'ｍ', u'n': u'ｎ', u'o': u'ｏ',
    u'p': u'ｐ', u'q': u'ｑ', u'r': u'ｒ', u's': u'ｓ', u't': u'ｔ',
    u'u': u'ｕ', u'v': u'ｖ', u'w': u'ｗ', u'x': u'ｘ', u'y': u'ｙ',
    u'z': u'ｚ',
    u'A': u'Ａ', u'B': u'Ｂ', u'C': u'Ｃ', u'D': u'Ｄ', u'E': u'Ｅ',
    u'F': u'Ｆ', u'G': u'Ｇ', u'H': u'Ｈ', u'I': u'Ｉ', u'J': u'Ｊ',
    u'K': u'Ｋ', u'L': u'Ｌ', u'M': u'Ｍ', u'N': u'Ｎ', u'O': u'Ｏ',
    u'P': u'Ｐ', u'Q': u'Ｑ', u'R': u'Ｒ', u'S': u'Ｓ', u'T': u'Ｔ',
    u'U': u'Ｕ', u'V': u'Ｖ', u'W': u'Ｗ', u'X': u'Ｘ', u'Y': u'Ｙ',
    u'Z': u'Ｚ',
    u'0': u'０', u'1': u'１', u'2': u'２', u'3': u'３', u'4': u'４',
    u'5': u'５', u'6': u'６', u'7': u'７', u'8': u'８', u'9': u'９',
    u'-': u'ー', u'_': u'＿', u'.': u'。', u'(': u'「', u')': u'」',
}

zenkaku_assist = {}