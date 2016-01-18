<?php 
//we want to redirect the user to the main if he is already logged in
session_start();
if(isset($_SESSION['user'])) header("Location:main.php");
 ?>
<html>
<head>
	<title></title>
	<meta lang="es">
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="styleAR.css" />
</head>
<body>
	<br>
	<header>
		<hgroup>
			<h1><img id="headimg" src="bar_gob2.png"><img src="logotrans2.png" width="60px" height="75px"></h1> <br>
		</hgroup>
	</header>
	<br>
	<br>
	<div>
		<h1>Iniciar Sesión</h1>
			<!--show the error message if the controller sets err=1 in the url query string-->
		<?php if (@$_GET['err'] == 1) { ?>
			<div class="error-text">Login Incorrect. Please try again</div>
		<?php } ?>
		<form method="POST" action="index.php">
			<a>Usuario: &nbsp</a>
				<input type="text" id="user" name="user" placeholder="Ej: Gabriel Rivero" required/> <br>
			<a>Contraseña: &nbsp</a>
				<input type="password" id="pass" name="pass" placeholder="Ej: 12345" required/> <br>
			<input type="submit" id="button" name="op" value="Entrar"/>  
		</form>
	</div>	
	<footer>Diseño por Gabriel Rivero. 2016</footer>
</body>
</html>