# 既存資産と技術の確認結果(2026-10-29)

## 確認できたこと(実査)
- リポジトリ: AIsign123/amanevia-site。静的HTML、ビルド工程なし。Firebase Hosting(`public/`、cleanUrls:true、trailingSlash:false)。
- 本リポジトリの `main` を変更せず、作業ブランチ `feature/tomorrow-additive`(PR #1、ドラフト、未マージ)に追加。
- 既存の派生領域は `/tomorrow/*`(約30ページ)。共通デザインは `public/tomorrow/assets/site.css`、メニューは `site.js`。
- 全新規ページは `noindex,nofollow` と「公開前モック」帯つき。

## 確認できなかったこと(UNKNOWN)
- 本番 amanevia.co.jp の現行ルートとローカルの一致(サンドボックスから本番に到達できない)。
- 指示書にある `/ideas` `/sources` `/glossary` `/concerns/management` `/concerns/ai-it` は、**本リポジトリに存在しない**。別リポジトリ・別版の可能性があるが、場所は不明。
- 用語集(820語Candidate)・出典DB(SSOT)の所在。本リポジトリには無く、参照できていない。
- 指示書の「Next.js想定」は不採用。実際のrepoは静的HTMLのため、技術は入れ替えていない。
- 代表者写真・画像の権利確認(既存の素材のみ使用)。
