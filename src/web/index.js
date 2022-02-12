const api = "https://localhost:5050";

function start_bot(name) {
  (async () => {
    const rawResponse = await fetch(api + "/manage/add", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        token: "OTM5OTc0NzE4MDk2ODE4MTc2.YgAprA.nBwsdDhEmfOoEKHJLGvdmXwsDxg",
        context: "/bots/test",
        name: "test",
      }),
    });
    const content = await rawResponse;

    console.log(content);
  })();
}
