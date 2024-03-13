## Flensing

category: `forensics`

type: `static`

flag: `pearl{n0_n33d_t0_d1v3_f0r_4mb3rg1s}`

### files

- [docker image tar](src/flensing.tar)

### Solution

The given tarball is corrupted. If we try to load using docker, docker will throw an error

```sh
$ docker load < flensing.tar
f812ce174d1f: Loading layer [==================================================>]   20.6MB/20.6MB
invalid diffID for layer 0: expected "sha256:f812ce174d1f8a213068092a9454ac8ab540686daa9c844544c35f02201926da", got "sha256:87c62e9614dca0d6305794e31ee30b51b88ed4ee7757d0950dace17b16795bde"
```

Unpack the tarball to see the image details

```sh
$ 7z x flensing.tar
```

`Layers` array in `manifest.json` file and `rootfs.diff_ids` array in the config file `3d2c21d870..1f73207.json` have been shuffled. In order to get the original order of the images, we can check the `json` file of each layer.

```json
{
  "id": "29868e5a907a61fb9e36830f8b286b548bcf99f06da86dbfdb9e7b953b737b63",
  "parent": "71690523b9610df4544f77657dc279fee6deea80135619bda563e44a219b7b22",
  "created": "1970-01-01T00:00:00Z",
  "container_config": {
    "Hostname": "",
    "Domainname": "",
    "User": "",
    "AttachStdin": false,
    "AttachStdout": false,
    "AttachStderr": false,
    "Tty": false,
    "OpenStdin": false,
    "StdinOnce": false,
    "Env": null,
    "Cmd": null,
    "Image": "",
    "Volumes": null,
    "WorkingDir": "",
    "Entrypoint": null,
    "OnBuild": null,
    "Labels": null
  },
  "os": "linux"
}
```

Each layer consists of it's parent layer. Using this information, we can build back the layers in the original order.

#### CORRECTED ORDER

```
e0e0188576ac2dc737a32a6f3e085869a45e4b927c044ea176943cb05ea3141a
0a819e84c3da607fdb81126a0884fb02ba5428997d5c4aebc4cdd28d3d88f375
71690523b9610df4544f77657dc279fee6deea80135619bda563e44a219b7b22
29868e5a907a61fb9e36830f8b286b548bcf99f06da86dbfdb9e7b953b737b63
792fa78682f4ca52abd4c98523ad99961e0df3475aded443ba966a56aeaffe36
4db075971a00d2af625939c4d346d5df5e79d1ac5d15307d78fd4c5f0be4c12f
d828dd10c8d189034ff6f06d2b5cf59547f1bc1d42cdc5ef0dc23f71cf474ff9
06fa54e6f9961595001faa323c212e1f8119f0323a2a528acd4f8886d79e888e
f354e4a4f20ee98cec24a17b470863dc68a3f683d8e55558e09f1e865b3d101a
```

Now that we know the order of layers, we can correct the order of the `rootfs.diff_ids` array by calculating `SHA256` hash of `layer.tar` file in each layer.

#### CORRECTED ORDER

```json
[
    "sha256:b09314aec293bcd9a8ee5e643539437b3846f9e5e55f79e282e5f67e3026de5e",
    "sha256:5603d7de78c0158d6e9d58b2f89b40e5f66d9234f9d0562f6d9eef72ce283228",
    "sha256:759ce084675cd1a5f69b16eaa7ca766f7cbf47bb3979692b31342d8a9c3062c7",
    "sha256:8bc55253c84e88fbc55b8b54b7e32cfbf9d9b94287efa9fde82fd301eae884e7",
    "sha256:22dec06264953c506fac8d1a5557cb82088a844b514f3570bdd2a1da4c47b151",
    "sha256:e5685591bd63ae2be566e279d0dbbd8037088acd85f1a7e8560df6c84cfae364",
    "sha256:38561855cd5c98db32003aa6aa145b7b7b4b00d5833c2ee9434c75d779ba6994",
    "sha256:67d1c467dc4c11c40e73745b0255b8d46dbd2fcd5fa45e4a2c7d8790a51c0f03",
    "sha256:3884e34556ead0c4727bdfcbb696e862e044d4a3c40b1584cd31b5058d4a9493"
]
```

We can now pack the image again to a tarball and load it into docker

```sh
$ tar -cvf repaired.tar \
0a819e84c3da607fdb81126a0884fb02ba5428997d5c4aebc4cdd28d3d88f375 \
10c22bb5a80843650f239977fdac7d3e7dd4d4de6d193230b18f57a2926f7499 \
2c73d2fe16014f3dac0a3ebcc8494d0349751a84af89bbf0ae040c0dff0076ca \
3cfaf1721a0b9486cb6a85503407f0f30efbef16c2bb84c4a93368aed08aae62 \
3d2c21d870c71fc2d3df45683b8cd474523378a8c6afeb54d07bbd3771f73207.json \
7cf879368a1e46b217aa6a91ba637387c4b415bb5c8e8fb5318d58d90593a844 \
8a998b97f9d2d5b49b997dd04032ac622b8290b9c769bc315457b05516501579 \
8df4a40a182beace89fd02f4f9b53a22308456ac7edf0fa7e3b9cd54aac77451 \
bb40b94345b864344153820101388040ef1f7008efe1e0695044c95bd9ebe584 \
c80c85df6f49f88ff97e7ffa3a41bea8a014a2654efbc4414e7645342ea260f5 \
e0e0188576ac2dc737a32a6f3e085869a45e4b927c044ea176943cb05ea3141a \
manifest.json \
repositories
```

```sh
$ docker load < repaired.tar
```

we can now see the image in docker images

```sh
$ docker images flensing
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
flensing     latest    3d2c21d870c7   4 hours ago   76.1MB
```

Create a container from the given image

Run the `/app/runme.py` script to get the first part of the flag.

Now if it clicks to you why the heck is it giving the flag check out this line

```py
import Crypto
```

That is the culprit

Go over to `/usr/local/lib/python3.12/site-packages/Crypto/` and check `__init__.py`.

There are 2 arrays that are being XORed to give that half flag. If you see carefully there is one more array. That's the other half. 

There you go ✌️