<?php 
require_once('user_controller.inc.php');
require_once('user_model.inc.php');

@$op = $_REQUEST['op'];

$user_controller = new UserController();

switch ($op) {
	case 'Entrar':
	//here we expect username and password... we omit the validation for now
		$username = $_POST['user'];
		$password = $_POST['pass'];

		if($user_controller->login($username, $password)) {
			header("Location:main.php");
		} else header("Location:login.php?err=1");
		break;

		case 'logout':
		$user_controller->logout();
		header("Location:login.php");
		break;

		default:
			header("Location:login.php");
		break;	
}
 ?>