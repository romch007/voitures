const socket = io();
const cars = new Map();

const carList = document.getElementById("car-list");

const formatData = (clientId, data) => clientId + ": " + JSON.stringify(data);

socket.on("update", (data) => {
  const clientId = data["client_id"];
  delete data["client_id"];

  if (cars.has(clientId)) {
    cars.get(clientId).textContent = formatData(clientId, data);
  } else {
    const newEntry = document.createElement("li");
    newEntry.textContent = formatData(clientId, data);
    cars.set(clientId, newEntry);
    carList.appendChild(newEntry);
  }
});
