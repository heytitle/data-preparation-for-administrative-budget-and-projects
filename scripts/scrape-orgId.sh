#!/bin/bash

END=392

for i in $(seq 1 $END); do
    cmd="curl 'http://www.dla.go.th/servlet/InfoServlet' -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Origin: http://www.dla.go.th' -H 'Upgrade-Insecure-Requests: 1' -H 'DNT: 1' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H 'Referer: http://www.dla.go.th/servlet/InfoServlet' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.9,th;q=0.8' -H $'Cookie: JSESSIONID=cwqXmrPylk5GS2NTqBTrgGYnQn8tMgmr1x8k3lZSyWFQd42b87z2\u211286938485; _ga=GA1.3.764317149.1559243386; _gid=GA1.3.1155693120.1559243386; _gat=1' --data '_mode=change_page&page=$i&special=N&orgCode=&orgName=&orgType=&provinceId=&amphurId=' --compressed"
    echo $i;
    eval $cmd >> "outputs/org.txt"
done