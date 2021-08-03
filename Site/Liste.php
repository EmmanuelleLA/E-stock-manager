<?php

	// Open DB
	include_once("dbConfig.php");
	$mysqli = new mysqli(DB_HOST, DB_LOGIN, DB_PWD, DB_NAME);
	$mysqli->set_charset("utf8");
	?>






<!DOCTYPE html>

<html>
<!-- En tête -->
<head>
	<!-- Fichiers CSS -->
	<link rel='stylesheet' type='text/css' href='./css/web.css' media='screen' />
	<!-- <link rel='stylesheet' type='text/css' href='./css/00_reset.css' media='screen' /> -->
	<!-- <link rel='stylesheet' type='text/css' href='./css/01_mobile.css' media='screen' /> -->
	<!-- <link rel='stylesheet' type='text/css' href='./css/02_fonts.css' media='screen' /> -->

	<!-- Fichiers Javascripts -->
	<script type='text/javascript' src='./js/jquery-2.0.3.min.js'></script>
	<script type='text/javascript' src='./js/web.js'></script>

	<!-- Encodage UTF8 pour les accents -->
	<meta charset='UTF-8'>

	<!-- Icône de l'onglet -->
	<link rel='icon' type='image/png' href='./images/favicon.png' />

	<!-- Titre de l'onglet -->
	<title></title>
</head>



<!-- Corps du document -->
<body>
	<!-- Wrapper -->
	<div class='wrapper'>


		<header>
			<h1> Inventaire</h1>

		</header>

		<nav>


		</nav>
 <button onclick="window.location.href = 'index.php';">Accueil</button>

		<section>
			<article>

			<p> Produits</p>

			<p class='Nameprod'> Nom</p>
			<!-- <p class='quantité'> Quantité</p> -->
			<p> Quantité</p>
		</article>

			<article>
				<ul class='pim'>
					<?php
					// Query : select
					$query = "SELECT * FROM Products;";
					$result = $mysqli->query($query);

					// Query result
					while ($row = $result->fetch_assoc()) {


						$url =$row['url'];


						// echo "<li>" . $row['quantity'] . "</li>";
						echo "<li class='pom'>
						<td>
						<img class='img' src='".$url."' height='90' width='80' alt='image'>
						</td>
						</li>";
					}
					$result->close();

					?>

				</ul>
			<ul>
			<?php

								// Query : select
								$query = "SELECT * FROM Products;";
								$result = $mysqli->query($query);

								// Query result
								while ($row = $result->fetch_assoc()) {

									echo "<li class='BDnom'>" . $row['Name'] . "</li>";

								}
								$result->close();
			?>
		</ul>

			<ul>
			<?php
								// Query : select
								$query = "SELECT * FROM Products;";
								$result = $mysqli->query($query);

								// Query result
								while ($row = $result->fetch_assoc()) {
									echo "<li class='BDquant'>" . $row['quantity'] . "</li>";
								}
								$result->close();
			?>

			</ul>
			</article>
		</section>
	</div>

</body>
</html>
