package Threads;

import java.util.Date;

public class JoinTester01 implements Runnable {
    private String name;
    private int count;
    public JoinTester01(String name) {
        this.name = name;
    }

    public void run() {
        System.out.printf("%s begins: %s\n", name, new Date());

//        try {
//            Thread.sleep(1000);
//        } catch (InterruptedException e) {
//            e.printStackTrace();
//        }
        System.out.printf("%s has finished: %s\n", name, new Date());

    }

    public static void main(String[] args) throws InterruptedException {
        System.out.println("Main thread is finished111");
        Thread thread1 = new Thread(new JoinTester01("One"));
        Thread thread2 = new Thread(new JoinTester01("Two"));
        thread1.start();
        thread2.start();

//      try {
////            thread2.join();
////            thread1.join();
//      } catch (InterruptedException e) {
//          // TODO Auto-generated catch block
//          e.printStackTrace();
//      }
        Thread.sleep(3);
        System.out.println("Main thread is finished222");
    }
}
