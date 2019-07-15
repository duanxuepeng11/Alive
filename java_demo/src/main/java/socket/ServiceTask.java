package socket;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.Buffer;

import org.omg.PortableInterceptor.INACTIVE;

public class ServiceTask implements Runnable{
    private Socket socket;
    private InputStream in=null;
    private OutputStream out=null;
    public ServiceTask(Socket socket) {
        this.socket=socket;
    }
    @Override
    public void run() {

        try {
            in=socket.getInputStream();
            out=socket.getOutputStream();
            BufferedReader reader=new BufferedReader(new InputStreamReader(in));
            PrintWriter writer=new PrintWriter(out);
            String result=getdata();
            System.out.println("打印："+result);
            String message=null;
            message=reader.readLine();
            System.out.println("客户端发来消息："+message);

            writer.println(result);
            writer.flush();

        } catch (IOException e) {

            e.printStackTrace();
        }finally{
            try {
                if(out!=null)
                    out.close();
                if(in!=null)
                    in.close();
                if(socket!=null)
                    socket.close();
            } catch (Exception e2) {

            }
        }
    }
    public String getdata(){
        return "Ok";
    }

}
