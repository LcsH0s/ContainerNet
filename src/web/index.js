const api = "https://localhost:5050";

window.onload = async function () {
  console.log("logged in!");
  var myRequest = new Request(api);
  fetch(myRequest).then(function (response) {
    return response.text().then(function (text) {
      console.log(text);
    });
  });
};
