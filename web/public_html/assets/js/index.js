const api = "https://localhost:5050";

function add_bot(name) {
  (async () => {
    const rawResponse = await fetch(api + "/discord/manage/add", {
      method: "PUT",
      headers: {
        Accept: "text/plain",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token: "OTM5OTc0NzE4MDk2ODE4MTc2.YgAprA.nBwsdDhEmfOoEKHJLGvdmXwsDxg",
        context: "/bots/test",
        name: "test",
      }),
    });

    rawResponse.text().then(function (text) {
      console.log(text);
    });
  })();
}

function start_bot(name) {
  (async () => {
    const rawResponse = await fetch(api + "/discord/manage/start", {
      method: "PUT",
      headers: {
        Accept: "text/plain",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: "test",
      }),
    });

    rawResponse.text().then(function (text) {
      console.log(text);
    });
  })();
}
