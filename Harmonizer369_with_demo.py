# Harmonizer369_with_demo.py
#
# 対話形式のテスト機能を備えた、汎用データ調和ライブラリ。
# ユーザーは事前に用意された複数のカオスデータパターンを選択し、
# 369理論による調和の効果を視覚的に確認できる。

import time
import sys
import math

class Harmonizer369:
    """
    カオス的な数値データストリームを「369の調和原理」で安定させるクラス。
    (クラスのコードは前回のものと同じなので、ここでは変更ありません)
    """

    def __init__(self, wisdom_factor: float = 0.369):
        if not 0 < wisdom_factor < 1:
            raise ValueError("智慧因子は0と1の間の値でなければなりません。")
        self.wisdom_factor = wisdom_factor
        self.colors = { "blue": "\033[94m", "green": "\033[92m", "yellow": "\033[93m", "cyan": "\033[96m", "end": "\033[0m" }

    def _print_colored(self, text: str, color: str = "blue"):
        sys.stdout.write(self.colors.get(color, "") + text + self.colors["end"])
        sys.stdout.flush()

    def harmonize(self, data_stream: list, verbose: bool = False):
        if not hasattr(data_stream, '__iter__'):
            raise TypeError("データストリームはイテラブル（リストなど）である必要があります。")
        
        data_stream = list(data_stream)
        if len(data_stream) == 0:
            return [], None

        harmonized_stream = []
        
        if verbose: self._print_colored("--- Harmonization Process Start ---\n", "green")
        
        global_trend = sum(data_stream) / len(data_stream)
        harmonized_value = data_stream[0] * (1 - self.wisdom_factor) + global_trend * self.wisdom_factor
        harmonized_stream.append(harmonized_value)
        
        if verbose:
            self._print_colored("  [Stage 1/3] Grasping the global trend...\n", "cyan")
            self._print_colored(f"    ▶ Initial harmonized value set to: {harmonized_value:.4f}\n\n", "cyan")
            time.sleep(0.5)
            self._print_colored("  [Stage 2-3/3] Harmonizing with each data point...\n", "blue")

        for current_point in data_stream[1:]:
            harmonized_value = harmonized_value * (1 - self.wisdom_factor) + current_point * self.wisdom_factor
            harmonized_stream.append(harmonized_value)
            if verbose:
                self._print_colored(f"\r    Input {current_point: <8.2f} -> Harmonized {harmonized_value:.4f}")
                time.sleep(0.1)

        if verbose: print("\n\n✅ Harmonization Complete.\n" + "---" * 15)
        
        return harmonized_stream, harmonized_stream[-1]


def plot_ascii_graph(title: str, data: list, width: int = 50):
    """
    データ系列をシンプルなASCIIアートでコンソールにプロットする。
    """
    if not data:
        return
    
    print(f"\n--- {title} ---")
    max_val = max(data)
    min_val = min(data)
    range_val = max_val - min_val
    if range_val == 0: range_val = 1

    for val in data:
        # 0からwidthの範囲に値を正規化
        bar_len = int(((val - min_val) / range_val) * (width - 1))
        bar = '#' * bar_len
        print(f"{val:8.2f} | {bar}")
    print("-" * (width + 10))


# --- このファイルを直接実行した際の対話型デモンストレーション ---
if __name__ == '__main__':
    
    test_cases = {
        "1": {
            "name": "急騰・急落パターン (Sudden Spike)",
            "data": [10.0, 12.5, 11.0, 15.2, 80.0, 18.0, 20.5, -30.0, 25.0, 30.0]
        },
        "2": {
            "name": "高周波ノイズパターン (High-Frequency Noise)",
            "data": [50.5, 49.8, 51.2, 50.1, 49.5, 50.8, 49.2, 51.5, 50.3, 49.9]
        },
        "3": {
            "name": "トレンド変動パターン (Drifting Trend with Noise)",
            "data": [20.1, 22.3, 21.5, 24.8, 23.9, 26.2, 28.1, 25.5, 27.8, 30.2]
        }
    }

    while True:
        print("\n" + "=" * 70)
        print(" Harmonizer369 - 対話型デモンストレーション・スイート")
        print("=" * 70)
        print("どのデータパターンをテストしますか？ (終了するには 'q' を入力)")
        for key, value in test_cases.items():
            print(f"  {key}: {value['name']}")
        
        choice = input("\n選択してください: ")
        
        if choice.lower() == 'q':
            print("終了します。")
            break
            
        if choice not in test_cases:
            print("無効な選択です。もう一度お試しください。")
            continue
            
        selected_test = test_cases[choice]
        chaotic_data = selected_test["data"]
        
        print(f"\n--- {selected_test['name']} のテストを開始します ---")
        
        harmonizer = Harmonizer369()
        harmonized_data, final_value = harmonizer.harmonize(chaotic_data, verbose=False) # デモでは結果をまとめて表示
        
        # ASCIIグラフでビフォー・アフターを視覚的に表示
        plot_ascii_graph("Original Chaotic Data", chaotic_data)
        plot_ascii_graph("Harmonized Stable Data", harmonized_data)
        
        print("\n[結果の要約]")
        print(f"  最終的な安定値: {final_value:.4f}")
        print("  ▶︎ 元のデータ（左）の激しい揺れが、調和後のデータ（右）では滑らかな流れになっていることが視覚的に確認できます。")
