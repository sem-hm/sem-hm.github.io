---
layout: post
title: "Instala y configura ZSH + Oh My Zsh en tu terminal"
date: 2025-06-22
categories: terminal linux productividad
---

En este post aprenderás cómo instalar **ZSH**, configurarlo con **Oh My Zsh** y personalizarlo con un tema atractivo. Si estás cansado de la apariencia básica de Bash, esta es una excelente forma de modernizar tu terminal.

---

## ¿Qué es ZSH?

**ZSH (Z Shell)** es un intérprete de comandos para sistemas tipo Unix que extiende funcionalidades de Bash, con mejoras como autocompletado inteligente, sugerencias y más personalización.

---

## Paso 1: Instalar ZSH

Primero, asegúrate de tener `zsh` instalado. Ejecuta el siguiente comando:

```bash
sudo apt update && sudo apt install zsh -y
```


Para verificar la instalación:

```bash
zsh --version
```

![zsh --version](/assets/blog/zsh/image1.png)

---

## Paso 2: Establecer ZSH como tu shell por defecto

```bash
chsh -s $(which zsh)
```

⚠️ Tendrás que cerrar sesión o reiniciar la terminal para que los cambios surtan efecto.

⚠️ probablemente tengas que seleccionar una opcion (2) para realizar la configuracion inicial.

![zsh first open](/assets/blog/zsh/image2.png)

---

## Paso 3: Instalar Oh My Zsh

Oh My Zsh es un framework para gestionar configuraciones de ZSH con cientos de temas y plugins.

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

![oh my zsh installed](/assets/blog/zsh/image3.png)

Una vez finalice, deberías ver una terminal renovada y un archivo `.zshrc` en tu carpeta home.

---

## Paso 4: Cambiar el tema de ZSH

Edita tu archivo `.zshrc` para cambiar el tema. Por defecto, Oh My Zsh usa `robbyrussell`, pero puedes usar uno como `agnoster` o `bira`.

```bash
nano ~/.zshrc
```

Busca la línea que dice:

```bash
ZSH_THEME="robbyrussell"
```

Y cámbiala por:

```bash
ZSH_THEME="agnoster"
```

![oh my zsh theme changing](/assets/blog/zsh/image4.png)

Guarda y cierra, luego recarga la configuración:

```bash
source ~/.zshrc
```

![oh my zsh new theme](/assets/blog/zsh/image5.png)

Ademas de eso voy actualizar el tema de la terminal por uno en modo dark:

![oh my zsh new theme](/assets/blog/zsh/image6.png)

Podemos tener un mejor resultado:

![oh my zsh new theme](/assets/blog/zsh/image7.png)

---


## Conclusión

¡Listo! Ahora tienes un terminal más moderno, funcional y bonito. En próximos posts veremos cómo agregar plugins útiles como autocompletado de Git, resaltado de sintaxis y más.

---

¿Te gustó este post? ¿Tienes dudas o sugerencias? Déjalas en los comentarios abajo.
