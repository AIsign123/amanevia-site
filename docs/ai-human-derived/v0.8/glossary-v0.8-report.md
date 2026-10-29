# 基本用語集 v0.8（20語）実装報告・事実性監査

- 日付：2026-10-29　／　ブランチ：`feature/tomorrow-additive`（PR #1・ドラフト）　／　本番：**未公開・未マージ**
- 判定：**READY_FOR_HUMAN_REVIEW**（本番公開の承認ではありません。代表者の最終承認待ち）
- 限界：原典照合は作成と同じAIによる自己点検であり、外部の独立監査ではありません。

## A. 実装サマリ
- 変更ページ：`/tomorrow/glossary`（20語のみ）、`/tomorrow`（基本用語8語の入口を1セクション追加）。
- リンク調整2件：`/tomorrow/leadership`・`/tomorrow/about/principles` の旧リンク `?area=values` → `/tomorrow/glossary`（理念分野は20語に含まれないため。principlesのリンク文言も「基本用語集」へ）。
- 追加：`docs/ai-human-derived/tools/build_public_glossary_v08.py`、`docs/ai-human-derived/v0.8/`（受領JSON原本・本報告）。
- 217語データは削除せず `docs/ai-human-derived/archive/glossary-217-verified-only-v0.8.json` へ移動（非公開）。マスターデータ（glossary-master.json）は無変更。
- 公開されるのは20語のみ。保留語（R302,R078,R176,R125,R126,R162,T741,T742,T562,R067,R110,T087）は含まれません。

## B. 変更差分
- 変更：`public/tomorrow/glossary/{index.html,glossary.js,glossary.css,glossary.json}`、`public/tomorrow/index.html`（+1セクション）、`public/tomorrow/assets/site.css`（+1行）、上記リンク2ページ。
- 未変更：`public/index.html`、代表者写真・プロフィール、サービス各ページ、firebase設定、noindex・公開前モック帯。
- 実装方式：既存の静的HTML＋ローカルJSON。新規DB・検索サービス・外部通信なし。

### 受領JSONからの文言修正（原典照合による。原本は `…original.json` に保存）
| ID | 項目 | 旧 | 新 |
|---|---|---|---|
| P037 | 定義 | 解決したい問題、または実現したい機会や望ましい状態。 | 対処すべき問題、または取り組むべき機会。 |
| T014 | 定義 | 取り組む変化や解決策に関係し、影響を与えたり受けたりする人や組織。 | 取り組む変化・ニーズ・解決策と、何らかの関係を持つ個人や集団。 |
| T055 | 定義 | …受け入れるために、事前に合意する具体的な条件。 | 要求や成果物について、受け入れられたと言えるために満たすべき条件。 |
| T018 | 定義 | 目標の達成に向けて、特に重要な進捗や業績を測る指標。 | 目標や戦略を実現するために設定した業務プロセスの状況を、見守るための指標。 |
| T052 | 定義 | 新しい考えや技術の実現可能性などを、限定した範囲で確かめる取り組み。 | 技術の原理や、市場にニーズがあるかを、実際に試して確かめる取り組み。 |
| T362 | 定義・注意 | プロジェクトの進め方、進捗、課題、意思決定などを支援する… | プロジェクトを進めるチームや意思決定者を支える、組織または機能。注意に「Project/Portfolio両方を指し得る」を明記 |
| P018 | 定義 | 短い期間で開発・確認・改善を繰り返し、変化を学びながら進める… | 開発する機能を短い期間（イテレーション）に区切り、各期間の終わりに動作を確認しながら進める開発の進め方。 |
| P001 | 定義 | …短い周期で成果をつくり、確認し、適応するための軽量なフレームワーク。 | 複雑な課題に対し、適応的な解決策で価値を生み出すことを助ける、軽量なフレームワーク。 |
| R004 | 定義・注意 | …個人または業務の場面で行うロボット。 | 人や設備にとって役立つ作業を行うロボット。（個人用/業務用は規格定義ではない旨を注意へ） |
| R003/R004 | 出典URL | `ifr.org/industrial-robots`, `ifr.org/service-robots`（開けず確認不能） | IFR World Robotics 2025 Service Robots PDF（ISO 8373:2021 §3.6/§3.7を引用） |
| T312 | 参照箇所 | NIST AI 100-2e2025 | NIST SP 800-218A の定義（GenAI同義語の出典がAI 100-2e2025） |
| T052 | 参照箇所 | — | 「SBIR推進プログラム公募の説明」を明記（一般定義ではなく公募文脈） |

追加（編集）：検索用の別名（別表記・略語）と「関連する言葉」。いずれも編集者による整理で、原典の主張ではありません（代表者確認項目）。

## C. 事実性監査（確認日 2026-10-29、出典ページを実際に開いて照合）
| ID | 掲載する主張 | 出典・該当箇所 | 判定 | 注意点 | 修正 |
|---|---|---|---|---|---|
| R201 | 人・組織のニーズを明らかにし、価値につながる変化や解決策を検討する活動 | IIBA BABOK用語集「business analysis」：定義によりニーズを明らかにし解決策を推奨して変化を可能にする実務 | SUPPORTED | 英語原文の編集要約 | なし |
| P037 | 対処すべき問題または機会 | IIBA「need」：A problem or opportunity to be addressed. | SUPPORTED（修正後） | 旧文の「望ましい状態」は原典になし | 修正 |
| T014 | 変化・ニーズ・解決策に関係する個人や集団 | IIBA「stakeholder」 | SUPPORTED（修正後） | 旧文の「影響を与えたり受けたり」は原典になし | 修正 |
| P038 | ニーズを検討・実装に使える形で表したもの | IIBA「requirement」：A usable representation of a need. | SUPPORTED | | なし |
| P034 | 備えるべき機能の条件 | IIBA「functional requirement」／補足：デジタル庁DS-130 p.5 | SUPPORTED | | なし |
| P035 | 性能・信頼性・セキュリティ等の品質や制約 | IIBA「non-functional requirement」／補足：DS-130 p.17 | SUPPORTED | 「機能以外」の曖昧さに注意 | なし |
| T055 | 受け入れられたと言えるために満たすべき条件 | IIBA「acceptance criteria」：…that must be met in order to achieve stakeholder acceptance | SUPPORTED（修正後） | 旧文の「事前に合意」は原典になし | 修正 |
| P040 | 関係者にとって意味や有用性があること | IIBA「value」 | SUPPORTED | 見出しは「Value」 | なし |
| T018 | 業務プロセスの状況を見守る指標 | デジタル庁DS-130 p.6–7：KGI達成のため業務プロセスをモニタリングする指標 | SUPPORTED（修正後） | 官公庁IT文脈の定義 | 修正 |
| T052 | 技術の原理や市場ニーズを実際に試して確かめる | NEDO SBIR公募ページ：技術シーズの原理確認又は市場でのニーズ確認の実証 | PARTIALLY_SUPPORTED | 公募制度内の説明。一般定義の網羅ではない。「成功＝本番OK」は原典にない主張として否定済み | 修正・文脈明記 |
| T362 | 支援する組織または機能 | PMI「Project Management Offices」：チームと意思決定者の支援構造、呼称は組織で異なる（Project 65%／Portfolio 34%の調査） | PARTIALLY_SUPPORTED | DS-130 p.17は PMO＝Portfolio Management Office、PJMO＝Project Management Office。同義扱いはCONTRADICTED（入力CSVの誤り）→訂正済み | 修正 |
| P018 | イテレーションに区切り各期間終了時に動作確認 | DS-130 p.2 | SUPPORTED（修正後） | 「計画不要」「スクラムと同義」ではない旨は注意文（編集者の整理） | 修正 |
| P001 | 複雑な課題への適応的解決で価値を生む軽量フレームワーク | Scrum Guide 2020「Scrum Definition」 | SUPPORTED | アジャイル全般と区別 | 修正 |
| T312 | 入力データの構造・特性を模して派生的な合成コンテンツを生成するAIモデルの一群 | NIST CSRC用語集（SP 800-218A） | SUPPORTED | 「正確性は保証されない」は原典要約ではなく一般的注意（編集） | 参照箇所修正 |
| T329 | データ・デジタル技術で顧客価値・事業・業務を変えること | IPA DX認定制度FAQ Q1-060（デジタルガバナンス・コード3.0引用） | SUPPORTED | 原文は長く、短縮要約 | なし |
| R001 | 現実世界を認識・判断し動作につなげるAIを指す広い呼び方 | NEDO「ロボット知っておきたい基礎知識」4章 | SUPPORTED | 単一規格・製品名ではない／完全自律・安全の保証ではない（NEDOの主張ではなく本サイトの注意）。NVIDIAページは補助で未再確認 | なし |
| R002 | 自律性を持ち移動・操作・位置決めを行うプログラムされた駆動機構 | IFR standardisation（ISO 8373の定義の引用） | SUPPORTED | 規格全文は未購読。「AI必須ではない」は定義にAIが含まれないことに基づく編集 | なし |
| R003 | 再プログラム可能で多目的なマニピュレータ（3軸以上） | IFR World Robotics Service Robots 2026 §3.6、同Industrial Robots 2022 §1.7.2 | SUPPORTED | 2012年版/2021年版で記述差あり。IFR統計は2012年版定義を使う年次あり | 出典差替・注意追記 |
| R004 | 人や設備に役立つ作業を行うロボット | 同 §3.7（原典は断片的引用） | PARTIALLY_SUPPORTED | 個人用/業務用はISO 8373:2021では定義されていない | 修正 |
| R012 | 自らの制御で移動できるロボット | IFR standardisation「Mobile robot」 | SUPPORTED | 「遠隔操作・誘導機能を持つ場合もある」は編集上の一般注意で原典未確認 → NOT_VERIFIED扱いで代表者確認 | なし |

未照合・限界：ISO 8373原文、PMBOK、DS-130のページ画像、NVIDIAページ。例文・「明日への問い」・「注意」の一部は編集者の文言で、原典の主張ではありません。

## D. 品質評価（実行したテストのみ）
実行：Playwright(Chromium)・ローカルサーバーで50件すべてPASS（`scratchpad/qa2/v08.js`）。
- 20語・ID一意・必須項目・指定ID一致・保留語の不在・トップ表示8語
- 日本語／英語／略語（PoC・PMO・KPI）／全角（ＰｏＣ）／別名（GenAI・ピーエムオー）検索
- カテゴリ別（8/5/2/5）・全件復帰・件数表示・0件案内
- 関連語リンク（遷移・フォーカス）・関連ID整合・直リンク `#t-ID`・旧 `?q=PMO` `?area=robotics`
- 出典リンク25本（https・noopener）※リンク先の生存は下記
- 見出し構造（h1は1つ）、キーボード（スキップリンク・入力・チップ・詳細開閉）
- モバイル375px（横スクロールなし・タップ領域45px）
- noindex維持、公開前モック帯、内部ステータス語の非混入（画面・JSON）、外部通信なし、コンソールエラーなし
- 回帰：`/tomorrow`・`/services` 配下36ページが200、/tomorrow配下はnoindex、内部リンク36本が解決。トップの代表者写真・氏名は変化なし。

| 項目 | 結果 |
|---|---|
| 出典URLの到達性（原典を実際に開いた） | 20語中、ifr.org/industrial-robots と /service-robots は開けず差替。他は2026-10-29に開いて確認 |
| axe／HTMLバリデータ／Lighthouse | BLOCKED（環境で実行不可） |
| 実機（iOS/Android）・スクリーンリーダー | NOT_RUN |
| PRプレビュー（Firebase）上での表示 | NOT_RUN（pushで自動生成。未確認） |
| 独立監査（別人・別モデル） | NOT_RUN |
| 法務・安全の専門家監修 | NOT_RUN |

## E. 公開前判断
**READY_FOR_HUMAN_REVIEW**。本番公開・PRマージ・noindex／モック帯の解除は未実施で、代表者の別途承認が必要です。

## 代表者への確認事項
1. 編集追加（別名・関連語・例文・「明日への問い」）の可否。
2. R012の「遠隔操作や誘導機能を持つ場合もある」を残すか（原典未確認）。
3. R004「個人用/業務用」を外した修正の可否。
4. PMOを Project Management Office として載せ、Portfolio Management Officeを注意に併記する扱い。
5. `/tomorrow` への8語入口の配置・文言、理念ページ等のリンク先変更2件。
6. 20語のうちPoC（SBIR公募の説明）は一般定義ではなく制度文脈である点の許容。

## PR #1 と PR #6 の取り込み提案（どちらも正本と断定しない）
- PR #6 は `public/index.html` のみ、PR #1 は `public/tomorrow/**` と docs。ファイル衝突なし（確認済み）。
- 提案：両方を別々にレビュー→代表者が順序を決定。PR #1 の公開時は noindex・モック帯の解除を別承認とする。
