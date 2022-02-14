const api = "https://localhost:5050";

function start_bot(name) {
  (async () => {
    const rawResponse1 = await fetch(api + "/discord/manage/add", {
      method: "POST",
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
    const rawResponse2 = await fetch(api + "/discord/manage/start", {
      method: "POST",
      headers: {
        Accept: "text/plain",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: "test",
      }),
    });
    rawResponse1.text().then(function (text) {
      console.log(text);
    });
    rawResponse2.text().then(function (text) {
      console.log(text);
    });
  })();
}
