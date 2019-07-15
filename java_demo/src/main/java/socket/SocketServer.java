package socket;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class SocketServer {
    public static void main(String[] args) throws IOException {
        ExecutorService executor=Executors.newCachedThreadPool();
        ServerSocket server=new ServerSocket();
        server.bind(new InetSocketAddress("localhost", 8877));

        while(true){
            Socket socket=server.accept();
            new Thread((new ServiceTask(socket))).start();
        }

    }
}
