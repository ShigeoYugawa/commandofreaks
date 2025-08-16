# commandofreaks/quotes/views.py


import random
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


QUOTES = [
    "グリーンベレーは朝飯前だ。今は腹が減っている。",
    "殺しを教えたのァ、てめえだぜ。",
    "どうも...。頼みがあるんだが、連れを起こさないでくれ。死ぬほど疲れてる",
    "お前は最後に殺すと約束したな？あれは嘘だ！",
    "こいつを使おう、奴にはもういらん。",
    "動けこのポンコツが！　動けってんだよ！。...この手に限る",
    "てめぇなんか怖かねぇ！……やあろう、ぶっ殺してやぁるぅうううう！！！",
    "ただのカカシですな。俺達なら瞬きする間に皆殺しにできる。忘れないことだ。",
    "こいよベネット！　銃なんか捨ててかかって来い！　……楽に殺しちゃつまらんだろう。ナイフを突き立て、俺が苦しみもがいて死んでいく様を見るのが望みだったんだろう。そうじゃないのかベネット？",
]


def quote_view(request: HttpRequest) -> HttpResponse:
    """
    コマンドーの名台詞を出力する
    """

    quote = random.choice(QUOTES) if request.method == "POST" else None
    return render(request, 'quotes/quote.html', {'quote': quote})
