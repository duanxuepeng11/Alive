import com.alibaba.fastjson.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class createJson {

    public static JSONObject StringCreateJson(){
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("request_ip","172.18.141.89");
        jsonObject.put("server_time","2019-06-1016:25:22");

        //粉丝是个数组,其实就是嵌套json
        JSONObject jsonObject1 = new JSONObject();
        jsonObject1.put("name","小王2");
        jsonObject1.put("age",7);


        //从此处可以看出其实list和json也是互相转换的
        List<JSONObject> jsonObjects = new ArrayList<JSONObject>();
        jsonObjects.add(jsonObject1);
        jsonObject.put("fans",jsonObject1);

//        System.out.println("jsonObject直接创建json:" + jsonObject);
        return jsonObject;
    }

    public static void main(String[] args) {
        System.out.println(createJson.StringCreateJson().toString());
        System.out.println(createJson.StringCreateJson().toJSONString());
    }
}
