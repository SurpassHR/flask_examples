document.getElementById("button").addEventListener("click", function () {
    let text = document.getElementById("textarea").value;
    console.log(text);
});

document.getElementById("post-button").addEventListener("click", function () {
    const formData = new FormData();
    var data = document.getElementById("textarea").value;
    console.log("data[" + data + "]");
    formData.append("textarea_data", data);
    fetch("/post", {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (response.status === 200) {
            console.log("POST request succeeded");
            return response.text();
        }
        console.log("POST request failed, status code [" + response.status + "]");
        return null;
    })
    .then(data => {
        if (data === null) {
            return;
        }
        console.log("POST request success, received data [" + data + "]");
    })
});

document.getElementById("get-button").addEventListener("click", function() {
    fetch("/get", {
        method: "GET",
    })
    .then(response => {
        if (response.status === 200) {
            console.log("GET request succeeded");
            return response.text();
        }
        return null;
    })
    .then(data => {
        if (data === null) {
            return;
        }
        var dataList = JSON.parse(data);
        console.log(dataList);
        var valueList = Object.values(dataList);
        var text = "";
        for (var i = 0; i < valueList.length; i++) {
            text += valueList[i] + "\n";
        }
        document.getElementById("textarea").value = text;
    })
});

document.getElementById("shell-ping-button").addEventListener("click", function() {
    fetch("/shell_ping", {
        method: "GET",
    })
    .then(response => {
        return response.text();
    })
    .then(data => {
        var ipList = JSON.parse(data);
        var ul = document.createElement("ul");
        var cnt = 1;
        ipList.forEach(element => {
            var p = document.createElement("p");
            var button = document.createElement("button");
            button.id = "ip-" + cnt;
            button.className = "version-button";
            button.innerHTML = "Get Version";
            p.innerHTML = element;
            ul.append(p);
            ul.append(button);
            cnt++;
        });
        document.body.appendChild(ul);
    })
});
