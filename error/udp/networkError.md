위치 : networking/broadcast - broadcastTx, broadcastBlock <br>
에러 메시지 : 'Remote end closed connection without response'  <br>
사실 : 
1. reception 서버는 tcp를 따름.
2. response가 오기 전에 connection이 종료된다.

추측 : reception 서버에서 response를 보내기 전에 four way handshake가 일어난다.<br>
<br>
검증 : <br>
tcpdump를 사용해 응답이 오기전에 connection이 종료되는지 확인한다.<br>
해결 방법 : broadcast 보낼 때 wait한다.<br>

보내기만 하면 되기 때문에 tcp를 쓰지 않고 udp를 쓰면 된다.<br>

 i/o시에는 스레드로 분리. udp로 바꾸는 것은 문제 직접 해결 방법은 아님, 스레드가혹은 res를 받는 코드가 res를 받기 전에 실행되는 것을 방지해야한다. 우연에 맡기지 않는 개발, request라이브러리? 자체에 문제가? 문제지점파악하기. udp로 바꾸는것동시 진행 <br>

 request.post와 socket.sendto의 차이점<br>
 request.post는 그대로 오기 전에 thread가 종료됨.<br>
 socket.sendto는 그렇지 않은 듯??<br>
 
 tcp를 사용할 경우 받는 서버에서 문제가 생기면 보내는 쪽 프로세스에도 에러 메시지가 나오지만 udp의 경우 상대 서버가 받았는지에 관심이 없기 때문에 에러가 발생하지 않는다.<br>

 블록, 트랜잭션 브로드 캐스트는 전달에만 목적이 있기 때문에 빠르고 효율적인 udp 사용해도 되는 듯<br> 