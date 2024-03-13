require('dotenv').config()

const childProcess = require('child_process');
var jwt = require('jsonwebtoken');

const express = require("express")
const path = require("path")
const bodyParser = require("body-parser")
var cookieParser = require('cookie-parser')

const app = express()

app.use(express.static(path.join(__dirname, 'public')))
app.use(bodyParser.urlencoded({ extended: false }))
app.use(cookieParser())

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "templates/index.html"))
})

const genToken = () => {
    var token = jwt.sign({ id: 1 }, process.env.SECRET);
    return token
}

app.post("/check", (req, res) => {
    try {
        let req_body = req.body.body
        
        if (req_body == undefined) {
            return res.status(200).send("Body is not provided")
        }

        let to_req = `http://localhost:5001/resp?body=${encodeURIComponent(req_body)}`

        childProcess.spawn('node', ['./bot.js', JSON.stringify({
            url: to_req,
            token: genToken()
        })]);

        return res.status(200).send("Admin will check!")
    } catch (e) {
        console.log(e)
        return res.status(500).send("Internal Server Error")
    }
})

app.get("/flag", (req, res) => {
    let token = req.cookies.token
    try {
        var decoded = jwt.verify(token, process.env.SECRET)
        if (decoded.id != 2) {
            return res.status(200).send("You are not verified")
        }

        return res.status(200).send(process.env.FLAG)
    } catch {
        return res.status(200).send("You are not verified")
    }
})

app.listen("5000", () => {
    console.log("Server started")
})