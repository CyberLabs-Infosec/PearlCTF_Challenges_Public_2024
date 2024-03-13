require('dotenv').config()

const express = require("express")
const app = express()

const bodyParser = require("body-parser")
app.use(bodyParser.urlencoded({ extended: false }))

const PORT = 7331
const FLAG = process.env.FLAG || "pearl{fake_flag}"

const fs = require("fs");
const { WASI } = require("wasi");
const wasi = new WASI();
const importObject = { wasi_snapshot_preview1: wasi.wasiImport };

function insertText(text, module) {
    let addr = module.exports.getBuffer()
    let buffer = module.exports.memory.buffer
 
    let mem = new Int8Array(buffer)
    let view = mem.subarray(addr, addr + text.length)
 
    for (let i = 0; i < text.length; i++) {
       view[i] = text.charCodeAt(i)
    }
 
    return addr
}

function getText(pointer, module) {
    let buffer = module.exports.memory.buffer
    let mem = new Int8Array(buffer)
    let view = mem.subarray(pointer, pointer + 1024)

    let string = ""

    for (var i = 0; i < 1024; i++) {
        if (view[i] == 0) {
            return string
        }
        string += String.fromCharCode(view[i])
    }

    return string
}

const isObject = (item) => {
    return (item && typeof item === 'object' && !Array.isArray(item));
}

(async () => {
    const wasm = await WebAssembly.compile(
        fs.readFileSync("./main.wasm")
    );
    const instance = await WebAssembly.instantiate(wasm, importObject);
    wasi.start(instance);

    let obfustaced_func1 = "RRZzDkxEUwIzDhFZC0QQCQ8cDg1xAAAAHlE6Ql4fAgt3AAAATRY5SwNQGxY2D0VJTEQwMA4cFCR5TQwKIhs1DgYNRRYEAAAAMFB5TQwKIhs1DgYNRRwEAAAAMFBgDRAXDkh3BD4SCAACRwAiBhwmNkxDAiI0DhwkUBwEAAAAMARk"
    let obfustaced_func1_addr = insertText(obfustaced_func1, instance)
    let snip0 = getText(instance.exports.getCode_1(obfustaced_func1_addr, obfustaced_func1.length), instance)

    const func1 = eval(snip0)

    let obfuscated_snip1 = "DhYxGBFZGAo6GSobB0QVOCo3Qwk+GRYcRQs6GksbAh0mRQobB1BkBwANTQ06BhUVDA06Vh4MHhwtUVRVHxYzDl9bHg0+DQNbQRg8CAAKHkMkGAALGxwtUUcXAhc6SUkdDA0+CQQKCEN9GwQLGRA+B0cEQRYtDAQXBAo+HwwWA0N9GwAYHxVxAgtbEEIQCQ8cDg1xGAANPQswHwoNFAk6JANRGRwyGwkYGRxzEBhQQQwsDhc2DxNxAhY4CRQ2BVoLCAoqBxFETyAwHkUaDBcxBBFZCRZ/Hw0YGVk3DhccTFtlQwMMAxpuQxEcAAkzChEcQQwsDhc2DxN2RxEcAAkzChEcQxAsKgEUBBd5TU0LCAoqBxFEKzUeLExQVg=="
    let obfuscated_snip1_addr = insertText(obfuscated_snip1, instance)
    let snip1 = getText(instance.exports.getCode_1(obfuscated_snip1_addr, obfuscated_snip1.length), instance)

    app.post("/verify", (req, res) => {
        try {
            result = "You are not permited to view the flag"
            eval(snip1)

            return res.status(200).send(result)
        } catch (e) {
            return res.status(500).send(e.message)
        }
    })
    
    app.listen(PORT, () => {
        console.log(`listening on ${PORT}`)
    })
})();