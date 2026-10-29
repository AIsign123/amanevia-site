# Amanevia Webサイト v1.2 リリース候補 完了報告

**最終ステータス: READY_FOR_HUMAN_REVIEW(条件付き)** 条件: 下記「事実性の残課題」①(実績文の裏付け)を代表者が判断すること。マージ・本番デプロイ・SNS投稿は未実施。承認待ち。

## 1. 6項目の結果
| # | 項目 | 結果 |
|---|---|---|
| 1 | 無料表現 | トップの「ご相談は無料です」を指定文に置換。全公開ページで「無料」は第三者窓口の説明1件のみ(自社の無償約束ではない)。PR #6にも同じ置換を反映(0455056)。料金・契約の新規約束なし |
| 2 | 金融機関向け経験 | 「108金融機関」の数字を削除。「金融機関向けシステムの本番移行プロジェクトにも参画した経験があります。」へ変更。実績ログ冒頭に「以下は代表者個人の職務経験であり、Amanevia株式会社としての受注・納品実績ではありません」と明記 |
| 3 | トップ→Tomorrow | ナビ(721px以上)とフッター上部に「仕事と未来への気づき」+指定の説明文を追加。大きな新規セクションなし |
| 4 | URL/SEO/OGP | 36ページに canonical・og:url/title/description/image・twitter:card を設定(正規URLは `https://amanevia.co.jp/tomorrow…`、末尾スラッシュなし)。OGP画像 1200×630 は自社ロゴ+文字で作成(要承認)。公開切替スクリプトで noindex・帯を除去し sitemap.xml(37URL)・robots.txt を生成。プレビューは noindex 維持 |
| 5 | 404 | `public/404.html` 追加(ホーム/Tomorrow/サービスへのリンク、メール案内、モバイル・キーボード対応)。firebase.json に rewrites/redirects なし。HTTP 404 をローカル模擬で確認 |
| 6 | 4つの入口 | `/tomorrow` を4入口(課題/AI・ロボ・学び/サービス/会社・代表)に再編。旧「3つの始め方」の固有内容(悩み・BA/PMO伴走・リーダー8視点)は文章を保って4入口とリーダーカードに移設 |

## 2. 変更ファイル(origin/main 比)
- 変更: `public/index.html`(5か所のみ)、`.gitignore`(`__pycache__/` を1行追加)
- 追加: `public/404.html`、`public/tomorrow/**`(36ページ+共通資産+`assets/og-default.png`)、`public/services/business-analysis/index.html`、`docs/**`(報告・台帳・`tools/release_switch.py`)

## 3. コミット
- v1.1: 3136ffa, e93a11c
- v1.2 本体: 0500a69
- main(PR #3)の取り込みマージ: d125cfc(履歴の書き換えなし)
- PR #6 側(feature/belief-v1-2): 0455056

## 4. PR間の競合
- PR #1 × #4、#1 × #5: 競合なし
- PR #1 × #6: `public/index.html` の実績ログ1か所で競合。**解決方針: #6の実績ログ版を採用**(#6は108の記載を含まない)。この方針で結合した場合、「無料」「108金融」0件、Tomorrowリンク2か所を確認
- PR #1 は main(3f2414e)と競合なし(mergeable_state: clean)

## 5. 自動テスト(ローカル Chromium、PASSのみ実行済み)
- 用語集(検索・カテゴリ・アンカー・20語): 50/50 PASS
- サイト全体(リンク・見出し・モバイル): 31/31 PASS
- v1.2: 52/52 PASS(無料・108の除去、会社情報表の維持、top→Tomorrow到達、head タグ全36ページ、OGP画像200・1200×630、公開切替後の noindex 残存なし・sitemap 37URL一致、404の状態/リンク/キーボード/モバイル、4入口)
- プレビュー(Firebase)実機: トップに新ナビ・新文言あり、108/無料なし、`/404` の案内ページ表示を確認。`/nope` は取得エラー(非2xx)だが、数値のHTTPステータスは取得ツールで確認不可 → **プレビュー実機の404ステータス: 部分確認**
- **NOT_RUN: メールの実着信**。方法: 外部のメールアカウントから contact@amanevia.co.jp に件名「サイト確認」で送信 → 受信箱に届くことを確認。期待結果: 数分以内に着信

## 6. スクリーンショット
会話に添付(PC/モバイル: トップ、/tomorrow、用語集、出典、サービス、BA、代表者、404)

## 7. 事実性の残課題
1. **実績文**: 「金融機関向けシステムの本番移行に参画した経験」は、本人記載以外の裏付け資料を確認できていません(Drive検索で資料なし)。確認できない場合は当該1文のみ削除(1行)。
2. 「以下は代表者個人の職務経験」という区分は代表者の確認が必要
3. 問い合わせ先の不一致: 現行の本番トップの mailto は `akira.inadomi@amanevia.com`、Tomorrow/404 は `contact@amanevia.co.jp`(PR #6 は contact@ に統一)。統一方針と contact@ の受信を要確認
4. OGP画像の使用承認
5. 本番トップ自体には OGP・canonical がない(今回の範囲外)
6. S16(Google PAIR)は着想のみ。台帳に注記済み

## 8. 本番デプロイ手順とロールバック
手順(承認後のみ):
1. 公開用ブランチを feature/tomorrow-additive から作成
2. `python3 docs/ai-human-derived/tools/release_switch.py public --date <公開日>`(noindex・帯・「公開前」文言の除去、sitemap/robots 生成)
3. 差分確認 → PR → マージ(mainへのマージで Firebase Hosting に自動デプロイ)
4. PR #4→#5→#6 は別承認。#6 を取り込む際は競合を #6 側の実績ログで解決

ロールバック: Firebase コンソール(Hosting)のリリース履歴で直前のリリースへロールバック。またはリリース用マージコミットを `git revert` して main に反映(自動デプロイ)。

## 9. 公開後の確認
- 全ページに noindex がない(404 を除く)/ canonical・og が本番URL
- `https://amanevia.co.jp/sitemap.xml`、`/robots.txt` の取得
- 未知URLが HTTP 404 で案内ページを返す
- `https://amanevia.co.jp/tomorrow/` が `/tomorrow` に転送される
- OGP: LinkedIn Post Inspector 等で画像と題名を確認
- トップのナビ・フッターから Tomorrow に到達
- メールの実着信テスト

## 10. LinkedIn・note 用 URL 候補(公開後のみ使用。現在は未公開で404になります)
- https://amanevia.co.jp/tomorrow
- https://amanevia.co.jp/tomorrow/glossary
- https://amanevia.co.jp/tomorrow/concerns
- https://amanevia.co.jp/tomorrow/leadership
- https://amanevia.co.jp/tomorrow/services
