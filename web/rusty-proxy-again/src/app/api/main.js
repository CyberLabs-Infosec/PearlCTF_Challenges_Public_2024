require('dotenv').config()

const express = require("express")
const app = express()

var bodyParser = require('body-parser')
var path = require("path")

const FLAG = process.env.FLAG || "pearl{fake_flag}"

app.use("/global.css", express.static(path.join(__dirname, "../client/global.css")))

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "../client", "index.html"))
})

app.post("/show", bodyParser.urlencoded({ extended: false }), (req, res) => {
    return res.status(200).json({status: "ok", body: req.body.name});
})

app.get("/show", (req, res) => {
    res.sendFile(path.join(__dirname, "../client", "show.html"))
})

app.post("/flag", bodyParser.urlencoded({ extended: false }), async (req, res) => {
    await fetch(req.body.to_req, {
        method: "GET",
        headers: {
            Flag: FLAG
        }
    })
    return res.status(200).send("OK")
})

app.all("/no_flag_banner", (req, res) => {
    return res.status(200).send("No flag for you!!")
})

app.listen(5000, () => {
    console.log("Started...");
})