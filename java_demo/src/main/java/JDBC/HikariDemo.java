package JDBC;

import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

/**
 * hikaricp  连接池实例
 *
 *
 */
public class HikariDemo {
    public static void main(String[] args) {
        //配置文件
        HikariConfig hikariConfig = new HikariConfig();
        hikariConfig.setJdbcUrl("jdbc:mysql://localhost:3306/test");
        hikariConfig.setDriverClassName("com.mysql.jdbc.Driver");
        hikariConfig.setUsername("root");
        hikariConfig.setPassword("123456");
        hikariConfig.addDataSourceProperty("cachePrepStmts", "true");
        hikariConfig.addDataSourceProperty("prepStmtCacheSize", "250");
        hikariConfig.addDataSourceProperty("prepStmtCacheSqlLimit", "2048");

        HikariDataSource ds = new HikariDataSource(hikariConfig);
        Connection con = null;
        Statement statement = null;
        ResultSet rs = null;

        try {
           con = ds.getConnection();
           statement = con.createStatement();

            rs = statement.executeQuery("select * from s_import");

            while(rs.next()){
                String s1 = rs.getString(1);
                String s2 = rs.getString(2);
                String s3 = rs.getString(3);
                String s4 = rs.getString(4);
                String s5 = rs.getString(5);
                System.out.println(s1+"--"+s2+"--"+s3+"--"+s4+"--"+s5);
            }
            con.close();
        }catch (Exception e){
            e.printStackTrace();
        }











    }
}
