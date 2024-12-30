package utils

import scala.io.Source
import scala.util.{Try, Using}

object FileReader {
def readFile(fileName: String): Try[String] = {
  val resourcePath = s"$fileName"
  println(s"Attempting to read resource at: $resourcePath") // Debug log
  Using(getClass.getResourceAsStream(resourcePath)) { stream =>
    if (stream == null) {
      throw new IllegalArgumentException(s"File not found: $resourcePath")
    }
    Source.fromInputStream(stream).mkString
  }
 }
}
