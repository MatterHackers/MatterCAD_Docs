---
title: リリースノート
nav_order: 104
source_hash: 3ac9ea595f4f14d23496f8e287ff115f5a7738ff
source_lang: en
---
# MatterCAD 2.2026.8 (2026年8月13日)
[Windows ダウンロード](https://mattercontrol.appspot.com/downloads/mattercad-windows/release)

## 新機能

* **子要素を編集**
  * ベッド上またはシーンツリーでオブジェクトをダブルクリックすると、その内部に入り、構成しているパーツを編集できます — 別のウィンドウやタブは不要です
  * 減算などの操作では、元となるパーツを編集し、外に戻ると結果が再構築されます
  * シーンツリー上部のパンくずリストに完全なパスが表示されます。階層をクリックすると編集内容が 1 回分の元に戻せる操作としてまとめられ、各階層はそれぞれ独自の元に戻す履歴を保持します
  <!-- Double-click into a nested group, move a part, then click back out through the breadcrumb. ~700x450px -->
  * ![Drill In](https://www.matterhackers.com/r/qgG4VA)

* **ひとつのブーリアンツール**
  * 結合、減算、交差、減算して置換が 1 つの操作に統合され、パネル上部のアイコン行でモードを切り替えられます — 削除して適用し直す必要はありません
  * 同じ操作で 3D メッシュと 2D パスの両方を扱え、重いブーリアン処理の実行中は進捗を表示します
  * 従来の個別のブーリアンオブジェクトで保存されたデザインも、これまでどおり開けます
  <!-- Boolean property panel with the four-icon operation row, Subtract selected. ~500x400px -->
  * ![20260810 181041 paste 20260810 181041](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)


* **確実に動作するブーリアン**
  * ブーリアンは新しいネイティブエンジンで動作し、より高速で、これまで失敗していたメッシュでも成功します
  * 結合は穴のあるパーツを自動的に修復します。きれいに修復できたものは合成結果に統合され、安全に結合できないパーツは名前を付けて隣に残され、修復できなかったパーツは元のジオメトリを保持します
  * 平面カットは真の立体交差になり、結果は開いたシェルではなく水密で印刷可能になります
  * 問題のあるインポートメッシュ向けに、裏返ったジオメトリを保持とワインディング順序を修復のオプションを新設


## 改善点

* **2D パスエディター**
  * 4 つのポイントモード — シャープ、対称、アライン、フリー — を 2D エディターと 3D ビューの両方でワンクリックで適用できます
  * ミラーがライブ対称モードになりました。編集するとその場で中心を挟んで対称にミラーされ、ミラーされたペアを軸上にドラッグすると 1 点に統合されます
  * ラバーバンドでポイントをドラッグ選択し、グループとして移動、グリッドにスナップでき、Esc でドラッグをキャンセルできます
  * スムーズは、クリックして作成したポイントを通る曲線を 1 ステップでフィットさせます
  <!-- gif — Rubber-band select several points, drag them as a group, Esc to cancel. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

* **表示とナビゲーション**
  * 平面パスを選択した状態で Z を押すと、そのパスに合わせた真上からの編集ビューへアニメーション遷移します
  * サブピクセルテキストレンダリングは、ディスプレイが対応していれば自動的に有効になり、詳細設定でオン/オフを切り替えることもできます

* **モデリング**
  * 直線押し出しで、底面エッジに独自のスタイル、半径、セグメント数でベベルを付けられます
  * エディター専用オブジェクト（3D曲線、測定ツール、説明、シート）は表示されますが、エクスポートからは除外されます

## 主なバグ修正

  * 途中で失敗した保存が、成功と報告しながら置き換え先のファイルを切り詰めてしまうことがありました。保存は完全に完了してから保存先をアトミックに置き換えるようになり、同じ保護がライブラリへの保存とエクスポートにも適用されます
  * 保存に失敗した場合はデザインが未保存としてマークされるため、アプリを閉じても作業内容が黙って破棄されることはありません
  * クラウドのアイテムをディスクに保存すると、古いタブ名が残り、再起動時にタブが失われる問題を修正
  * 3MF のサブモデルが読み込み時に黙って破棄される問題と、同時に読み込んだ 3MF ファイル同士が干渉する問題を修正
  * クラッシュ、ヒストグラムフィルターの不具合、画像パーツのコピーが元と同期しない問題を修正
  * 曲線ポイントの削除時のクラッシュと、閉じたパスの継ぎ目のポイントで選択したモードが元に戻ってしまう問題を修正
  * 実行中のタスクの停止ボタンがクリック可能になり、実際にキャンセルできるようになりました

---

# MatterCAD 2.2026.5 (2026年5月8日)
[Windows ダウンロード](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMiMyt-ICwwLEgZVcGxvYWQYgIDI7IHKkwoM)

## 新機能

* **配列ツールの刷新**
  * 統合された単一の配列操作が、従来の直線配列、放射状配列、高度な配列を置き換えます
  * **線形**モード: 任意の回転と漸進的なスケールを伴って、指定方向にコピーします
  * **放射状**モード: 半径、スイープ角度、円弧または全周のパターンを設定して、中心軸まわりにコピーします
  * **変換**モード: 手動の変換、または名前付きの兄弟オブジェクトの変換を使ってコピーをステップ配置します
  * 線形の複合回転モードにより、スパイラル、扇形、らせんを自然に作成できます
  * オウムガイの殻状や等比数列的なレイアウトのためのスケールがオフセットに影響オプション
  * <!--  Screenshot showing the Array tool panel with the four mode buttons, and a radial example in the viewport -->
![20260506 162839 paste 20260506 162839](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-162839-paste-20260506-162839.jpg)

* **ライブラリのお気に入り**
  * ライブラリの任意のアイテムにスターを付けて、永続的なお気に入りフォルダーに追加できます
  * よく使うプリミティブ、ジェネレーター、保存済みパーツに 1 か所からすばやくアクセスできます
  * <!-- Screenshot of the Favorites container in the library sidebar with a few starred items -->
![20260506 083533 paste 20260506 083533](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083533-paste-20260506-083533.jpg)
![20260506 083600 paste 20260506 083600](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-083600-paste-20260506-083600.jpg)


## 改善点

* **整列**
  * 積み重ねの整列が、ドロップダウンのオプションではなく直接のモードボタンになりました
  * エッジを揃える、正確な隙間を空ける、順序立てたスタックを作るための、よりわかりやすいシンプル、オフセット、積み重ねの各モードを追加
  * ![Two objects with the Align operation settings visible](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154830-paste-20260506-154830.jpg)

* **ファイルサポート**
  * 画像ベースの操作で WEBP 画像形式をサポート
  * SVG ファイルの解析を改善し、インポートの信頼性が向上

* **信頼性**
  * 3MF ファイルの読み込み速度と信頼性を改善
  * セッション間のタブ復元を改善

## 主なバグ修正

* **ログインとクラウドライブラリへのアクセス**
  * バックエンドサーバーのアップグレードによってサインインできなくなっていた問題を修正し、ログインとクラウドライブラリへのアクセスを復旧しました。
  * クラウドアクセス時に期限切れまたは無効な資格情報が検出された場合、MatterCAD が再度のサインインを求めるようになりました。

* **シーンツリーの選択**
  * シーンツリーからオブジェクトを選ぶ際の一貫性のない選択動作を修正しました。

* **ヘルプのナビゲーション**
  * 同梱のヘルプおよびリリースドキュメントのナビゲーションの問題を修正しました。

* **ライブラリの右クリック**
  * ライブラリのツリービューでの右クリック動作を修正しました。

* **シート**
  * シートの作業中に発生する可能性があったクラッシュを修正しました。

---

# MatterCAD 2.2026.3 (2026年3月12日)
[Windows ダウンロード](https://mattercontrol.appspot.com/admin/uploads/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgMjk1aGoCwwLEgZVcGxvYWQYgIDItJywqgsM)

## 新機能

* **全く新しい Direct3D 11 レンダリングエンジン**
  * OpenGL から Direct3D 11 への完全移行により、パフォーマンスが劇的に向上
  * くっきりときれいなエッジのための FXAA アンチエイリアス
  * 順序に依存しない正しい透明表示のためのデュアルデプスピーリング
  * ハードウェアアクセラレーションによるベッドの影
  * オブジェクトのアウトラインと選択の表示を改善
  * ![Screenshot of a design with one object set to 50% transparency, showing objects behind it](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC80NGNmZGZlOC02NGI1LTRiZTEtYjE4Ni0wYTRhZjkxYWQxYzQ)

* **オブジェクトの透明度**
  * シーン内の個々のオブジェクトにアルファ/透明度を設定できます
  * 面ごとに色を持つメッシュでも、色を損なわずにアルファをサポート
  * ![Show rotating a scene with multiple transparent objects and bed shadows](https://img.matterhackers.com/g/Z3M6Ly9taC1pcHMtcHJvZC9jbXMtcHJvZC9iNjNhOWMxNy00MzE0LTQ0ZmUtOGFjZS1kMWVlMTdkMzEzMDE)
  
* **オブジェクトのロックと非表示**
  * オブジェクトをロックして、誤った選択や編集を防止
  * オブジェクトを非表示にして、特定のパーツの作業中の視覚的な煩雑さを軽減
  * 表示をすばやく元に戻すための、すべて再表示およびすべてロック解除コマンド
  * ロックされたオブジェクトと非表示のオブジェクトは、レイベースの選択から正しく除外されます
  * ![Show locking an object (clicking lock icon), then trying to select it, then using Unlock All](https://www.matterhackers.com/r/g4j2gw)

* **ブーリアン減算の改善**
  * 複数減算の操作が大幅に信頼性・精度ともに向上

## 改善点

* **ファイル処理**
  * プロジェクトは STL ではなく既定で 3MF として保存され、色、マテリアル、デザイン履歴が保持されます
  * 3D ビューへのファイルおよびフォルダーのドラッグ＆ドロップのサポートを強化

* **ワークフロー**
  * 名前を付けて保存と移動のダイアログが、最後に使ったフォルダーの場所を記憶します
  * 数式フィールドが `pi`、`tau`、`e`、`count` をサポート
  * デザイン編集中は Esc キーで元に戻すを実行
  * マウスがシーンから離れても 3D コントロールが表示されたままになります

* **パフォーマンスと安定性**
  * 起動時のクラッシュと再帰的な読み込みの問題を修正
  * ライティングとミップマッピングのレンダリング不具合を修正
  * ライブラリのツリービューの更新を改善
  * ズーム動作を改善する動的なニア/ファークリップ面の計算
  * .NET 10 へアップグレード

---

# MatterCAD 2.2025.6 (2025年6月20日)
[Windows ダウンロード](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIjH1paxCAwLEgZVcGxvYWQYgICIj46vnwsM)

## 新機能

* **SVG ファイルのサポート**  
  * SVG ファイルのドラッグ＆ドロップに完全対応
  * SVG グラフィックスから 3D オブジェクトへの直接変換
  * 既存の CAD ワークフローとのシームレスな統合

* **高度な OBJ ファイル処理**  
  * ZIP アーカイブからのマテリアル読み込みをサポート
  * OBJ ファイルの解析とマテリアル処理を強化
  * 複数マテリアルを含む複雑な 3D モデルへの対応を改善

* **強化されたタブ管理システム**
  * クラウドライブラリのタブが正しく保持され、作業内容は中断したところにそのまま残ります
  * タブの整理とナビゲーションを改善
  * セッション間で開いていたタブを自動的に復元

## ユーザーエクスペリエンスの向上

* **洗練されたインターフェース**
  * すばやくアクセスできるよう、最近使った項目メニューを再編成
  * 長時間の処理中の視覚的フィードバックを改善
  * アプリケーションの起動時間と応答性を改善

* **信頼性**
  * 3D シーン操作における重大なクラッシュを修正
  * メモリ管理の問題を解決
  * すべてのプラットフォームでアプリケーションの安定性を向上

---

# MatterCAD 2.21.5 (2025年2月13日)

[Windows ダウンロード](https://mattercontrol.appspot.com/downloads/development/ag9zfm1hdHRlcmNvbnRyb2xyQQsSB1Byb2plY3QYgICI5uHFqwoMCxINUHVibGljUmVsZWFzZRiAgIiHsuvhCgwLEgZVcGxvYWQYgICIh-O2lgsM)

# 既存の機能

*以下の機能は、MatterControl から受け継いだ MatterCAD の基盤となるものです:*

* 中空フィーチャーを追加  
 ![Hollow Example](https://lh3.googleusercontent.com/-ImcYYK1I3P7tvxJXLRYDitBkc2xfXD0mElN3tiX8mZk1-Qe0Gxm5TtXXzC-Er756XajqOPpu7HFEuflNCnbZZqEzg=w220) ![Hollow Menu](https://lh3.googleusercontent.com/JiCUdiJx0eboPJk2cQH3dMOvlrFsFcz7OK-v9nG3G8ztDDHovXw--xaDsN8-HbFhFfAz5jSFKHUNQwnee5WXRNApH2M=w120)
* ポリゴン縮小を追加  
![Reduce Options](https://lh3.googleusercontent.com/h6opzhbdA352u9JFtIcqPnrnJC4JjcoVehdFstGZHe1gu7qiupQ8KAYrngTORjSyUerGlxhX48sGHLlwF2AoPjG0ifw=w220) ![Reduce Menu](https://lh3.googleusercontent.com/Pw2RYm45dFljKfmAq65378bpwULWxH857_Gz_SB95JLsmQYF3YmhOJ-XFEtWqWcFcK4weNLmz2hnVggk_85jWFDE=w120) 
* メッシュ修復を追加  
 ![Repair Options](https://lh3.googleusercontent.com/C-fT1jQ-z1oOU1uBzWNLCN2IsAGOGAmJdhmUKqQLhC3p9_WdeKFDNKSoTGb4U8RRDdYk2ZRbWJ2FbjfNKzo6ii6v=w220) ![Repair Menu](https://lh3.googleusercontent.com/uQ8uaWvzremfTd7jkSu7OhKURHfvyEAFtbT1_KaTL1wgSrSUOjjQ0tm1a6uROpe6JZwC50HvdB4bJcGq8XqGAUMwmg=w120) 
* 新しい手動サポートオプションに加えて、完全自動サポート（レガシーサポート）をオプションとして搭載
* gsSlicer のサポートを追加（実験的な新しいスライスエンジン）
* バグを修正

## 変更点

* メッシュのグループ解除（複数メッシュへの分割）を改善
    * 退化した面を破棄
    * 微細な離散フィーチャーを破棄

## 変更点

* アプリケーションに検索バーを追加
    * ![Search](https://lh3.googleusercontent.com/pAN6dqaGJJZs0cVZZDtkY40IlLXeoHNFmoovzivkGdhzCwN65wuqQdYvguoVo7SewCNl33mbLMd__OVw6BJhhV1n)
* デザインツールバーを改善
    * 一部の項目にグループ化を追加
    * デュアル整列ボタンを追加
    * すべて整列ボタンを追加
* 矢印キーでベッド上の項目を微移動
* ダウンロードフォルダーを日付順に並べ替え

## 変更点

* UI の改善
    * クラウドライブラリのフォルダーの更新を高速化
    * 再度開いたときに UI を復元
    * キーボードナビゲーションのサポートを改善
* 新しいエラー検出および警告システム
    * より多くのハードウェアエラーに対応
* デザインツールの改善と最適化
    * 新しいツイストツール 
    * 曲線ツールを改善
    * 整列を改善


## 変更点

* フラット化を改善
* 元に戻す機能のサポートを改善
* デザイン履歴を改善

## 変更点
* バージョン管理: (バージョン).(年).(月) のバージョン番号へ移行。読みやすく、より多くの情報が得られます。
* 最先端の減算、結合、交差部を新搭載（Windows のみ）
* 新規ユーザーが操作に慣れられるよう、起動時に「機能ツアー」を表示するようになりました

## 変更点
* デザインツール - 完全なモデリングプリミティブ一式で 3D モデリングが可能に
* プリミティブを使って独自のカスタムサポートを作成
* デザインアプリ - デザインアプリ: 高度にカスタマイズ可能なデザイン
* 64 ビット処理
