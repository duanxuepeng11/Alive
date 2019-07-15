import java.util

import kafka.utils.ZkUtils
import org.apache.kafka.common.security.JaasUtils

object kafkaJDBC2 {

  //zk
  val zk="192.168.121.41:2181" ;
  //seend
  val seed="192.168.121.41" ;
  //topic
  val TOPIC="data_form_mysql"
  //broker的地址
  val BROKER_LIST="192.168.121.41:6667,192.168.121.42:6667,192.168.121.43:6667"
  //自定义group_id
  val GROUP_ID = "data_form_mysql-gid1"

  val port=6667
  def main(args: Array[String]): Unit = {

    println(queryTopic.length)
    queryTopic.foreach(println)
  }

  // 读取kafka 所有主题
  def queryTopic():List[String]= {
    val list= new util.ArrayList()
    val zkUtils = ZkUtils.apply(kafkaJDBC2.zk, 30000, 30000, JaasUtils.isZkSecurityEnabled());
    val topics = zkUtils.getAllTopics();
    //maps.put(topics.toList(),topics.size());
    zkUtils.close()
    val dd: List[String] = topics.toList
    dd
  }

}
