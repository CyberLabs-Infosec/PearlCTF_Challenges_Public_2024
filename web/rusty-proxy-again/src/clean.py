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
try_rmdir("app/api/node_modules")
try_rmdir("http_proxy/target/debug")
try_rmdir("proxy_file")

os.mkdir("source")
shutil.copytree("app", "source/app")
shutil.copytree("http_proxy", "source/http_proxy")
shutil.copy("Dockerfile", "source/Dockerfile")
shutil.copy("supervisord.conf", "source/supervisord.conf")
shutil.copy(".dockerignore", "source/.dockerignore")

try_rm("source/http_proxy/src/main.rs")
try_rm("source/http_proxy/src/parser.rs")
try_rm("source/app/api/.env")
try_rm("source.zip")

os.mkdir("source/http_proxy/target/debug")

