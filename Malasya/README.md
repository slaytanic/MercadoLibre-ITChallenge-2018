# 🇲🇾 Malasya

Hemos definido nuestro propio lenguaje de marcado, HRML.

En HRML, cada elemento consta de una etiqueta de inicio y atributos asociados a ella. Para cerrar un elemento, hay 2 opciones: una etiqueta de cierre separada, o; la etiqueta de cierre con una sintaxis especial. Solo las etiquetas de inicio pueden tener atributos. Las etiquetas también pueden estar anidadas.

Las etiquetas de apertura siguen el formato:

```xml
<tag-name attribute1-name="value1" attribute2-name="value2" ... >
```

Las etiquetas de cierre siguen el formato:

En la línea
```xml
<tag-name attribute1-name="value1" ... />
```

Etiqueta separada:
```xml
</tag-name>
```

Podemos llamar a un atributo haciendo referencia a la etiqueta, seguida del símbolo '~' y el nombre del atributo. Para atravesar etiquetas anidadas usamos el carácter '.” entre las etiquetas.

Por ejemplo:

```xml
<tag1 value="HelloWorld">
  <tag2 desc="Description1" />
  <tag3 name="Name2">
    <tag4 quantity="12" />
  </tag3>
</tag1>
```

Los atributos se referencian como:

```
tag1~value
tag1.tag2~desc
tag1.tag3~name
tag1.tag3.tag4~quantity
```

Recibes un conjunto ordenado de archivos. Se te proporciona un código fuente válido en formato HRML que consta de N líneas. Tienes que responder Q consultas asociadas a cada código fuente. Cada consulta te pide que imprimas el valor del atributo especificado en una nueva línea separada. Imprimir "¡No encontrado!" si no existe dicho atributo.

La respuesta que le permitirá continuar con la competencia será el hash SHA-256 (en mayúsculas) de un archivo que contiene todos los valores obtenidos como resultado de las consultas (respecto del pedido), un valor por línea, sin líneas en blanco (excepto una última nueva línea vacía que debe estar presente). Use solo LF (0x0A) como nueva línea.

Formato de entrada de cada archivo

La primera línea consta de dos enteros separados por espacio, N y Q. Las siguientes N líneas del código fuente de HRML válido y cada línea constan de una etiqueta de apertura con cero o más atributos, o una etiqueta de cierre. Luego, las siguientes líneas Q contienen las consultas. Cada consulta consiste en una string que hace referencia a un atributo en el código fuente HRML.

Restricciones

N> = 1

N> = 1

Todos los nombres de etiquetas son únicos.

Sample Input for one file

4 3

```xml
<tag1 value = "HelloWorld">
  <tag2 name = "Name1">
  </tag2>
</tag1>
```

```
tag1.tag2~name
tag1~name
tag1~value
```

Sample Output for one file

```
Name1
Not Found!
HelloWorld
```

https://www.dropbox.com/s/tdpttblm5ez64vq/HRML%20Parser.zip?dl=0
