<!doctype html>
<html lang="pt-br">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
		
		<title>Form Pessoa</title>
    <style>
        body {
					height: 100vh;
					width: 100%;
					background-color: #212121;

					display: flex;
					flex-direction: column;

					gap: 1rem;

					color: rgb(118, 226, 154);
				}

        h1, h2, h3 {
          color: rgb(118, 226, 154);
        }
    </style>
  </head>
  <body>
    <?php
			//print "entrei....<br/>";
			//print_r($_POST);
			//print "<br/>";
				if (
				IsSet($_POST['txtNome']) && IsSet($_POST['txtEndereco']) &&
				IsSet($_POST['txtTelefone']) && IsSet($_POST['txtCep'])
			)
			{
				$marray=array();
				$erro = FALSE;
				
				if($_POST['txtNome']=="") {
					$marray[0]= "Nome não cadastrado!";
					$erro = TRUE;		
				}
				
				if($_POST['txtEndereco']== "") {
					$marray[1]= "Endereço não cadastrado!";
					$erro = TRUE;		
				}
					
				if($_POST['txtTelefone']== "") {
					$marray[2]= "Telefone não adastrado!";
					$erro = TRUE;		
				}
				if($_POST['txtCep']== "") {
					$marray[3]= "Cep não cadastrado!";
					$erro = TRUE;		
				}
					
				if( $erro == TRUE ) {
					print "<h1>Erro</h1>";
					print_r($marray);
					print"<a href=pessoa.html>Tente novamente! </a>";
				} else 	{
					//print "no else";
					
					print "<h1>Olá " . $_POST['txtNome'] . "</h1>";
					print "<h2>Reside no endereço: " . $_POST['txtEndereco'] . "</h2>";
					print "<h2>Telefone: " . $_POST['txtTelefone'] . "</h2>";
					print "<h2>CEP: " . $_POST['txtCep'] . "</h2>";
					if (IsSet($_POST['txtEscondido'])) { 
						print "<h3>Campo escondido: " . $_POST['txtEscondido'] . "</h2>";
					} else {
						print "<h3>Campo escondido não encontrado, verifique o nome do campo: txtEscondido</h3>";
					}
					//print "que que deu?";
				}
			} else {
				print "Variaveis não definidas, precisa ser um POST com txtNome, txtEndereco, txtTelefone e txtCep";
			}
			
		?>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  </body>
</html>