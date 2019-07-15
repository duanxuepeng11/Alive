package Threads;

public class NoVisibility{
    private static volatile boolean ready;
    private static  int number;

    private static class Reader extends Thread{
        public void run(){
            while(!ready){
                Thread.yield();
            }
            System.out.println(number);
        }
    }
    public static void main(String[] args) throws InterruptedException {
        Reader r1 = new Reader();
        r1.start();
       // r1.join();
        System.out.println("aaa");
        number = 42;
        Thread.sleep(1000);
        ready = true;
        number = 43;
        System.out.println("bbb");
    }
}
