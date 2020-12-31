<html>
    <head>
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Andika+New+Basic:ital,wght@1,700&display=swap" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Jura:wght@700&display=swap" rel="stylesheet">
        <link rel = "icon" href =  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrp5Ebp4TQICmdFEgq5jUpWVFsNQif9d5BGg&usqp=CAU" type = "image/x-icon"> 
        <title>GCD of Two Numbers</title>
    </head>
    <style>

        body {
            background-color: #000;
            font-family: 'Jura', sans-serif;
        }

        input[type=number]{
            width: 20%;
            border: 2px solid #aaa;
            border-radius: 10px;
            margin: 8px 0;
            outline: none;
            padding: 12px;
            box-sizing: border-box;
            transition: 5px;
            opacity: 100;
            font-family: 'Jura', sans-serif;
        }
        
        input[type=text]:focus{
            border-color: #0bbcf1;
            box-shadow: 0 0 30px 0 #0bbcf1;
        }

        input:hover {
            /* background-color: #0bbcf1; */
            color: #ff0000;
        }

        div {
            padding: 40px;
            text-align: center;
            color:white;
            font-family: 'Jura', sans-serif;
        }

        button {
            display: inline-block;
            padding: 10px 30px;
            font-size: 20px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            font-family: 'Jura', sans-serif;
            outline: none;
            color: #fff;
            /* background-color: #4CAF50; */
            background-color: #0bbcf1;
            border: none;
            border-radius: 15px;
            box-shadow: 0 9px #999;
        }

        button:hover {
            /* background-color: #091eda; */
            background-color: #fff;
            color: #0bbcf1;
        }

        button:active {
            background-color: #c9f117;
            color: #fff;
            box-shadow: 5px 5px 5px 5px #666;
            transform: translateY(5px);
        }

        h1 {
            margin: 20px;
            padding: 40px;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #0bbcf1;
            font-family: 'Jura', sans-serif;
            font-size: 45px;
            cursor: pointer;
            /* background-color: #000; */
            font-family: 'Jura', sans-serif;
        }

        h1 span {
            display: inline-flex;
            color: #0bbcf1;
        }

        h1 span:nth-child(even) {
            overflow: hidden;
            transition: ease-in-out 0.5s;
            /* color: #fff; */
            /* border-bottom: 2px solid #0bbcf1; */
            letter-spacing: -1em;
        }

        h1:hover span:nth-child(even) {
            letter-spacing: 0;
            background: none;
        } 

        h1 span {
            transition: 1s;
        }

        h1:hover span {
            color: rgb(255, 255, 255);
            text-shadow: 0 0 10px #0bbcf1,
                         0 0 20px #0bbcf1,
                         0 0 40px #0bbcf1,
                         0 0 80px #0bbcf1,
                         0 0 120px #0bbcf1,
                         0 0 160px #0bbcf1;
        } 

        h2 span {
            font-size: xx-large;
            font-family: 'Jura', sans-serif; 
            outline-color: #0bbcf1;
            outline-style: dashed; 
            outline-width: 5px; 
            padding: 8px;
            min-width: auto;
        }

    </style>
    <body >
        <h1>
            <span>G</span><span>reatest &nbsp;</span> 
            <span>C</span><span>ommon &nbsp;</span>
            <span>D</span><span>ivisor &nbsp;</span>
            <span>&nbsp;Calculator</span>
        </h1>
        <div>
                <input type="number" id="Text1" name="TextBox1" pattern="-*+*[0-9]+" required="required" onfocusout="this.checkValidity() ? '' : myFunction('Text1')" placeholder="Enter First Number">
                <input type="number" id="Text2" name="TextBox2" pattern="-*+*[0-9]+" required="required" onfocusout="this.checkValidity() ? '' : myFunction('Text2')" placeholder="Enter Second Number"> 
                <!-- <input type="text" id="Text1" name="TextBox1" placeholder="Enter First Number">
                <input type="text" id="Text2" name="TextBox2" placeholder="Enter Second Number">  -->
                <br><br>
                <br><br>
             <button id="buttongcd" onclick="gcd()">Find GCD</button>
             <button id="buttonclear" onclick="allclear()">Clear Data</button>
             <br><br><br><br><br><br><br><br><br><br>
            <h2><span id=Text3 ></span></h2>
            <br>
        </div>
    </body>
    <script>
        function salpaclear(id1) {
            document.getElementById(id1).value = '';
        }
        function allclear() {
            salpaclear('Text1');
            salpaclear('Text2');
            document.getElementById('Text3').innerHTML = '';
        }
        function myFunction(id_var) {
            alert('Enter Only Numbers');
            salpaclear(id_var);
        }
        function gcd() {
            var m1 = document.getElementById("Text1").value;
            var m2 = document.getElementById("Text2").value;
            var n1 = Math.abs(m1);
            var n2 = Math.abs(m2);
            // if(Number.isNaN(n1) && Number.isNaN(n2)) {
            //     alert("Please enter valid Non-zero Numbers");
            //     allclear();
            // }
            // else if(Number.isNaN(n1) )
            // alert("n1 is "+n1);
            // alert("n2 is "+n2);
            if(n1 == '' && n2 == '') {
                alert("Please enter two valid Non-zero numbers");
                allclear();
                return;
            }
            else if(typeof n1 === 'string' && typeof n2 === 'string') {
                //alert("Enter only Numbers");
                allclear();
                return;
            }
            else if(typeof n1 === 'string') {
                    //alert("Enter only Number in First Number");
                    myFunction('Text1');
                    return;
                }
                else if(typeof n2 === 'string'){
                    //alert("Enter only Number in Second Number");
                    myFunction('Text2');
                    return;
                } 
            // var n1 = Math.abs(m1);
            // var n2 = Math.abs(m2);
            if(n1 != '' && n2 != ''){
                if((n1 == 0) || (n2 == 0)){
                    document.getElementById('Text3').innerHTML = 'Invalid values';
                } else {
                    while(n2) {
                        var t = n2;
                        n2 = n1 % n2;
                        n1 = t;
                    }
                    document.getElementById('Text3').innerHTML = 'GCD of ' + document.getElementById("Text1").value + ' and ' + document.getElementById("Text2").value + ' is ' + n1;
                }
            } else{
                document.getElementById('Text3').innerHTML = 'Please enter two valid Non-zero numbers';
            }
        }
    </script>
</html>