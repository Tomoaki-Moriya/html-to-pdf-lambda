import base64
import os
import tempfile
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


def lambda_handler(event, context):
    print("Start")
    # テンプレートが格納されているディレクトリを指定
    env = Environment(loader=FileSystemLoader("./"))

    # テンプレートを読み込む
    template = env.get_template("sample.html")

    # プレースホルダを置換する値を指定
    data = {"title": "レポート"}

    # テンプレートをレンダリング（プレースホルダの置換）して結果を取得
    result = template.render(data)

    print("HTML created")
    print(result)

    with tempfile.TemporaryDirectory() as tmp:
        pdf = HTML(string=result, encoding="utf-8").write_pdf()
        print("PDF created")
        print(pdf)
        if pdf:
            v = base64.b64encode(pdf)
            # vをbase64文字列にする
            print(v.decode("utf-8"))


lambda_handler(None, None)
