import shutil, os

def try_rmdir(path):
    try:
       shutil.rmtree(path)
    except:
        pass

def try_rm(file):
    try:
       os.remove(file)
    except:
        pass

try_rmdir("source")
try_rmdir("app/node_modules")
try_rm("source.zip")

os.mkdir("source")
shutil.copy("./app/main.js", "./source/main.js")
shutil.copy("./app/main.wasm", "./source/main.wasm")
shutil.copy("./html/.htaccess", "./source/.htaccess")