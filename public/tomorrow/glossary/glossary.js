(function(){
'use strict';
var TERMS=[],BYID={},cat='';
var $=function(id){return document.getElementById(id)};
function normalize(s){return String(s==null?'':s).normalize('NFKC').toLocaleLowerCase('ja').replace(/\s+/g,' ').trim()}
function el(tag,cls,text){var e=document.createElement(tag);if(cls)e.className=cls;if(text!==undefined)e.textContent=String(text);return e}
function clear(n){while(n.firstChild)n.removeChild(n.firstChild)}
function safeUrl(v){try{var u=new URL(String(v||''));return u.protocol==='https:'?u:null}catch(e){return null}}
function link(u,label){var a=el('a','gl-source',label);a.href=u.href;a.target='_blank';a.rel='noopener noreferrer';return a}
function haystack(x){return normalize([x.term_ja,x.term_en,(x.aliases||[]).join(' '),x.definition,x.example].join(' '))}
function field(dl,name,val,cls){if(!val)return;var w=el('div');w.appendChild(el('dt','',name));w.appendChild(el('dd',cls||'',val));dl.appendChild(w)}
function card(x){
 var a=el('article','gl-term');a.id='t-'+x.id;
 var h=el('div');var h3=el('h3','',x.term_ja);h3.tabIndex=-1;h.appendChild(h3);if(x.term_en)h.appendChild(el('div','gl-en',x.term_en));a.appendChild(h);
 var m=el('div','gl-meta');m.appendChild(el('span','gl-tag',x.category));a.appendChild(m);
 a.appendChild(el('p','gl-def',x.definition));
 var dl=el('dl','gl-fields');field(dl,'例',x.example);field(dl,'注意したい点',x.caution,'caution');a.appendChild(dl);
 if(x.question){var n=el('div','gl-note');n.appendChild(el('strong','','明日への問い　'));n.appendChild(document.createTextNode(x.question));a.appendChild(n)}
 var d=el('details','gl-detail');d.appendChild(el('summary','','関連する言葉・参考資料'));var inner=el('dl');
 if(x.related&&x.related.length){var w=el('div');w.appendChild(el('dt','','関連する言葉'));var dd=el('dd','gl-rel');x.related.forEach(function(id){var r=BYID[id];if(!r)return;var l=el('a','',r.term_ja);l.href='#t-'+id;l.addEventListener('click',function(ev){ev.preventDefault();goTo(id)});dd.appendChild(l)});w.appendChild(dd);inner.appendChild(w)}
 var u=safeUrl(x.source_url);if(u){var b=el('div');b.appendChild(el('dt','','参考資料'));var dd2=el('dd');dd2.appendChild(link(u,x.source_title+'（'+u.hostname+'）'));dd2.appendChild(el('span','small muted','参照箇所：'+x.source_section+'／確認日：'+x.reviewed_on+'。参照先であり、第三者の推薦ではありません。'));var s=safeUrl(x.secondary_url);if(s)dd2.appendChild(link(s,'補足資料（'+s.hostname+'）'));b.appendChild(dd2);inner.appendChild(b)}
 d.appendChild(inner);a.appendChild(d);return a}
function render(){
 var q=normalize($('query').value);
 var list=TERMS.filter(function(x){return(!cat||x.category===cat)&&(!q||q.split(' ').every(function(w){return haystack(x).indexOf(w)>=0}))});
 $('resultCount').textContent=TERMS.length+'語中 '+list.length+'語を表示';
 $('empty').hidden=list.length!==0;
 var box=$('results');clear(box);var f=document.createDocumentFragment();list.forEach(function(t){f.appendChild(card(t))});box.appendChild(f)}
function setCat(v){cat=v;[].forEach.call(document.querySelectorAll('[data-cat]'),function(b){b.setAttribute('aria-pressed',b.getAttribute('data-cat')===cat?'true':'false')});render()}
function reset(){$('query').value='';setCat('')}
function goTo(id){reset();var c=$('t-'+id);if(!c)return;var h=c.querySelector('h3');c.scrollIntoView({block:'start'});if(h)h.focus({preventScroll:true});c.classList.add('gl-hit');setTimeout(function(){c.classList.remove('gl-hit')},2200);try{history.replaceState(null,'','#t-'+id)}catch(e){}}
function init(data){
 TERMS=data.terms||[];TERMS.forEach(function(t){BYID[t.id]=t});
 var cats=[];TERMS.forEach(function(t){if(cats.indexOf(t.category)<0)cats.push(t.category)});
 var g=$('cats');clear(g);var all=el('button','gl-chip','すべて');all.type='button';all.setAttribute('data-cat','');all.setAttribute('aria-pressed','true');g.appendChild(all);
 cats.forEach(function(c){var b=el('button','gl-chip',c);b.type='button';b.setAttribute('data-cat',c);b.setAttribute('aria-pressed','false');g.appendChild(b)});
 [].forEach.call(g.querySelectorAll('button'),function(b){b.addEventListener('click',function(){setCat(b.getAttribute('data-cat'))})});
 $('query').addEventListener('input',render);$('clear').addEventListener('click',function(){reset();$('query').focus()});$('clear2').addEventListener('click',function(){reset();$('query').focus()});
 var p=new URLSearchParams(location.search);if(p.get('q'))$('query').value=p.get('q').slice(0,120);
 if(p.get('area')==='robotics')cat='ロボティクス';
 setCat(cat);
 $('loading').hidden=true;
 if(/^#t-[A-Z]\d{3}$/.test(location.hash)){var id=location.hash.slice(3);if(BYID[id])setTimeout(function(){goTo(id)},0)}}
window.addEventListener('hashchange',function(){if(/^#t-[A-Z]\d{3}$/.test(location.hash)&&BYID[location.hash.slice(3)])goTo(location.hash.slice(3))});
fetch('/tomorrow/glossary/glossary.json?v=20261029e').then(function(r){if(!r.ok)throw new Error(r.status);return r.json()}).then(init).catch(function(){var l=$('loading');l.hidden=false;l.className='gl-error';l.setAttribute('role','alert');l.textContent='用語データを読み込めませんでした。時間をおいて、もう一度お試しください。'});
})();
