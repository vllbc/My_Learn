import java.net.URL

class Request(val url:String){
    public fun run(): String{
        val jsonString: String = URL(url).readText()
        return jsonString
    }
}
fun main(){
    val url = "https://api.bilibili.com/x/web-interface/view?aid=85440373"

    println(Request(url).run())
}
