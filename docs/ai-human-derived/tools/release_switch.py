#!/usr/bin/env python3
"""公開切替スクリプト（承認後のリリースPRでのみ実行する。今は実行しない）。
PRプレビュー用の noindex・「公開前モック」帯・プレビュー文言を外し、sitemap.xml / robots.txt を生成する。
使い方:  release_switch.py <publicディレクトリ> [--date YYYY-MM-DD]
  ・元ファイルを直接書き換える。通常は作業用コピーで試験し（tests参照）、リリースPRの専用ブランチで実行する。
  ・404.html は noindex を維持する（404ステータスのページは検索対象外）。
"""
import sys,os,re,glob,datetime
root=sys.argv[1];date=sys.argv[sys.argv.index('--date')+1] if '--date' in sys.argv else datetime.date.today().isoformat()
BASE='https://amanevia.co.jp'
NOIDX='<meta name="robots" content="noindex,nofollow">'
urls=['/'];n=0
files=sorted(glob.glob(root+'/tomorrow/**/index.html',recursive=True))+[root+'/services/business-analysis/index.html']
for f in files:
    t=open(f,encoding='utf-8').read();o=t
    t=t.replace(NOIDX,'')
    t=re.sub(r'<div class="preview-band">.*?</div>\n?','',t,flags=re.S)
    t=t.replace('（公開前の確認用ページ）','').replace('公開前の確認用ページ','')
    t=t.replace('<span>新しい入口</span>','<span>仕事と未来への気づき</span>').replace('>新しい入口</a>','>仕事と未来への気づき</a>').replace('aria-label="Amanevia 新規ページの入口へ"','aria-label="Amanevia 仕事と未来への気づき"')
    t=t.replace('既存の企業公式トップを開く ↗','会社のトップページへ ↗')
    open(f,'w',encoding='utf-8').write(t);n+=t!=o
    urls.append(f[len(root):-len('/index.html')])
open(root+'/sitemap.xml','w',encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{BASE}{u if u!="/" else "/"}</loc><lastmod>{date}</lastmod></url>\n' for u in urls)+'</urlset>\n')
open(root+'/robots.txt','w',encoding='utf-8').write(f'User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n')
print('switched',n,'pages;',len(urls),'urls in sitemap')
