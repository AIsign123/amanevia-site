# -*- coding: utf-8 -*-
"""公開用 glossary.json を作る。方針：出典ページ自体がその語を説明していると確認できた語だけを載せる。
入力: docs/ai-human-derived/glossary-master.json（全語の台帳。非公開）
出力: docs/ai-human-derived/archive/glossary-217-verified-only-v0.8.json（非公開アーカイブ。公開ページは build_public_glossary_v08.py の20語）
確認記録: docs/ai-human-derived/glossary-verification-ledger.json"""
import json,sys,os,datetime
sys.path.insert(0,os.path.dirname(__file__))
from pm_terms import SRC,PM,EXIST
from acct_terms import SRC2,ACCT
from robo_terms import SRC3,ROBO
SRC.update(SRC2);SRC.update(SRC3)
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..'))
M=json.load(open(f'{ROOT}/docs/ai-human-derived/glossary-master.json',encoding='utf-8'))
byid={t['id']:t for t in M['terms']}
CHECK='2026-10-29'
J=lambda p,t:{'url':p,'title':t,'checked':CHECK}
jpx=lambda p,t:J('https://www.jpx.co.jp/glossary/'+p+'.html','JPX 用語集「'+t+'」')
EX_OTHER={ # id -> [refs]  いずれも2026-10-29にページを開いて、その語の説明があることを確認
 'T510':[jpx('ka/76','株式移転')],'T514':[jpx('ka/81','株式分割')],'T515':[jpx('ka/87','株主資本')],'T522':[jpx('ka/92','監査法人')],
 'T535':[jpx('ka/69','合併比率')],'T621':[jpx('sa/165','財務諸表')],'T646':[jpx('sa/194','資本準備金')],'T652':[jpx('sa/195','社債')],
 'T713':[jpx('ta/270','第三者割当増資')],'T810':[jpx('ra/471','連結財務諸表')],
 'T547':[J('https://www.jsda.or.jp/shijyo/minasama/greensheet/index.html','日本証券業協会「グリーンシート」（2018年3月31日に終了と記載）')],
 'T562':[J('https://www.nta.go.jp/taxes/shiraberu/taxanswer/hojin/5762.htm','国税庁 タックスアンサー No.5762 青色申告書を提出した事業年度の欠損金の繰越控除')],
 'T741':[J('https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1191.htm','国税庁 タックスアンサー No.1191 配偶者控除')],
 'T742':[J('https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1195.htm','国税庁 タックスアンサー No.1195 配偶者特別控除')],
 'T313':[J('https://support.google.com/analytics/answer/9191807?hl=ja','Googleアナリティクス ヘルプ「アナリティクスのセッションについて」')],
 'T327':[J('https://support.google.com/analytics/answer/12195621','Googleアナリティクス ヘルプ「エンゲージメント率と直帰率」')],
 'T166':[J('https://www.nist.gov/itl/ai-risk-management-framework','NIST AI Risk Management Framework')],
 'R125':[J('https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/','Google DeepMind「RT-2」')],
 'R126':[J('https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/','Google DeepMind「RT-2」')],
 'R110':[J('https://github.com/ros2/ros2_documentation/blob/rolling/source/ROS-Framework/interfaces/Topics-Services-Actions.rst','ROS 2 ドキュメント「Topics, Services, Actions」')],
 'R111':[J('https://github.com/ros2/ros2_documentation/blob/rolling/source/ROS-Framework/interfaces/Topics-Services-Actions.rst','ROS 2 ドキュメント「Topics, Services, Actions」')],
 'R112':[J('https://github.com/ros2/ros2_documentation/blob/rolling/source/ROS-Framework/interfaces/Topics-Services-Actions.rst','ROS 2 ドキュメント「Topics, Services, Actions」')],
 'R113':[J('https://github.com/ros2/ros2_documentation/blob/rolling/source/ROS-Framework/interfaces/Topics-Services-Actions.rst','ROS 2 ドキュメント「Topics, Services, Actions」')],
 'R032':[J('https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly/grasping','NIST「Grasping」')],
 'R094':[J('https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly/grasping','NIST「Grasping」')],
 'R045':[J('https://moveit.picknik.ai/main/doc/concepts/motion_planning.html','MoveIt「Motion Planning」')],
 'T362':[],
}
CATJA={'Performance Management':'指標・目標','Consulting & Delivery':'プロジェクト管理の基本','Product Framework':'事業・プロダクト','Consulting Core':'ステークホルダー・価値','Project Delivery':'プロジェクト管理の基本','Delivery':'スコープ・要件','Decision & Portfolio':'プロジェクト管理の基本','Measurement & Delivery':'スケジュール','Corporate Reorganization':'会社の再編・資本','Equity & Capital':'会社の再編・資本','Financial Statements':'財務諸表・会計','Audit & Assurance':'財務諸表・会計','M&A':'会社の再編・資本','Corporate Finance':'会社の再編・資本','Legacy Capital Market':'資本市場','Corporate Tax':'税務（法人税）','Personal Tax':'税務（所得税）','SEO & Web Analytics':'Web分析・SEO','AI Governance Framework':'AIガバナンス'}
BOILER=('フレームを埋めること自体を成果とせず',)
def refs_of(keys): return [J(*SRC[k]) for k in keys]
out=[];ledger={}
def base(t):
    r={k:t.get(k) for k in('id','english','japanese','category','definition','client_explanation','misuse_caution','related_terms','aliases','confusable_with','legal_or_standard_status','scope_note','not_for','reader_question','framework','proposer','note_v07') if t.get(k)}
    r['category']=CATJA.get(r['category'],r['category'])
    r.setdefault('related_terms',[]);r.setdefault('aliases',[])
    if r.get('misuse_caution','').startswith(BOILER): del r['misuse_caution']
    if r.get('not_for','').startswith('単独で成果保証'): del r['not_for']
    return r
for tid,keys in EXIST.items():
    r=base(byid[tid]);r['verified_refs']=refs_of(keys);out.append(r)
for tid,refs in EX_OTHER.items():
    if tid=='T362': continue
    r=base(byid[tid]);r['verified_refs']=refs;out.append(r)
# PMOは出典の説明に合わせて定義を修正して掲載
t=base(byid['T362'])
t['definition']='デジタル庁の標準ガイドライン群では、PMOを府省内のIT施策を全体として管理する組織（Portfolio Management Office）、PJMOを個々のプロジェクトを遂行し進捗を管理する組織と区別している。一般にPMOは、プロジェクトの標準化・可視化・リスクや課題の管理などを支援する機能・組織を指して使われ、組織によって意味が異なる。'
t['client_explanation']=t['definition'];t['misuse_caution']='「PMO」は、組織や資料によって指す範囲が異なる。使うときは、全体管理か個別プロジェクトの推進かを確かめる。'
t['verified_refs']=refs_of(['DS130','DS120']);out.append(t)
for i,(ja,en,cat,df,cau,rel,src,al) in enumerate(PM,1):
    r={'id':'P%03d'%i,'japanese':ja,'english':en,'category':cat,'definition':df,'client_explanation':df,'aliases':al,'related_terms':rel,'verified_refs':refs_of(src),'scope_note':'本用語集による要約。原文の正式な訳文ではありません。'}
    if cau: r['misuse_caution']=cau
    out.append(r)
for i,(ja,en,cat,df,cau,rel,src,al) in enumerate(ACCT,1):
    r={'id':'A%03d'%i,'japanese':ja,'english':en,'category':cat,'definition':df,'client_explanation':df,'aliases':al,'related_terms':rel,'verified_refs':refs_of(src),'scope_note':'本用語集による要約。原文の正式な文言ではありません。実務では国税庁などの最新の案内で確認してください。'}
    if cau: r['misuse_caution']=cau
    out.append(r)
for (rid,ja,en,cat,df,cau,rel,src,al) in ROBO:
    r={'id':rid,'japanese':ja,'english':en,'category':cat,'definition':df,'client_explanation':df,'aliases':al,'related_terms':rel,'verified_refs':refs_of(src),'scope_note':'本用語集による要約。原文の正式な文言ではありません。規格の本文は、各規格の最新版で確認してください。'}
    if cau: r['misuse_caution']=cau
    out.append(r)
# 関連語は公開語だけに限定
names=set()
for r in out:
    for k in [r['japanese'],r['english']]+r.get('aliases',[]): names.add(k)
for r in out:
    r['related_terms']=[x for x in r.get('related_terms',[]) if x in names]
    r['confusable_with']=[x for x in r.get('confusable_with',[]) if x in names]
    ledger[r['id']]=[{'url':v['url'],'title':v['title'],'checked':v['checked']} for v in r['verified_refs']]
data={'version':'0.8-verified-only','as_of':CHECK,'terms':out}
json.dump(data,open(f'{ROOT}/docs/ai-human-derived/archive/glossary-217-verified-only-v0.8.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
json.dump({'checked':CHECK,'rule':'出典ページ自体がその語を説明していることを、確認日にページを開いて確認できた語のみ公開','entries':ledger},open(f'{ROOT}/docs/ai-human-derived/glossary-verification-ledger.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out),'published of',len(M['terms']),'master + new PM',len(PM),'+ ACCT',len(ACCT),'+ ROBO',len(ROBO))
