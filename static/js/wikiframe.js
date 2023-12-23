function convert_markdown(markdown) {
    return marked.parse(markdown);
}

function display_markdown(markdown) {
    let elem = document.getElementById('wiki-elem');
    elem.innerHTML = convert_markdown(markdown);
}

function request_markdown(path) {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "/api/get_wiki?path=" + path)
    xhr.send(null);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let resp = JSON.parse(xhr.responseText);
            if (resp.code == 0) {
                document.title = resp.data.title;
                display_markdown(resp.data.markdown);
            } else {
                document.title = "无法显示页面 - Wiki";
                display_markdown("# 页面不存在或出现错误");
            }
        }
    };
}

function main() {
    hljs.initHighlightingOnLoad();
    let href = location.pathname // href = /Wiki/<Path>
    href = href.substring(5); // href = /<Path>
    request_markdown(href);
}

main();