// fun sum(x:Int,y:Int):Int {  // 第一种方式
//     return x + y
// }
// fun vars(vararg l:Int){
//     for (i in l){
//         print(i)
//     }
// }
// fun sum2(x:Int,y:Int) = x+y // 第二种方式
// fun main(args: Array<String>) {
//     val sumLambda: (Int,Int) -> Int = {x,y -> x+y}
//     println(sum2(1,2))
//     println(sumLambda(1,2))
//     vars(1,2,3,4,5)
// }
fun main(args: Array<String>) {
    // var a:Int = 1
    // var s1 = "a is $a"
    // println(s1)
    // a = 2
    // val i:Int
    // var z :Int
    // val s2 = "${s1.replace("is","was")},but now is $a"
    // println(s2)
    // for (i in 10 downTo 1 step 2){
    //     print(i)
    // }
    //     println()
    // for (i in 1 until 4){
    //     print(i)
    // }
    // val a: Int = 1000
    // val x1: Int? = a
    // val x2: Int? = a
    // println(x1 == x2)
    // var s = "1"
    // var num: Int = s.toInt()
    // println(num)
    // var x: Int = 2
    // print(x.shl(3))


    // println(chr_to_int('2'))
    // val a = arrayOf(1,2,3)  // [1,2,3]
    // val b = Array(3,{i -> (i*2)}) // [0,2,4]
    // println(a[0])
    // println(b[1])
    // val x: IntArray = intArrayOf(1,2,3)
    // x[0] = x[1] + x[2]
    // for (i in 0..2){
    //     println(x[i])
    // }
    // var x = "HELLO WORLD"
    // println("$x 的长度为 ${x.length}")
    // print("${'$'}")

    // var a: Int = 1
    // var b: Int = 2
    // var max = if (a > b) a else b 
    // if (max in 1..3){
    //     println("在区间内")
    // }
    

    // var x: Int = 1
    // when (x){
    //     in 0..3 -> println("yes")
    //     else -> {
    //         println("wu")
    //     }
    // }
    // println(hasYes("Yesaaa"))

    // var x: Int = 2
    // when{
    //     x %2 != 0 -> println("$x 是奇数")
    //     x % 2 == 0 -> println("$x 是偶数")
    //     else -> println("nonono")
    // 
    // val arr = arrayOf(1,2,3,4)
    // for ((index,value) in arr.withIndex()){
    //     println("$index 索引上的值为$value")
    // }
    val b: (Int) -> String = {n -> n.toString()}
    println(b(1))
}
fun chr_to_int(c: Char): Int{
    if (c !in '0'..'9'){
        throw IllegalArgumentException("Out of range")
    }
    return c.toInt() - '0'.toInt()
}

fun getStringLength(obj:Any):Int?{
    if (obj is String){
        return obj.length
    }
    return null
}
fun hasYes(x:Any): Boolean{
    return when(x){
    is String -> x.startsWith("Yes")
    else -> false
}
}