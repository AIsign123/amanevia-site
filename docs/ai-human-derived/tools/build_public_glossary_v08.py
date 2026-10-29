#!/usr/bin/env python3
"""v0.8 公開候補20語 -> public/tomorrow/glossary/glossary.json
入力: docs/ai-human-derived/v0.8/Amanevia_Glossary_Public_Candidates_20_v0.8.original.json（受領原本・無改変）
本スクリプトは (1) 原典照合で修正した文言 FIX (2) 検索用別名 ALIAS (3) 関連語 REL を適用し、
内部用ステータス項目を落として公開JSONを書き出す。"""
import json,os
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..'))
src=json.load(open(f'{ROOT}/docs/ai-human-derived/v0.8/Amanevia_Glossary_Public_Candidates_20_v0.8.original.json',encoding='utf-8'))
IFRPDF='https://ifr.org/img/worldrobotics/Definition_Service_Robots_2026.pdf'
FIX={
 'P037':dict(definition='対処すべき問題、または取り組むべき機会。'),
 'T014':dict(definition='取り組む変化・ニーズ・解決策と、何らかの関係を持つ個人や集団。',example='導入担当だけでなく、使う現場や運用担当の声も聴く。'),
 'T055':dict(definition='要求や成果物について、受け入れられたと言えるために満たすべき条件。'),
 'T018':dict(definition='目標や戦略を実現するために設定した業務プロセスの状況を、見守るための指標。'),
 'T052':dict(definition='技術の原理や、市場にニーズがあるかを、実際に試して確かめる取り組み。',source_section='概念実証（POC：Proof of Concept）（SBIR推進プログラム公募の説明）'),
 'T362':dict(definition='プロジェクトを進めるチームや意思決定者を支える、組織または機能。',
  caution='呼び名や役割は組織・制度で異なる。Project Management Officeを指すことも、Portfolio Management Officeを指すこともある（デジタル庁の用語集の「PMO」はPortfolio Management Office）。',
  secondary_url='https://www.digital.go.jp/assets/contents/node/basic_page/field_ref_resources/e2a06143-ed29-4f1d-9c31-0f06fca67afc/bb231f8c/20260715_resources_standard_guidelines_glossary_01.pdf'),
 'P018':dict(definition='開発する機能を短い期間（イテレーション）に区切り、各期間の終わりに動作を確認しながら進める開発の進め方。'),
 'P001':dict(definition='複雑な課題に対し、適応的な解決策で価値を生み出すことを助ける、軽量なフレームワーク。'),
 'T312':dict(source_section='Definition（NIST SP 800-218A）／同義語 GenAI（NIST AI 100-2e2025）'),
 'R003':dict(source_title='IFR / World Robotics 2025 – Service Robots（ISO 8373:2021の定義を引用）',source_url=IFRPDF,source_section='Section 1.1 / ISO 8373:2021 §3.6',
  caution='ISO 8373の定義には軸数などの条件がある。すべての自動機械を産業用ロボットと呼ぶわけではない。IFRの統計は2012年版の定義を使う年次もある。'),
 'R004':dict(definition='人や設備にとって役立つ作業を行うロボット。',source_title='IFR / World Robotics 2025 – Service Robots（ISO 8373:2021の定義を引用）',source_url=IFRPDF,source_section='Section 1.1 / ISO 8373:2021 §3.7',
  caution='個人用・業務用の区別は規格の定義そのものではない。産業用・医療用などとの分類は、用途や採用する規格の版による。'),
 'R012':dict(source_section='Robot definitions at ISO / Mobile robot'),
}
ALIAS={'R201':['BA','ビジネス分析'],'T018':['重要業績評価指標','Key Performance Indicator'],'T052':['POC','概念実証','Proof of Concept'],
 'T362':['プロジェクトマネジメントオフィス','Project Management Office','Portfolio Management Office','ピーエムオー'],
 'T312':['GenAI','Generative AI','ジェネレーティブAI'],'T329':['デジタルトランスフォーメーション','Digital Transformation'],
 'R001':['Physical AI'],'P018':['アジャイル','Agile'],'P001':['Scrum'],'T014':['ステークホルダー','Stakeholder'],'P034':['FR'],'P035':['NFR'],'R002':['Robot'],'R012':['AMR','AGV']}
REL={'R201':['P037','T014','P040'],'P037':['R201','P038','T014'],'T014':['R201','P037','P038'],'P038':['P037','P034','P035','T055'],
 'P034':['P038','P035'],'P035':['P038','P034'],'T055':['P038','P034','P035'],'P040':['R201','P037'],
 'T018':['T052','T055'],'T052':['T018','R001'],'T362':['T018','P018'],'P018':['P001','T362'],'P001':['P018'],
 'T312':['R001','T329'],'T329':['T312','T052'],'R001':['R002','T312','R012'],'R002':['R003','R004','R012','R001'],
 'R003':['R002','R004'],'R004':['R002','R003','R012'],'R012':['R002','R004']}
PAGES={ # 用語から関連ページへ（本文にその語や主題が実在するページのみ。相談への誘導ではない。編集者の整理）
 'R201':('/services/business-analysis','ビジネスアナリシス（BA）支援'),'T055':('/services/business-analysis','ビジネスアナリシス（BA）支援'),
 'P040':('/tomorrow/insights/customer-value','本当の価値を見つけ、選ばれ続けるために'),
 'T018':('/services/business-analysis','ビジネスアナリシス（BA）支援'),'T052':('/tomorrow/services/robotics','AI・ロボティクス社会実装の構想支援'),
 'T362':('/tomorrow/services/pmo','経営・プロジェクト伴走／PMO支援'),
 'T312':('/tomorrow/insights/ai-human','AIにまかせることと、人が大切にすること'),
 'R001':('/tomorrow/services/robotics','AI・ロボティクス社会実装の構想支援'),'R002':('/tomorrow/services/robotics','AI・ロボティクス社会実装の構想支援'),
 'R003':('/tomorrow/services/robotics','AI・ロボティクス社会実装の構想支援'),'R004':('/tomorrow/services/robotics','AI・ロボティクス社会実装の構想支援'),'R012':('/tomorrow/services/robotics','AI・ロボティクス社会実装の構想支援')}
KEEP=['id','term_ja','term_en','category','definition','example','question','caution','source_title','source_url','source_section','source_type','reviewed_on','secondary_url','homepage_featured']
ids={t['id'] for t in src['terms']}
assert len(ids)==20==len(src['terms'])
out=[]
for t in src['terms']:
    t=dict(t);t.update(FIX.get(t['id'],{}))
    o={k:t[k] for k in KEEP}
    if t['id'] in PAGES: o['page']={'href':PAGES[t['id']][0],'label':PAGES[t['id']][1]}
    o['aliases']=ALIAS.get(t['id'],[]);o['related']=REL.get(t['id'],[])
    assert all(r in ids for r in o['related'])
    out.append(o)
data={'version':'0.8-public-candidate-20','as_of':src['as_of'],'terms':out}
json.dump(data,open(f'{ROOT}/public/tomorrow/glossary/glossary.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out),'terms')
