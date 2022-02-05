const api = "http://localhost:5050";

window.onload = function () {
  console.log("logged in!");

  fetch(api)
    .then((data) => {
      return data.json();
    })
    .then((res) => {
      console.log(res);
    });
};
