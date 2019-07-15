import java.util
import com.fasterxml.jackson.annotation.JsonProperty

import scala.beans.BeanProperty
import scala.collection.JavaConversions._

object parse {
  case class Item(@JsonProperty("bw") @BeanProperty bw: String, @JsonProperty("cdn") @BeanProperty cdn: Long, @JsonProperty("ct") @BeanProperty ct: Long)
  case class Outer(@JsonProperty("video_bandwidths") @BeanProperty items: util.ArrayList[Item])

  def main(args: Array[String]): Unit = {
    import com.fasterxml.jackson.core.JsonParser.Feature
    import com.fasterxml.jackson.databind.ObjectMapper

    val mapper = new ObjectMapper
    //解析器支持解析单引号
    mapper.configure(Feature.ALLOW_SINGLE_QUOTES, true)
    //解析器支持解析结束符
    mapper.configure(Feature.ALLOW_UNQUOTED_CONTROL_CHARS, true)

    val jsonMap = mapper.readValue("{\"video_bandwidths\":[ { \"bw\" : \"484456834\" , \"cdn\" : 0 , \"ct\" : 0} , { \"bw\" : \"160477600\" , \"cdn\" : 0 , \"ct\" : 1} , { \"bw\" : \"603954332\" , \"cdn\" : 0 , \"ct\" : 2}]}", classOf[Outer]) //转换为HashMap对象

    println(jsonMap)
    jsonMap.getItems.foreach(println)
    println(jsonMap.getItems.get(0).getBw)
    jsonMap.getItems.foreach(a=>println(a.getBw))
  }
}