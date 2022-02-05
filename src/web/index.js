const api = "https://localhost:5050";

window.onload = async function () {
  console.log("logged in!");

  await fetch(api)
    .then((data) => {
      return data;
    })
    .then((res) => {
      console.log(res);
    });
};
