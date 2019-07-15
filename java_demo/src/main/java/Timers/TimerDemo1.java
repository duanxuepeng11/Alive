package Timers;

import org.spark_project.jetty.util.thread.TimerScheduler;

import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

public class TimerDemo1 {

    static class Helper extends TimerTask
    {
        public static int i = 0;
        public void run()
        {
            System.out.println("Timer ran " + ++i);
        }
    }
    public static void main(String[] args) {

        Timer timer = new Timer();
        TimerTask task = new TimerTask(){
            @Override
            public void run() {
                System.out.println("hello");
            }
        };

        timer.schedule (task, 1000L,1000L);
    }
}
