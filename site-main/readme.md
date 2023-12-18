/* conecta no servidor, usando a senha que foi definida por voce

ssh root@"IP do seu servidor"

*/

/* envia TODOS os arquivos e pastas a partir da pasta aonde voce abriu o prompt para o respectivo servidor com o IP 

scp -r ./* root@143.198.186.226: "caminho da pasta aonde vc quer guardar o projeto :)"

// lembrando que esse ultimo comando e feito na SUA maquina, nao no servidor, e de preferencia esteja na pasta aonde todos os arquivos e pastas serao transferidos para o servidor

*/

143.198.186.226
http://143.198.186.226/phpmyadmin/index.php

/* senha de usuario administrativo do MySQL

admin
ccc4a4b0f237275f165bb45afe28f39d05d39d3f308be7df
*/

/* alguns comandos uteis para configurar o usuario no MySQL

mysql -u root -p -h localhost

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'a3cb636e07a424c1d8d2507a5a9ade1e38d78aa1eed40a3a';

CREATE USER 'brabozodb'@'%' IDENTIFIED BY 'a3cb636e07a424c1d8d2507a5a9ade1e38d78aa1eed40a3a';
ALTER USER 'brabozodb'@'179.208.52.241' IDENTIFIED BY 'a3cb636e07a424c1d8d2507a5a9ade1e38d78aa1eed40a3a';

GRANT ALL PRIVILEGES ON brabozo.* TO 'brabozodb'@'%';

*/ 

http://143.198.186.226:8080/api/log/int ?
http://143.198.186.226:8080/logs
http://143.198.186.226:8080
