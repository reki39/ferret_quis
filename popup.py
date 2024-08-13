
import math
import PySimpleGUI as sg

QUIZ = [

{"問題":"メスはオスより大きくなる","答え":"No"},
{"問題":"トイレを覚える","答え":"Yes"},
{"問題":"爪切りの頻度は月一である","答え":"No"},
{"問題":"固まるトイレ砂は使っても良い","答え":"No"},
{"問題":"お風呂は必須である","答え":"No"},
{"問題":"一日の睡眠時間は約50%である","答え":"No"},
{"問題":"多頭飼いしやすい動物である","答え":"Yes"},
{"問題":"ワクチンの定期接種が必須である","答え":"Yes"},
{"問題":"一番なりやすい病気は皮膚疾患である","答え":"No"},
{"問題":"イタチ科はネコ目ネコ亜目である","答え":"No"}

]

ok = 0
for i,qdata in enumerate(QUIZ):

    q = qdata["問題"]
    a = qdata["答え"]

    user = sg.popup_yes_no(q,title=f"クイズ　第{i+1}問目")

    if user == a:
        sg.popup("正解")
        ok +=1

    else:
        sg.popup("不正解")

rate = math.floor(ok/len(QUIZ)*100)
sg.popup(f"{ok}問正解。正解率:{rate}%",title="成績")