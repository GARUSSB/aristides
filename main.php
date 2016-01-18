<?php 
require_once('user_model.inc.php');
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
</head>
<body>
	<p>
		You are now logged in
		...this is the main.
		<a href="index.php?op=logout">Logout</a>
	</p>
</body>
</html>