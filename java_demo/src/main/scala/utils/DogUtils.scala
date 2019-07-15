package utils

object DogUtils {


  def main(args: Array[String]): Unit = {
    //调用隐士函数
    import impliciUtils.str2Dog
    run("333")
    import impliciUtils.dog
    rum2
  }
  def run(x:Int) =println(x)


  def rum2(implicit str:String) =println("hello :"+str)
}
