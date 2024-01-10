
function cookietab(){
    document.getElementById("tab").innerHTML += `
    <form action="" name="cookieform">
    <input type="text" name="username" placeholder="Enter your name to create cookie">
    <input type="submit" value="Enter" onclick="createCookie()"  class="btn btn-primary">
    </form>
    `
}

function createCookie(){
    const name = escape(document.cookieform.username.value)
    document.cookie = "cookieforu="+name+":;"+"SameSite=None"
}

function ifelsestatement(){
    const ads = "Advanced Data Structre"
    var adsmark = parseInt(prompt("Enter the adsmark"))
    var osmark = parseInt(prompt("Enter the Os mark"))

    if(adsmark < osmark){
        os = "Operating Systems"
        document.write("You should have a Good mark in ,", ads," than " ,os)
    }
    else{
        document.write(os ," mark is ",osmark," and ",ads," mark is ",adsmark )
    }
}

function switchstatement(){
    function add(n,m){
        return n+m;
    }
    function sub(n,m)
        {return n-m;}

    var num1 = parseInt(prompt("Enter Num1 "))
    var num2 = parseInt(prompt("Enter Num2 "))
    const op = prompt("Enter the OPerator only '+' ,'-")
    switch(op){
        case '+':
            document.write(add(num1,num2))
        case '-':
            document.write(sub(num1,num2))
    }
}

function loops(){
    const arr = new Array(23,45,67,89,90)
    j = 0
    document.write("For Loop <br> ")
    for(i = 0;i<5;i++)
        document.write(arr[i],' ');
    document.write("<br>","While Loop <br>")
    n = parseInt(prompt("Enter the number to print the last digit and count","365463"))
    while(n > 0){
        n = Math.trunc(n/10);
        j++;
    }
    document.write("Digits:"+j)
}
