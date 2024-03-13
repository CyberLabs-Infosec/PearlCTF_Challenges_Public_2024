# Noob Hacker #
Analyzing the comment section of the video, we can see that three people are having a conversation. By checking all of their usernames, we can find a GitHub account belonging to shenoyharry. We have been asked for the email of the attacker. So, by analyzing the repositories, we can see that two repos stand out: "Coool" and "PGP". "Coool" has around 5 commits, and "PGP" has a public key. Decoding that key from Base64, we get the email as shenoyharry@proton.me.

So, the flag is pearl{shenoyharry@proton.me}.
