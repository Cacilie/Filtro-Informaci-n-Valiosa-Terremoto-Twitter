# Filtro-Informaci-n-Valiosa-Terremoto-Twitter
Filtra información valiosa relacionada al terremoto 09-19-2017

## Lo que hace
Busca tweets relacionados al terremoto ocurrido el 09-19-2017 y a través de un filtro con palabras claves, recoge los
tweets que podrían ser inportante, ya sea porque previenen de un peligro o intentan ayudar y pedir ayuda.
 
Las palabras claves actuales son:
1. evitar
2. eviten
3. centro
4. acopio
5. ayudar
6. importante
7. donativos
8. colapsar
9. albergue
10. comida
11. daños
12. necesitan
13. riesgo
14. necesidades
15. necesita
16. apoyo
17. urgente
18. agua
19. medicos
20. #busco
21. busco
22. tengo
23. #tengo
24. #necesito
25. necesito
26. tenemos
27. #tenemos
28. requieren
29. #requiero
30. requiero
31. necesitamos
32. #necesitamos


Se recuperan tweets relacionados a estas palabras claves y que incluyan como mención a @comoayudarmx y se retweetea a la cuenta asociada.

Ejemplo:

1.- Se corre el Script.
2.- El script busca información relevante con mención a @comoayudarmx y que pase los filtros.
3.- Se hace RT a la información relevante con la cuenta asociada.

Para asociar tu cuenta, tienes que llenar los datos que se piden en credentials.example.py 
y quitarle el credentials, de tal manera que quede credentials.py


## Si deseas...

Si deseas agregar más palabras clave, añadelas en el archivo keywords.py-
Si deseas cambiar el hashtag buscado, sólo tienes que modificar el query en searcher.py linea 31.

Es necesario configurar que el script se ejecute cada cierto tiempo en el servidor. Bastará con un script :D

## Se pretende

Que se consiga información más valiosa.

# Importante

Este trabajo y muchos otros apoyan las iniciativas de Codeando México. Si deseas ayudar te invito al slack
codeandomexico.slack.com


