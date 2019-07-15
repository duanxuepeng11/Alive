package JDBC;

import javax.swing.table.TableRowSorter;
import java.sql.*;

import java.util.ResourceBundle;

public class DBUtils {

    // 数据库连接地址
    public static String URL;
    // 用户名
    public static String USERNAME;
    // 密码
    public static String PASSWORD;
    // mysql的驱动类
    public static String DRIVER;

    private static ResourceBundle rb = ResourceBundle.getBundle("db-config");

    private DBUtils() {
    }

    // 使用静态块加载驱动程序
    static {
        URL = rb.getString("jdbc.url");
        USERNAME = rb.getString("jdbc.username");
        PASSWORD = rb.getString("jdbc.password");
        DRIVER = rb.getString("jdbc.driver");
        try {
            Class.forName(DRIVER);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    // 定义一个获取数据库连接的方法
    public static Connection getConnection() {
        Connection conn = null;
        try {
            conn = DriverManager.getConnection(URL, USERNAME, PASSWORD);
        } catch (SQLException e) {
            e.printStackTrace();
            System.out.println("获取连接失败");
        }
        return conn;
    }

    // 关闭数据库连接
    public static void close(ResultSet rs, Statement stat, Connection conn) {
        try {
            if (rs != null)
                rs.close();
            if (stat != null)
                stat.close();
            if (conn != null)
                conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public static void close( Statement stat, Connection conn) {
        try {
            if (stat != null)
                stat.close();
            if (conn != null)
                conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Connection connection = DBUtils.getConnection();
        Connection connection1 = DBUtils.getConnection();
        Connection connection2 = DBUtils.getConnection();
        Connection connection3 = DBUtils.getConnection();
        Connection connection4 = DBUtils.getConnection();
        Connection connection5 = DBUtils.getConnection();
        Connection connection6 = DBUtils.getConnection();
        Connection connection7 = DBUtils.getConnection();
        Thread.sleep(10033300);
    }
}
