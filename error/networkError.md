위치 : networking/broadcast - broadcastTx, broadcastBlock <br>
에러 메시지 : 'Remote end closed connection without response'  <br>
사실 : 
1. reception 서버는 tcp를 따름.
2. response가 오기 전에 connection이 종료된다.

추측 : reception 서버에서 response를 보내기 전에 four way handshake가 일어난다.<br>
<br>
검증 : <br>
tcpdump를 사용해 응답이 오기전에 connection이 종료되는지 확인한다.
해결 방법 : broadcast 보낼 때 wait한다.