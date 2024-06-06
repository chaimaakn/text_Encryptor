# text_Encryptor

Fonctionnalités: 
cette application utilise trois méthodes de cryptage:


1/Cryptage Symétrique
Définition :
Le cryptage symétrique est une méthode de chiffrement où la même clé est utilisée pour chiffrer et déchiffrer les données. Cela signifie que la clé de chiffrement doit être gardée secrète et partagée uniquement entre les parties autorisées. Les algorithmes de cryptage symétrique sont généralement plus rapides que les algorithmes asymétriques.

Algorithmes utilisés :

AES (Advanced Encryption Standard):est un algorithme de cryptage symétrique. Il utilise des clés de longueur variable (128, 192 ou 256 bits) pour chiffrer et déchiffrer les données en blocs de 128 bits. AES est largement utilisé en raison de sa sécurité et de son efficacité. 3DES (Triple DES):Le Triple DES (3DES) est une version améliorée de l'algorithme Data Encryption Standard (DES). Il applique le DES trois fois avec trois clés différentes pour renforcer la sécurité. Bien qu'il soit plus sûr que DES, il est plus lent et a été largement remplacé par des algorithmes plus modernes comme AES. ChaCha20:ChaCha20 est un algorithme de cryptage symétrique conçu pour offrir une sécurité et une performance élevées. Il utilise une clé de 256 bits pour chiffrer les données en flux, offrant ainsi une grande vitesse de traitement et une forte résistance aux attaques. ChaCha20 est souvent utilisé dans des environnements où les performances sont critiques, comme les connexions mobiles et les applications Internet. RC4:RC4 (Rivest Cipher 4) est un algorithme de chiffrement en flux qui utilise une clé de longueur variable pour chiffrer les données. Bien que largement utilisé dans le passé, notamment dans les protocoles SSL/TLS et WEP, RC4 a été abandonné en raison de plusieurs vulnérabilités découvertes, rendant ses implémentations moins sécurisées par rapport aux algorithmes modernes.

2/Cryptage Asymétrique
Définition : 
Le cryptage asymétrique utilise une paire de clés : une clé publique pour chiffrer les données et une clé privée pour les déchiffrer. La clé publique peut être distribuée librement, tandis que la clé privée doit être gardée secrète. Cette méthode est souvent utilisée pour sécuriser la transmission de données sensibles sur des réseaux non sécurisés.

Algorithme utilisé :

RSA (Rivest-Shamir-Adleman):est un algorithme de cryptage asymétrique largement utilisé pour la sécurisation des données. Il fonctionne en utilisant une paire de clés : une clé publique pour le chiffrement et une clé privée pour le déchiffrement. RSA repose sur la difficulté de factoriser de grands nombres premiers, ce qui en fait un choix populaire pour les transactions sécurisées sur Internet, comme les échanges de clés et les signatures numériques.

3/Cryptage Hybride 
Définition :
Le cryptage hybride combine les avantages du cryptage symétrique et asymétrique. Dans ce système, une clé symétrique temporaire (session key) est générée pour chiffrer les données. Cette clé symétrique est ensuite chiffrée avec la clé publique du destinataire et envoyée avec les données chiffrées. Le destinataire utilise sa clé privée pour déchiffrer la clé symétrique, puis utilise cette clé symétrique pour déchiffrer les données. 
Processus :
1.Génération d'une clé symétrique pour chiffrer les données. 2.Chiffrement de la clé symétrique avec la clé publique du destinataire. 3.Envoi de la clé symétrique chiffrée et des données chiffrées au destinataire. 4.Déchiffrement de la clé symétrique avec la clé privée du destinataire. 5.Utilisation de la clé symétrique déchiffrée pour déchiffrer les données.

Algorithme utilisé: Deffie-hallman +AES: Diffie-Hellman est utilisé pour échanger de manière sécurisée une clé de session symétrique, qui est ensuite utilisée pour chiffrer les données avec un algorithme symétrique AES.

PS: le fichier exécutable est interface.py

Ordre à suivre pour crypter et décrypter les messages :

1/Générez les clés via Key Generator (gardez ces clés). 
2/Cryptez le message en utilisant les clés générées (le texte chiffré est automatiquement copié, pas besoin de le faire manuellement). 
3/Décryptez le message en entrant le message chiffré et les clés utilisées pour le chiffrer.

Merciii d'avoir prêté attention à ce projet :)
