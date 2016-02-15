<?php 
require_once('../models/user_model.inc.php');
//we want to redirect the user to the login if his session is expired/invalid
session_start();
if (!isset($_SESSION['user'])) {
	header("Location:login.php");
} else {
	$user = $_SESSION['user'];
}

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
	<div class="flex-container">
  		<div class="flex-item">flex item 1</div>
  		<div class="flex-item">flex item 2</div>
  		<div class="flex-item">flex item 3</div> 
  		<div class="flex-item">flex item 4</div>  
	</div>

	<br>

	<div class="logoutButton">
	<a class="logout" href="index.php?op=logout">Desconectarse</a>
	</div>

	<footer>Diseño por Gabriel Rivero. 2016</footer>
</body>
</html>
