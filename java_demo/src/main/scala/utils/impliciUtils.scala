package utils

object impliciUtils {
  //定义隐士转换函数
  implicit def str2Dog(s:String) = s.toInt

  //定义隐士参数
  implicit val dog = "Smitch dog"
}
