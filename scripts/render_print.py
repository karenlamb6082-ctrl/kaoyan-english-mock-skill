"""Render separate, self-contained print HTML files; not final PDF QA."""
import argparse
import base64
import html
import json
import re
import sys
from pathlib import Path
from validate_paper import read_json, validate, local_asset

CSS = """
@page {size:A4; margin:18mm;}
body {font-family:"Times New Roman","Noto Serif CJK SC","SimSun",serif; font-size:11pt; line-height:1.4; color:#000;}
main {max-width:174mm; margin:auto;}
h1,h2,h3 {break-after:avoid;}
h1,h2 {text-align:center;}
p.body {text-indent:2em; margin:.55em 0;}
.directions,.caption {text-indent:0;}
.directions {overflow-wrap:anywhere;}
.page {break-before:page;}
.cover {text-align:center; padding-top:35mm; min-height:210mm;}
.question {break-inside:avoid; margin:5mm 0;}
.options {display:grid;grid-template-columns:1fr 1fr;gap:1mm 4mm;}
table {width:100%;border-collapse:collapse;}
td,th {vertical-align:top;padding:1.5mm;}
.cloze td {border:none;font-size:10pt;}
img {display:block;max-width:100%;height:auto;margin:4mm auto;}
.caption {text-align:center;}
u {text-decoration-thickness:1px;text-underline-offset:3px;}
.note {border-top:1px solid #777; padding-top:3mm;}
@media screen {body{background:#eee;} main{background:white;padding:18mm;}}
"""
def esc(text):
    return html.escape(str(text),quote=True)
def marked(text):
    out=esc(text)
    out=re.sub(r"\{\{(\d+)\}\}(.*?)\{\{/\1\}\}",
               lambda m:f"<u><b>{m[1]}.</b> {m[2]}</u>",out,flags=re.S)
    return re.sub(r"\{\{(\d+)\}\}",lambda m:f" <b>{m[1]}</b> __________ ",out)
def para(text,kind="body"):
    return f'<p class="{kind}">{marked(text).replace(chr(10),"<br>")}</p>'
def question(q):
    return (f'<div class="question"><b>{q["id"]}. {esc(q.get("stem",""))}</b>'
            +'<div class="options">'+''.join(f'<div>[{key}] {esc(value)}</div>' for key,value in q["options"].items())
            +'</div></div>')
def document(title,body):
    return '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>'+esc(title)+'</title><style>'+CSS+'</style></head><body><main>'+body+'</main></body></html>'
def outputs(data,base):
    title=data["meta"]["title"]
    paper='<section class="cover"><h1>'+esc(title)+'</h1><h2>英语（一）训练卷</h2><p>姓名：________　日期：________</p><p>100分　建议用时180分钟</p><p>原创训练材料，非官方试题</p></section>'
    paper+='<h2 class="page">Section I Use of English</h2>'+para('Directions: Choose the best word(s) for each numbered blank and mark A, B, C or D. (10 points)','directions')
    for p in data["cloze"]["text"].split("\n\n"):paper+=para(p)
    paper+='<table class="cloze">'
    for q in data["cloze"]["questions"]:
        paper+='<tr><td>'+str(q["id"])+'</td>'+''.join('<td>['+k+'] '+esc(v)+'</td>' for k,v in q["options"].items())+'</tr>'
    paper+='</table>'
    for i,r in enumerate(data["readings"],1):
        paper+='<section class="page">'
        if i==1:paper+='<h2>Section II Reading Comprehension</h2><h3>Part A</h3>'+para('Read the texts and answer questions 21-40. (40 points)','directions')
        paper+=f'<h3>Text {i}</h3>'+''.join(para(p) for p in r["paragraphs"])
        paper+=''.join(question(q) for q in r["questions"])+'</section>'
    pb=data["part_b"]
    paper+='<section class="page"><h3>Part B</h3>'+para(pb["directions"],"directions")
    paper+=''.join(para(f"[{k}] {v}","directions") for k,v in pb["choices"].items())
    paper+=''.join(para(p) for p in pb["body"])
    if pb["display_mode"]=="prompts":
        paper+=''.join(para(f'{q["id"]}. {q["prompt"]}',"directions") for q in pb["items"])
    paper+='</section><section class="page"><h3>Part C</h3>'+para('Translate the five underlined parts into Chinese. (10 points)','directions')
    paper+=''.join(para(p) for p in data["translation"]["paragraphs"])+'</section>'
    paper+='<section class="page"><h2>Section III Writing</h2><h3>51. Part A</h3>'+para(data["writing_a"]["prompt"],"directions")
    paper+='<h3>52. Part B</h3>'+para(data["writing_b"]["prompt"],"directions")
    v=data["writing_b"]["visual"]; p=local_asset(base,v["path"]); raw=p.read_bytes()
    if p.suffix.lower()==".png":
        if not raw.startswith(b"\x89PNG\r\n\x1a\n"):raise ValueError("invalid PNG file")
        mime="image/png"
    else:
        if not raw.startswith(b"\xff\xd8"):raise ValueError("invalid JPEG file")
        mime="image/jpeg"
    paper+='<img alt="作文视觉材料" src="data:'+mime+';base64,'+base64.b64encode(raw).decode('ascii')+'">'
    paper+=para(v["caption"],"caption")+'</section>'
    answers='<h1>'+esc(title)+' · 答案与复盘</h1><p class="note">首次限时作答后再阅读。结构检查不证明答案唯一或真题难度等值。</p>'
    answers+='<h2>1—40 答案与证据</h2>'
    for q in data["cloze"]["questions"]+[q for r in data["readings"] for q in r["questions"]]:
        answers+=f'<div class="question"><b>{q["id"]}. {q["answer"]}　{esc(q["answer_text"])}</b>'+para(q["evidence"],"directions")
        if "traps" in q:answers+=para("选项边界："+"；".join(k+": "+t for k,t in zip("ABCD",q["traps"])),"directions")
        if q.get("strongest_distractor"):
            answers+=para("最强干扰项："+q["strongest_distractor"]+" — "+q["options"][q["strongest_distractor"]],"directions")
            answers+=para("支持它的最强理由："+q["strongest_distractor_case"],"directions")
            answers+=para("决定性边界："+q["decisive_boundary"],"directions")
        answers+='</div>'
    answers+='<h2>41—45 Part B</h2>'
    for q in pb["items"]:answers+=para(f'{q["id"]}. {q["answer"]} {q["answer_text"]}\n{q["evidence"]}',"directions")
    answers+='<h2>46—50 翻译</h2>'
    for q in data["translation"]["items"]:answers+=para(f'{q["id"]}. {q["answer"]}',"directions")
    answers+='<h2 class="page">写作参考</h2>'
    for part in ("writing_a","writing_b"):
        answers+=f'<h3>{data[part]["id"]}.</h3>'+para(data[part]["sample"])+para(data[part]["notes"],"directions")
    answers+='<h2 class="page">来源与边界</h2>'
    for s in data["sources"]:
        answers+=para(f'{s["title"]} / {s["publisher"]} / {s["date"] or "日期未记录"}\n{s["url"]}\n核验状态：{s["verification"]}\n保留：{s["retained"]}\n删去：{s["omitted"]}\n改写边界：{s["adaptation_boundary"]}',"directions")
    answers+='<h2>发布状态</h2>'+para(json.dumps(data["release"],ensure_ascii=False,indent=2),"directions")
    return {"test.html":document(title,paper),"answers.html":document(title+" · 答案",answers)}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paper",type=Path)
    ap.add_argument("--output-dir",required=True,type=Path)
    args=ap.parse_args()
    try:
        data=read_json(args.paper); base=args.paper.resolve().parent
        report=validate(data,base)
        if report["errors"]:raise ValueError("Structural validation failed:\n"+"\n".join(report["errors"]))
        rendered=outputs(data,base)
        targets=[args.output_dir/name for name in rendered]
        if any(p.exists() for p in targets):raise ValueError("Output exists: choose a new output directory; frozen files are not overwritten.")
        args.output_dir.mkdir(parents=True,exist_ok=True)
        for name,content in rendered.items():(args.output_dir/name).write_text(content,encoding="utf-8")
        print("Created test.html and answers.html. Browser PDF export and page-by-page QA remain required.")
        return 0
    except (OSError,ValueError,KeyError,TypeError) as ex:
        print(str(ex),file=sys.stderr);return 1
if __name__=="__main__":sys.exit(main())
