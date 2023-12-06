120704Gvnn

ssh root@143.198.186.226
scp -r ./* root@143.198.186.226:/opt/brabozo

143.198.186.226
http://143.198.186.226/phpmyadmin/index.php

admin
ccc4a4b0f237275f165bb45afe28f39d05d39d3f308be7df

mysql -u root -p -h localhost

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'a3cb636e07a424c1d8d2507a5a9ade1e38d78aa1eed40a3a';

CREATE USER 'brabozodb'@'%' IDENTIFIED BY 'a3cb636e07a424c1d8d2507a5a9ade1e38d78aa1eed40a3a';
ALTER USER 'brabozodb'@'179.208.52.241' IDENTIFIED BY 'a3cb636e07a424c1d8d2507a5a9ade1e38d78aa1eed40a3a';

GRANT ALL PRIVILEGES ON brabozo.* TO 'brabozodb'@'%';