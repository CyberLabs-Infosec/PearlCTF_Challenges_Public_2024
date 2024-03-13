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
        <?php
            $password = "y0u_c4n't_gue5s_th1s_right?";
            extract($_GET); // get request to "input" arg
            if ($input == $password) {
                if ($input != "PearlCTF_15345384" && md5($input) == md5("PearlCTF_15345384")) {
                    echo "head to /u_c4nt_gu355_th1s to get flag\n";
                } else {
                    echo "md5 didn't match\n";
                }
            } else {
                echo "Wrong password!\n";
            }
        ?>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>
</body>
</html>