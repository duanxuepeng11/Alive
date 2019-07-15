package Fanxing;


import com.google.common.base.Supplier;

public class Test02 {

    public static void main(String[] args) {
        Student st1 = new Student("张三");
        fn1(st1);
    }

    public static <T extends Student> void fn1(T t){
        Runnable getName = t::getName;
        String name = t.getName();
        System.out.println(getName.toString());
//        t::setName("aaa");
    }
}
class Student{
    public String name;

    public Student(String name){
        this.name = name;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

