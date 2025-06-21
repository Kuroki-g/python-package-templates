# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///

# pipによるライブラリの追加をしていない場合には、相対パスでインポートする。補完が得られない。
import sys
from pathlib import Path
# 1. このスクリプト(main.py)があるディレクトリの絶対パスを取得
script_dir = Path(__file__).resolve().parent
# 2. 2つ上の階層のディレクトリ(custom/)のパスを取得
root_dir = script_dir.parent.parent
# 3. Pythonのモジュール検索パスにroot_dirを追加
sys.path.append(str(root_dir))

from minimum import minimum

def main() -> None:
    minimum.say_hello()

if __name__ == "__main__":
    main()
