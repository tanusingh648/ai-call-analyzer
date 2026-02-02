let callActive = true;
let seconds = 0;
let risk = 10;
let aiInterval = null;
let recognition = null;

/* ELEMENTS */
const duration = document.getElementById("duration");
const riskValue = document.getElementById("riskValue");
const riskText = document.getElementById("riskText");
const riskCircle = document.getElementById("riskCircle");
const alertBar = document.getElementById("alertBar");
const keywordList = document.getElementById("keywordList");
const behaviorList = document.getElementById("behaviorList");
const historyTable = document.getElementById("historyTable");


/* ---------------- TIMER ---------------- */

setInterval(() => {
  seconds++;
  const m = String(Math.floor(seconds / 60)).padStart(2, "0");
  const s = String(seconds % 60).padStart(2, "0");
  duration.textContent = `${m}:${s}`;
}, 1000);


/* ---------------- RISK UI ---------------- */

function updateRisk() {
  riskValue.textContent = risk + "%";

  if (risk < 40) {
    riskText.textContent = "LOW RISK";
    riskText.style.color = "#00ff9d";
    riskCircle.style.borderColor = "#00ff9d";
  } 
  else if (risk < 70) {
    riskText.textContent = "SUSPICIOUS";
    riskText.style.color = "#ffb300";
    riskCircle.style.borderColor = "#ffb300";
  } 
  else {
    riskText.textContent = "HIGH RISK";
    riskText.style.color = "#ff3b3b";
    riskCircle.style.borderColor = "#ff3b3b";
    alertBar.style.display = "flex";
  }
}


/* ---------------- LIVE CALL ---------------- */

async function startLiveAnalysis() {
  try {
    const res = await fetch("http://127.0.0.1:8000/live-call");
    const data = await res.json();

    document.getElementById("callText").value = data.text;

    risk = data.risk;
    updateRisk();
  } catch {
    console.log("Backend not reachable");
  }
}

// run every 3 sec
aiInterval = setInterval(() => {
  if (!callActive) return;
  startLiveAnalysis();
}, 3000);


/* ---------------- ML ANALYZE ---------------- */

async function sendToML(text) {

  const res = await fetch("http://127.0.0.1:8000/ml-analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json"},
    body: JSON.stringify({ text })
  });

  const data = await res.json();

  risk = data.risk;
  updateRisk();

  // show keyword
  const li = document.createElement("li");
  li.textContent = text;
  keywordList.appendChild(li);

  if (data.prediction === "FRAUD") {
    alertBar.style.display = "flex";
  }
}


/* ---------------- MIC ---------------- */

function startMicAnalysis() {

  if (!("webkitSpeechRecognition" in window)) {
    alert("Use Chrome for mic feature");
    return;
  }

  recognition = new webkitSpeechRecognition();
  recognition.lang = "en-IN";

  recognition.onresult = (event) => {

    const transcript = event.results[0][0].transcript;

    document.getElementById("callText").value = transcript;

    sendToML(transcript);
  };

  recognition.start();
}


/* ---------------- HISTORY ---------------- */

function saveHistory(action) {

  const row = document.createElement("tr");

  row.innerHTML = `
    <td>${new Date().toLocaleTimeString()}</td>
    <td>Unknown</td>
    <td>${risk}%</td>
    <td>${action}</td>
  `;

  historyTable.appendChild(row);
}


/* ---------------- CALL ACTIONS ---------------- */

function endCall() {
  callActive = false;
  clearInterval(aiInterval);
  saveHistory("Ended");
}

function blockCall() {
  endCall();
  alert("🚫 Number Blocked");
}

function reportCall() {
  endCall();
  alert("📢 Fraud Reported");
}


/* ---------------- SETTINGS ---------------- */

function openSettings() {
  document.getElementById("settingsModal").style.display = "block";
}

function closeSettings() {
  document.getElementById("settingsModal").style.display = "none";
}
async function sendAudio() {
   console.log("sendAudio triggered");
}
