import org.apache.spark.sql.SparkSession
import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD

object GraphProcessing {
  def main(args: Array[String]): Unit = {

    val spark = SparkSession.builder()
      .appName("Graph Processing with GraphX")
      .master("local[*]")
      .getOrCreate()

    val sc = spark.sparkContext
    sc.setLogLevel("WARN")

    // Create users (vertices)
    val users: RDD[(VertexId, (String, Int))] = sc.parallelize(Seq(
      (1L, ("John", 30)),
      (2L, ("Jane", 25)),
      (3L, ("Bob", 35))
    ))

    // Create relationships (edges)
    val relationships: RDD[Edge[String]] = sc.parallelize(Seq(
      Edge(1L, 2L, "follows"),
      Edge(2L, 3L, "follows"),
      Edge(1L, 3L, "friend")
    ))

    // Create graph
    val graph = Graph(users, relationships)

    println("\n=== USERS ===")
    graph.vertices.collect().foreach(println)

    println("\n=== RELATIONSHIPS ===")
    graph.edges.collect().foreach(println)

    // PageRank
    println("\n=== PAGERANK ===")
    val ranks = graph.pageRank(0.001).vertices
    ranks.collect().foreach(println)

    // Connected components
    println("\n=== CONNECTED COMPONENTS ===")
    val components = graph.connectedComponents().vertices
    components.collect().foreach(println)

    // Triangle count
    println("\n=== TRIANGLE COUNT ===")
    val triangles = graph.triangleCount().vertices
    triangles.collect().foreach(println)

    // Degrees
    println("\n=== DEGREES ===")
    graph.degrees.collect().foreach(println)

    println("\n=== IN DEGREES ===")
    graph.inDegrees.collect().foreach(println)

    println("\n=== OUT DEGREES ===")
    graph.outDegrees.collect().foreach(println)

    spark.stop()
  }
}
