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
	<link rel="stylesheet" type="text/css" href="../static/css/styleAR.css" />
</head>
<body>
	<br>
	<header>
		<hgroup>
			<h1><img id="headimg" class="state-bar" src="../static/img/bar_gob2.png"><img src="../static/img/logotrans2.png" width="5%" height="100%"></h1> <br>
		</hgroup>
	</header>
	<br>
	<br>
	<div class="form-container">
		<h2 class="form-tittle">Iniciar Sesión</h2>
			<!--show the error message if the controller sets err=1 in the url query string-->
		<?php if (@$_GET['err'] == 1) { ?>
			<div class="error-text">Usuario incorrecto, vuelva a intentar</div>
		<?php } ?>
		<form method="POST" action="/aristides/index.php">
			<div class="form-group">
				<label for="user" class="percent-width-50">Usuario: </label>
				<input type="text" id="user" class="percent-width-50" name="user" placeholder="Ej: Gabriel Rivero" required/>
			</div>
			<div class="form-group">
				<label for="pass" class="percent-width-50">Contraseña: </label>
				<input type="password" class="percent-width-50" id="pass" name="pass" placeholder="Ej: 12345" required/> <br>
			</div>
			<input type="submit" id="button" name="op" value="Entrar"/>  
		</form>
	</div>	
	<footer>Diseño por Gabriel Rivero. 2016</footer>
</body>
</html>





























