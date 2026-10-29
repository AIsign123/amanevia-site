# 変更マップ（KEEP / UPDATE / ADD / PAUSE）

| 対象 | ブランチ／PR | 判定 | 内容 |
|---|---|---|---|
| `public/index.html` `#philosophy` | `feature/belief-v1-2`（PR #5 の上に積む） | UPDATE | v1.2の要点を反映。現在／研究／長期の3区分、CSSは `.scope-grid` 1ルールのみ追加 |
| `public/index.html` その他（ヒーロー・事業・強み・実績・会社概要・CTA・フッター） | 同上 | KEEP | 変更なし |
| `public/tomorrow/about/our-way/index.html` | `feature/tomorrow-additive`（PR #1） | ADD | v1.2第1〜3章の全文。noindex、「公開前モック」帯付き |
| `public/tomorrow/about/principles/index.html` | 同上 | UPDATE | WHY WE EXIST の平和／信念モデルをv1.2見出し・要点に更新、全文ページへのリンク |
| `public/tomorrow/assets/site.css` | 同上 | UPDATE | `.pull-q` 1ルール追加 |
| 代表者ページ・サービス・会社情報・写真 | — | KEEP | 変更なし |
| 既存トップ → `/tomorrow/about/our-way` へのリンク | — | PAUSE | 本番トップから公開前モックへ張るのはFounder判断 |
| ピアノ×AI構想、致知おすすめ書籍の一覧化 | — | PAUSE / 対象外 | 指示書どおり混ぜない。未確認の書名は作らない |

## 注意（ブランチの前後関係）
`feature/tomorrow-additive` 上の `public/index.html` は、まだPR #3/#5 を取り込む前の旧版。トップの更新は PR #5 → 新PRの順にマージして反映される。
