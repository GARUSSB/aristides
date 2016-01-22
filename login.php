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
			<h1 style="height:70px"><img id="headimg" style="width:95%;height:100%" src="static/img/bar_gob2.png"><img src="static/img/logotrans2.png" width="5%" height="100%"></h1> <br>
		</hgroup>
	</header>
	<br>
	<br>
	<div class="form-container">
		<h2>Iniciar Sesión</h2>
			<!--show the error message if the controller sets err=1 in the url query string-->
		<?php if (@$_GET['err'] == 1) { ?>
			<div class="error-text">Login Incorrect. Please try again</div>
		<?php } ?>
		<form method="POST" action="index.php">
			<label>Usuario: </label>
				<input type="text" id="user" name="user" placeholder="Ej: Gabriel Rivero" required/> <br>
			<label>Contraseña: </label>
				<input type="password" id="pass" name="pass" placeholder="Ej: 12345" required/> <br>
			<input type="submit" id="button" name="op" value="Entrar"/>  
		</form>
	</div>	
	<footer>Diseño por Gabriel Rivero. 2016</footer>
</body>
</html>





























