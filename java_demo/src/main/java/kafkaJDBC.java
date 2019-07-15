import kafka.admin.AdminUtils;
import kafka.admin.RackAwareMode;
import kafka.utils.ZkUtils;

import java.util.*;
import java.util.stream.Collectors;

import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.TopicPartition;
import org.apache.kafka.common.security.JaasUtils;


import scala.collection.JavaConversions;

public class kafkaJDBC {

    //zk
    public static final String zk="192.168.121.41:2181" ;
    //seend
    public static final String seed="192.168.121.41" ;
    //topic
    public static final String TOPIC="axt1" ;
    //broker的地址
    public static  final  String BROKER_LIST="192.168.121.41:6667,192.168.121.42:6667,192.168.121.43:6667";
    //自定义group_id
    public static  final  String GROUP_ID = "data_form_mysql-gid1";

    public static final  int port=6667;
    // 读取kafka 所有主题
    private static List<String> queryTopic() {
        ZkUtils zkUtils = ZkUtils.apply(kafkaJDBC.zk, 30000, 30000, JaasUtils.isZkSecurityEnabled());
        List<String> list = (List<String>)JavaConversions.seqAsJavaList(zkUtils.getAllTopics());
        zkUtils.close();
        return list;
    }

    //创建kafka 主题
    public static void createTopic(String topicName,int partitions,int replications){
        ZkUtils zkUtils = ZkUtils.apply(kafkaJDBC.zk, 30000, 30000, JaasUtils.isZkSecurityEnabled());
        // 创建一个单分区单副本名为t1的topic
        AdminUtils.createTopic(zkUtils, topicName, partitions, replications, new Properties(), RackAwareMode.Enforced$.MODULE$);
        zkUtils.close();
    }
    //删除 topic
    public static void deleteTopic(String topicName){
            ZkUtils  zkUtils = ZkUtils.apply(kafkaJDBC.zk,30000,
                    30000,JaasUtils.isZkSecurityEnabled());
            AdminUtils.deleteTopic(zkUtils,topicName);
                zkUtils.close();
    }

    //获取某个topic下总数据大小
    public static long totalMessageCount(String topic, String brokerList) {
        Properties props = new Properties();
        props.put("bootstrap.servers", brokerList);
//        props.put("group.id", "data_form_mysql-gid1");
        props.put("enable.auto.commit", "false");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

        try (KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props)) {
            List<TopicPartition> tps = Optional.ofNullable(consumer.partitionsFor(topic))
                    .orElse(Collections.emptyList())
                    .stream()
                    .map(info -> new TopicPartition(info.topic(), info.partition()))
                    .collect(Collectors.toList());
            Map<TopicPartition, Long> beginOffsets = consumer.beginningOffsets(tps);
            Map<TopicPartition, Long> endOffsets = consumer.endOffsets(tps);
            return tps.stream().mapToLong(tp -> endOffsets.get(tp) - beginOffsets.get(tp)).sum();
        }
    }

    /**
     * 得到所有topic的配置信息
     kafka-configs.sh --zookeeper localhost:2181 --entity-type topics --describe
     */
    public static void listTopicAllConfig(){
        ZkUtils zkUtils = null;
        try {
            zkUtils = ZkUtils.apply(kafkaJDBC.zk,30000,30000,JaasUtils.isZkSecurityEnabled());
            Map<String,Properties> configs = (Map<String,Properties>)JavaConversions.mapAsJavaMap(AdminUtils.fetchAllTopicConfigs(zkUtils));
            for (Map.Entry<String,Properties> entry :  configs.entrySet()){
                System.out.println("key="+entry.getKey()+" ;value= "+entry.getValue());
            }
        }catch (Exception e){
            e.printStackTrace();
        }finally {
            if (zkUtils!=null){
                zkUtils.close();
            }
        }
    }

    public static void main(String[] args) {

        //创建kafka
        // createTopic("a1",1,1);
        //删除kafka topic
        //deleteTopic("a1");
        //查看
//        System.out.println(kafkaJDBC.queryTopic().size());
//        System.out.println(kafkaJDBC.queryTopic().toString());
        //获取某个topic下面的数据量
        long dd = totalMessageCount(kafkaJDBC.TOPIC, kafkaJDBC.BROKER_LIST);
        System.out.println(kafkaJDBC.TOPIC+" topic下一共有"+dd+"数据");
        //  kafkaJDBC.listTopicAllConfig();
    }
}
