# 🧬 Payload Analysis

`c1a234c4827bf5e1c0341477461bb6543c1c132cbafea67f6f20dcf98578086d`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Comunicación remota. Se identificaron 28 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:10:53.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c1a234c4827bf5e1c0341477461bb6543c1c132cbafea67f6f20dcf98578086d`
- **MD5:** `b2562808b844a3a68691161f0cfb85b8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Tamaño | 212.8 KiB |
| Entropía | 5.33 |
| Strings | 1521 |

## 🧠 Comportamiento observado

1. **Comunicación remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=unknown; strings=1521; iocs=10

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://github[.]githubassets[.]com/assets/light_colorblind-3a437477a570cc40.css | strings |
| url | hxxps://github[.]githubassets[.]com/ | strings |
| url | hxxps://github[.]community/ | strings |
| url | hxxps://github[.]com/features/code-review | strings |
| url | hxxps://github[.]com/resources/articles?topic=software-development | strings |
| url | hxxps://docs[.]github[.]com/articles/blocking-a-user-from-your-personal-account | strings |
| url | hxxps://github[.]com/robertdavidgraham | strings |
| url | hxxps://github[.]com/solutions/industry/manufacturing | strings |
| url | hxxps://github[.]githubassets[.]com/assets/react-core-e4c170c2bde2bd35.js | strings |
| url | hxxps://github[.]com/features/codespaces | strings |
| url | hxxps://github[.]githubassets[.]com/favicons/favicon.svg | strings |
| url | hxxps://github[.]com/robertdavidgraham?tab=followers | strings |
| url | hxxps://avatars[.]githubusercontent[.]com/u/3814757?v=4?s=400 | strings |
| url | hxxps://github[.]com/solutions/use-case/devops | strings |
| url | hxxps://github[.]com/collections | strings |
| url | hxxps://github[.]com/robertdavidgraham&quot; | strings |
| url | hxxps://github[.]com/features/models | strings |
| url | hxxps://github[.]com/resources/articles?topic=security | strings |
| url | hxxps://github[.]githubassets[.]com/assets/55682-a358ec7c2f348fcf.js | strings |
| url | hxxps://avatars[.]githubusercontent[.]com/u/3814757?s=64&amp;v=4 | strings |
| ip | 012.076.024.XXX | static_analysis |
| ip | 09.047.171.XXX | static_analysis |
| ip | 1.5.75.XXX | static_analysis |
| ip | 5.5.75.XXX | static_analysis |
| ip | 1.7.75.XXX | static_analysis |
| ip | 053.096.108.XXX | static_analysis |
| ip | 4.084.75.XXX | static_analysis |
| ip | 138.112.25.XXX | static_analysis |
| hash | c1a234c4827bf5e1c0341477461bb6543c1c132cbafea67f6f20dcf98578086d | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
