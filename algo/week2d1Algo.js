var arr =["a","c","a","A"]

function call (arr){
    var obj={}
    for (var i = 0; i < arr.length; i++) {
        if (obj.hasOwnProperty(arr[i])){
            obj[arr[i]]++
        }
        else{
            obj[arr[i]]=1
                }
    }
    return obj
}

console.log(call(arr))

// how to do a fonction array



