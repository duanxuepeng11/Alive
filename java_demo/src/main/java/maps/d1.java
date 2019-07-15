package maps;

import org.apache.commons.collections.map.HashedMap;

import java.util.Iterator;
import java.util.Map;

public class d1 {
    public static Map<String,Integer> maps = new HashedMap();

    public static void main(String[] args) {

        maps.put("2222",1);
        maps.put("333",1);

        String keys = "2222";

        if(maps.containsKey(keys)){
            Integer integer = maps.get(keys);
            maps.put(keys,integer+1);
        }else{
            maps.put(keys,1);
        }
//        Iterator<String> iterator = maps.keySet().iterator();
//        while (iterator.hasNext()){
//            try {
//
//
//                String key = iterator.next();
////                maps.put("aaaaa",1);
////                maps.remove("bb")
////                if(keys.equals(key)){
////                    Integer integer = maps.get(keys);
////                    maps.put("bbbbbbb",integer+1);
////                }
//            }catch (Exception e){
//                e.printStackTrace();
//            }
//
//        }
//
//
//        System.out.println("size"+maps.size());
        for(Map.Entry<String,Integer> ens : maps.entrySet()){
            System.out.println(ens.getKey()+"======"+ens.getValue());
        }
    }
}
