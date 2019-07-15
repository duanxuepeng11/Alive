import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.consumer.OffsetAndMetadata;
import org.apache.kafka.common.TopicPartition;
import org.apache.kafka.common.serialization.StringDeserializer;

import java.util.Properties;
import java.util.TreeMap;

import kafka.api.PartitionOffsetRequestInfo;
import kafka.cluster.BrokerEndPoint;
import kafka.common.OffsetMetadataAndError;
import kafka.common.TopicAndPartition;
import kafka.javaapi.OffsetFetchRequest;
import kafka.javaapi.OffsetFetchResponse;
import kafka.javaapi.OffsetResponse;
import kafka.javaapi.PartitionMetadata;
import kafka.javaapi.TopicMetadata;
import kafka.javaapi.TopicMetadataRequest;
import kafka.javaapi.consumer.SimpleConsumer;
import kafka.network.BlockingChannel;

public class KafkaOffsetTools {
    private static KafkaConsumer<String, String> consumer;
    private static String topic;
    private static String group = null;
    private static SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
    private static Properties props = new Properties();

    public static void init() {
        group = "data_form_mysql-gid1";
        props.put("bootstrap.servers", "192.168.121.41:6667");
        props.put("group.id", group);
        props.put("enable.auto.commit", "true");
        props.put("auto.commit.interval.ms", "1000");
        props.put("max.poll.records", 100);
        props.put("session.timeout.ms", "30000");
        props.put("auto.offset.reset", "earliest");
        props.put("key.deserializer", StringDeserializer.class.getName());
        props.put("value.deserializer", StringDeserializer.class.getName());
        consumer = new KafkaConsumer<String, String>(props);
        topic = "axt1";
        consumer.subscribe(Arrays.asList(topic));
    }

    public static void main(String[] args) {
        init();

        String broker = props.getProperty("bootstrap.servers").split(",")[0].split(":")[0];
        System.out.println("kafka地址-----------" + broker);
        int port = 6667;
        String clientId = "Client_kafkaOffset_1";
        int correlationId = 0;
        BlockingChannel channel = new BlockingChannel(broker, port, BlockingChannel.UseDefaultBufferSize(),
                BlockingChannel.UseDefaultBufferSize(), 5000);
        channel.connect();

        List<String> seeds = new ArrayList<String>();
        seeds.add(broker);
        KafkaOffsetTools kot = new KafkaOffsetTools();

        /**
         * metadatas的 key就是分区
         * value就是分区的数据
         */
        TreeMap<Integer, PartitionMetadata> metadatas = kot.findLeader(seeds, port, topic);

        long sum = 0l;
        long sumOffset = 0l;
        long lag = 0l;
        //存放topic和分区
        List<TopicAndPartition> partitions = new ArrayList<TopicAndPartition>();
        for (Entry<Integer, PartitionMetadata> entry : metadatas.entrySet()) {
            int partition = entry.getKey();
            TopicAndPartition testPartition = new TopicAndPartition(topic, partition);
            partitions.add(testPartition);
        }
        OffsetFetchRequest fetchRequest = new OffsetFetchRequest(group, partitions, (short) 0, correlationId, clientId);
        for (Entry<Integer, PartitionMetadata> entry : metadatas.entrySet()) {
            int partition = entry.getKey();
            try {
                channel.send(fetchRequest.underlying());
                OffsetFetchResponse fetchResponse = OffsetFetchResponse.readFrom(channel.receive().payload());

                TopicAndPartition testPartition0 = new TopicAndPartition(topic, partition);
                Map<TopicAndPartition, OffsetMetadataAndError> offsets = fetchResponse.offsets();
                OffsetMetadataAndError result = offsets.get(testPartition0);
                OffsetAndMetadata committed = consumer.committed(new TopicPartition(topic, partition));
                long partitionOffset = committed.offset();
//                System.out.println("获取提交的偏移量--------" + topic + "_" + partition + ":" + partitionOffset);
                sumOffset += partitionOffset;
                String leadBroker = entry.getValue().leader().host();
                String clientName = "Client_" + topic + "_" + partition;
                SimpleConsumer consumer = new SimpleConsumer(leadBroker, port, 100000, 64 * 1024, clientName);
                long readOffset = getLastOffset(consumer, topic, partition, kafka.api.OffsetRequest.LatestTime(),
                        clientName);
// System.out.println("最近时间："+kafka.api.OffsetRequest.LatestTime());
                sum += readOffset;
                System.out.println("Topic_分区:" + topic + "_" + partition + "  "+"\t一共:"+readOffset+"\t消费:" + partitionOffset+"\t剩余:"+(readOffset-partitionOffset));

                if (consumer != null)
                    consumer.close();
            } catch (Exception e) {
                channel.disconnect();
            }
        }

        System.out.println("汇总如下:");
        System.out.println("logSize：" + sum);
        System.out.println("offset：" + sumOffset);

        lag = sum - sumOffset;
        System.out.println("lag:" + lag);

    }

    public static long getLastOffset(SimpleConsumer consumer, String topic, int partition, long whichTime,
                                     String clientName) {
        TopicAndPartition topicAndPartition = new TopicAndPartition(topic, partition);
        Map<TopicAndPartition, PartitionOffsetRequestInfo> requestInfo = new HashMap<TopicAndPartition, PartitionOffsetRequestInfo>();
        requestInfo.put(topicAndPartition, new PartitionOffsetRequestInfo(whichTime, 1));
        kafka.javaapi.OffsetRequest request = new kafka.javaapi.OffsetRequest(requestInfo,
                kafka.api.OffsetRequest.CurrentVersion(), clientName);
        OffsetResponse response = consumer.getOffsetsBefore(request);

        if (response.hasError()) {
            System.out.println(
                    "Error fetching data Offset Data the Broker. Reason: " + response.errorCode(topic, partition));
            return 0;
        }
        long[] offsets = response.offsets(topic, partition);
// System.out.println("getLastOffset------------------"+Arrays.toString(offsets));
        return offsets[0];
    }

    private TreeMap<Integer, PartitionMetadata> findLeader(List<String> a_seedBrokers, int a_port, String a_topic) {
        TreeMap<Integer, PartitionMetadata> map = new TreeMap<Integer, PartitionMetadata>();
        for (String seed : a_seedBrokers) {
            SimpleConsumer consumer = null;
            try {
                consumer = new SimpleConsumer(seed, a_port, 100000, 64 * 1024, "leaderLookup" + new Date().getTime());
                List<String> topics = Collections.singletonList(a_topic);
                TopicMetadataRequest req = new TopicMetadataRequest(topics);
                kafka.javaapi.TopicMetadataResponse resp = consumer.send(req);

                List<TopicMetadata> metaData = resp.topicsMetadata();
                for (TopicMetadata item : metaData) {

                    for (PartitionMetadata part : item.partitionsMetadata()) {
                        BrokerEndPoint leader = part.leader();
                        map.put(part.partitionId(), part);
                    }
                }
            } catch (Exception e) {
                System.out.println("Error communicating with Broker [" + seed + "] to find Leader for [" + a_topic
                        + ", ] Reason: " + e);
            } finally {
                if (consumer != null)
                    consumer.close();
            }
        }
        return map;
    }

}
