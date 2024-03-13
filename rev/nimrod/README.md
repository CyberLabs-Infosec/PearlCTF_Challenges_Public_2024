## Nimrod

category: `rev`

type: `static`

flag: `pearl{us3_y0ur_c4lcul4t0r_bc}`

### files

- [docker image](https://hub.docker.com/r/thealpha16/nimrod)

### Solution

Spawn a new container using the image. The home directory is encrypted and files have random strings at the start of the filenames.

Notice that there is no trace of ransomware binary in the whole filesystem since the ransomware has deleted itself after encryption. You can inspect the files to find a network capture file.
