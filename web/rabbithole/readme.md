# Writeup - Web / Rabbithole

The link to the website takes us to a webpage that shows:
> You're on your own :)

Going to `/robots.txt` gives us the following:
![/robots.txt](robots.png)

So we move to the `w0rk_h4rd` directory. This has the following: 
![/w0rk_h4rd](work_hard.png)

There's two pieces of information here. The first one is `hardworking`. This is another directory you need to visit. The second text that stands out is:
> <span style="color: #CFB225;">s3cr3t1v3_m3th0d</span>

The text points towards HTTP methods, which in turn reveals that sometimescustom methods can be used to access a webpage. `s3cr3t1v3_m3th0d` is one such custom method.

I used Burp Suite to modify the http requests being sent. Replace the `GET` method by `s3cr3t1v3_m3th0d`, and send the request to `/hardworking` (any other method will return the error <span style="color: #3399ff;">`Method not allowed`</span>).
![changing method in Burp Suite](burp_method.png)

Sadly, the flag still doesn't appear. The response now is:
![not privileged](not_privileged.png)

Notice that the HTTP request contains a cookie **`userID`**, with the value `guest`. Try changing the values to `admin` or `administrator`. You'll se that `userID=admin` works.
![final Burp request](burp_request.png)

Finally, the flag appears. The response webpage is:
![flag webpage](flag.png)

The flag is:
> <span style="color: #CFB225;">**pearl{c0ngr4t5_but_th1s_1s_just_th3_b3g1nn1ng}**</span>