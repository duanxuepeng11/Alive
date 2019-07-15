package Threads;

public class innerThread {

    public void startRun(){
        new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i=0;i<10;i++){
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println("aaaa");
                }

            }
        }).start();
    }
    public static void main(String[] args) {
        System.out.println("start run");
        new innerThread().startRun();
        System.out.println("end run");
    }
}
