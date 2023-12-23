from flask import Flask, render_template, request, make_response, redirect
import requests
import json
import time


SERVER_IP = "0.0.0.0"  # IP 地址，0.0.0.0 为所有 IP
PORT = 11451  # 端口
DEBUG = True  # 是否为调试
VERSION = "1.0"
VERSION_NUMBER = 0

app = Flask(__name__)

@app.route("/")
def root_directory():
    return redirect("/Wiki/");

@app.route("/Wiki/<path:filename_str>")
def wiki_content(filename_str):
    return render_template("Wiki_Page.html")

@app.route("/api/get_wiki")
def wiki_content_api():
    return_value = {}
    return_value["formatVersion"] = 1
    try:
        filename_str = request.args.get("path")
        with open("indexes.json", "r", encoding="utf-8") as f:
            wiki_indexes = json.load(f)
            for wiki_page in wiki_indexes:
                if filename_str == wiki_page["PageIndex"]:
                    filepath = f"pages/{wiki_page['FileName']}";
                    print(filepath)
                    with open(filepath, "r", encoding="utf-8") as fmd:
                        mdcontent = ''.join(fmd.readlines());
                        content_title = "Wiki";
                        try:
                            content_title = f"{wiki_page['Title']} - Wiki"
                        except:
                            content_title = "Wiki"
                        return_value["code"] = 0
                        return_value["data"] = {"markdown": mdcontent, "title": content_title}
                        return_value["msg"] = "OK"
                        break
                else:
                    return_value["code"] = 2
                    return_value["msg"] = "File Not Exsists"

    except:
        return_value["code"] = 1
        return_value["msg"] = "Exception"
    resp = make_response(json.dumps(return_value))
    resp.content_type = "application/json"
    return resp

@app.route("/Wiki/")
def wiki_root():
    return wiki_content("")

if __name__ == "__main__":
    app.run(SERVER_IP, port=PORT, debug=DEBUG)