package socket;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class SocketClient {
    private static Socket socket =null;
    private static InputStream in =null;
    private static OutputStream out=null;

    public static void main(String[] args) {
        try {
            socket=new Socket("localhost",8877);
            in =socket.getInputStream();
            out=socket.getOutputStream();
            BufferedWriter writer=new BufferedWriter(new OutputStreamWriter(out));
            BufferedReader reader=new BufferedReader(new InputStreamReader(in));
            writer.write("hello\n");
            writer.flush();
            String message=null;
            while((message=reader.readLine())!=null){
                System.out.println(message);
            }
        } catch (UnknownHostException e) {

            e.printStackTrace();
        } catch (IOException e) {

            e.printStackTrace();
        }
    }
}
