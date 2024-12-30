import utils.FileReader

object HelloWorld {
 def main(args: Array[String]): Unit = {
   println("Hello Scala!")

   val resource = getClass.getResource("/aocday1.txt")
   println(s"Resource URL: $resource")
   val result = FileReader.readFile("aocday1.txt")

   result match {
     case scala.util.Success(content) => println(s"File content:\n$content")
     case scala.util.Failure(exception) => println(s"Error: ${exception.getMessage}")
   }

 }
}
