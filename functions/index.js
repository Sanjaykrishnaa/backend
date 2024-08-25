const functions = require("firebase-functions");
const express = require("express");
const app = express();
const {exec} = require("child_process");

// Run your Flask app
exec("python app.py", (err, stdout, stderr) => {
  if (err) {
    console.error(`Error: ${err.message}`);
    return;
  }
  if (stderr) {
    console.error(`Stderr: ${stderr}`);
    return;
  }
  console.log(`Stdout: ${stdout}`);
});

// Use your Flask app as an Express app
app.get("/bfhl", (req, res) => {
  res.send("Flask App is Running");
});

exports.app = functions.https.onRequest(app);
