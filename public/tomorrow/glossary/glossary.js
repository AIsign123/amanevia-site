(function(){
'use strict';
var BASE_COUNT=820,PAGE_SIZE=18,TERMS=[];
var $=function(id){return document.getElementById(id)};
var area='all',page=1,results=[];
function normalize(s){return String(s==null?'':s).normalize('NFKC').toLocaleLowerCase('ja').replace(/\s+/g,' ').trim()}
function newItem(x){return /^R\d{3}$/.test(x.id||'')}
var FEATURED=['Physical AI','Robot','Humanoid Robot','Business Analysis','Social Implementation','Industry Academia Collaboration','Co-creation','Compassion in Practice','Wisdom in Practice','Psychological Safety','PoC','VLA','Teleoperation','Tactile Sensor','Robot System','AGV','AMR','Robot Simulation'];
function featureRank(x){var i=FEATURED.indexOf(x.english);return i<0?999:i}
function categoryOf(x){return x.category||'その他'}
function flag(x){return String(x.source_status||'')}
var PUB=/(\.go\.jp|iso\.org|ifr\.org|nist\.gov|jpx\.co\.jp)$/;
function isOfficial(x){var r=x.source_refs||[];for(var i=0;i<r.length;i++){var u=safeUrl(r[i]);if(u&&PUB.test(new URL(u).hostname))return true}return false}
function isLegacy(x){return x.canonical_status==='deprecated'||x.canonical_status==='legacy'||flag(x).indexOf('legacy')>=0||x.legal_or_standard_status==='historical_or_legacy'}
function needsVerify(x){return x.legal_or_standard_status==='needs_current_verification'}
function belongs(x){return area==='all'||(area==='robotics'&&newItem(x)&&x.category!=='理念・思考')||(area==='values'&&x.category==='理念・思考')||(area==='consulting'&&(!newItem(x)||x.english==='Business Analysis'))}
var LEGAL_JA={needs_current_verification:'制度・条件は変わることがあります。現行の内容を、専門家や公式情報で確認してください。',historical_or_legacy:'旧制度・旧用語に関わる語です。現行制度と混同しないでください。',current_checked:'現行性を確認した記録があります（個別案件の判断は別です）。'};
function safeUrl(ref){var v=String(ref||'').replace(/^WEB_(PRIMARY|REFERENCE):/,'').trim();try{var u=new URL(v);return u.protocol==='https:'?u.href:null}catch(e){return null}}
function el(tag,cls,text){var e=document.createElement(tag);if(cls)e.className=cls;if(text!==undefined)e.textContent=String(text);return e}
function clear(n){while(n.firstChild)n.removeChild(n.firstChild)}
function setArea(v){area=v;page=1;[].forEach.call(document.querySelectorAll('[data-area]'),function(b){b.setAttribute('aria-pressed',b.getAttribute('data-area')===area?'true':'false')});populateCats();render()}
function populateCats(){var sel=$('category'),cur=sel.value;clear(sel);sel.appendChild(new Option('すべてのカテゴリ',''));var seen={},cats=[];TERMS.filter(belongs).forEach(function(x){var c=categoryOf(x);if(!seen[c]){seen[c]=1;cats.push(c)}});cats.sort(function(a,b){return a.localeCompare(b,'ja')});cats.forEach(function(c){sel.appendChild(new Option(c,c))});if(cats.indexOf(cur)>=0)sel.value=cur}
function matches(x,q){if(!q)return true;var parts=[x.english,x.japanese,x.definition,x.client_explanation,x.misuse_caution,x.reader_question,(x.aliases||[]).join(' '),(x.related_terms||[]).join(' '),x.category];var text=normalize(parts.join(' '));return q.split(/\s+/).every(function(w){return text.indexOf(w)>=0})}
function score(x,q){if(!q)return newItem(x)?0:1;var en=normalize(x.english),jp=normalize(x.japanese);if(en===q||jp===q)return 0;if(en.indexOf(q)===0||jp.indexOf(q)===0)return 1;return 2}
function field(inner,name,val,cls){if(!val)return;var w=el('div');w.appendChild(el('dt','',name));w.appendChild(el('dd',cls||'',val));inner.appendChild(w)}
function oneTerm(x){
 var a=el('article','gl-term');var h=el('div');h.appendChild(el('h3','',x.japanese||x.english));if(x.english&&x.english!==x.japanese)h.appendChild(el('div','gl-en',x.english));a.appendChild(h);
 var m=el('div','gl-meta');m.appendChild(el('span','gl-tag',x.category||'その他'));if(newItem(x))m.appendChild(el('span','gl-tag','追加候補'));if(isLegacy(x))m.appendChild(el('span','gl-tag warn','旧制度・旧語に注意'));else if(needsVerify(x))m.appendChild(el('span','gl-tag warn','制度・条件は要確認'));a.appendChild(m);
 a.appendChild(el('p','',x.client_explanation||x.definition||'定義は確認中です。'));
 if(x.reader_question){var n=el('div','gl-note');n.appendChild(el('strong','','明日への問い　'));n.appendChild(document.createTextNode(x.reader_question));a.appendChild(n)}
 var d=el('details','gl-detail');d.appendChild(el('summary','','詳しい説明・注意点・参考資料'));var inner=el('dl');
 if(x.definition!==x.client_explanation)field(inner,'定義',x.definition);
 field(inner,'誤解しやすい点',x.misuse_caution,'caution');
 if(x.related_terms&&x.related_terms.length)field(inner,'関連する言葉',x.related_terms.join(' / '));
 if(x.confusable_with&&x.confusable_with.length)field(inner,'混同しやすい言葉',x.confusable_with.join(' / '));
 if(x.legal_or_standard_status&&LEGAL_JA[x.legal_or_standard_status])field(inner,'制度・規格の確認状態',LEGAL_JA[x.legal_or_standard_status],'caution');
 if(x.scope_note)field(inner,'適用範囲',x.scope_note);
 if(x.not_for)field(inner,'この語の説明では判断できないこと',x.not_for);
 var cnt=0;
 function addLinks(label,list,note){var box=el('div');box.appendChild(el('dt','',label));var dd=el('dd');var c=0;
  for(var i=0;i<list.length&&c<3;i++){var u=safeUrl(list[i].url||list[i]);if(!u)continue;var l=el('a','gl-source',(list[i].title?list[i].title+'（':'')+new URL(u).hostname+(list[i].title?'）':'')+' を開く');l.href=u;l.target='_blank';l.rel='noopener noreferrer';dd.appendChild(l);c++}
  if(c){if(note)dd.appendChild(el('span','small muted',note));box.appendChild(dd);inner.appendChild(box);cnt+=c}}
 if(x.source_refs&&x.source_refs.length)addLinks(x.ref_state==='candidate'?'参考資料（候補・定義との照合は未了）':'参考資料',x.source_refs.map(function(r){return{url:r}}),'参照先であり、第三者の推薦ではありません。');
 if(x.domain_refs&&x.domain_refs.length)addLinks('この分野の公式資料（入口）',x.domain_refs,'分野を確認するための入口で、この語の定義を直接確認したものではありません。');
 if(!cnt)field(inner,'参考資料','国や公的機関などの資料での確認を進めています。');
 if(x.framework)field(inner,'関連する体系・枠組み',x.framework+(x.proposer?'（提唱主体の候補：'+x.proposer+'。原典での照合は未了）':''));
 if(x.note_v07)field(inner,'補足の注意',x.note_v07,'caution');
 if(x.category==='ロボティクス基礎'||x.category==='安全・規格')field(inner,'注意','現場への適用・法令適合・安全性の判断には、実際の機器・用途・最新版の規格と専門家による確認が必要です。','caution');
 d.appendChild(inner);a.appendChild(d);return a}
function render(){
 var q=normalize($('query').value),cat=$('category').value,s=$('source').value;
 results=TERMS.filter(function(x){return belongs(x)&&(!cat||x.category===cat)&&matches(x,q)&&(!s||(s==='official'?isOfficial(x):s==='legacy'?isLegacy(x):!isOfficial(x)))});
 results.sort(function(a,b){return (q?score(a,q)-score(b,q):featureRank(a)-featureRank(b))||((newItem(a)?0:1)-(newItem(b)?0:1))||String(a.japanese||a.english).localeCompare(String(b.japanese||b.english),'ja')});
 var pages=Math.max(1,Math.ceil(results.length/PAGE_SIZE));page=Math.max(1,Math.min(page,pages));
 $('resultCount').textContent='検索結果 '+results.length.toLocaleString('ja-JP')+' 語';$('pageInfo').textContent=page+' / '+pages+' ページ';$('pageLabel').textContent=page+' / '+pages;
 $('empty').hidden=results.length!==0;$('pagination').hidden=results.length<=PAGE_SIZE;$('prev').disabled=page<=1;$('next').disabled=page>=pages;
 var box=$('results');clear(box);var frag=document.createDocumentFragment();results.slice((page-1)*PAGE_SIZE,page*PAGE_SIZE).forEach(function(t){frag.appendChild(oneTerm(t))});box.appendChild(frag)}
function init(data){
 TERMS=data.terms||[];$('totalTerms').textContent=TERMS.length.toLocaleString('ja-JP');$('extraTerms').textContent=TERMS.filter(function(t){return /^R/.test(t.id)}).length.toLocaleString('ja-JP');
 [].forEach.call(document.querySelectorAll('[data-area]'),function(e){e.addEventListener('click',function(){setArea(e.getAttribute('data-area'))})});
 $('query').addEventListener('input',function(){page=1;render()});$('category').addEventListener('change',function(){page=1;render()});$('source').addEventListener('change',function(){page=1;render()});
 $('clear').addEventListener('click',function(){$('query').value='';$('source').value='';$('category').value='';setArea('all');$('query').focus()});
 function jump(){var h=$('resultCount');h.setAttribute('tabindex','-1');h.focus();h.scrollIntoView({block:'start'})}
 $('prev').addEventListener('click',function(){page--;render();jump()});$('next').addEventListener('click',function(){page++;render();jump()});
 var p=new URLSearchParams(location.search);if(p.get('q'))$('query').value=p.get('q').slice(0,120);populateCats();
 var ar=p.get('area');if(ar&&['robotics','values','consulting'].indexOf(ar)>=0)setArea(ar);else render();
 $('loading').hidden=true}
fetch('/tomorrow/glossary/glossary.json').then(function(r){if(!r.ok)throw new Error(r.status);return r.json()}).then(init).catch(function(){var l=$('loading');l.hidden=false;l.className='gl-error';l.setAttribute('role','alert');l.textContent='用語データを読み込めませんでした。時間をおいて、もう一度お試しください。'});
})();
