<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>

<body style='background-color:gray;'>
    <form action="{{route('postLogin')}}" method="post">
        <center>
        <h1>Login</h1>
        <input type="email" name="email" id=""><br><br><br>
        <input type="password" name="pass" id=""><br><br>
        <input type="submit" value="enviar">
        </center>
    </form>

</body>

</html>