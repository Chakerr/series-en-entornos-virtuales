# Proyectos de Series Matemáticas

Este repositorio contiene dos proyectos independientes desarrollados en Python para visualizar series matemáticas mediante gráficas:

1. **Fibonacci Gráfica** (`fibonacci`): genera y grafica la sucesión de Fibonacci.
2. **Taylor Series** (`taylor/`): aproxima la función \(e^x\) usando su serie de Taylor y la grafica.

---

## Estructura de directorios

```
<root>/
├── fibonacci/             ← Proyecto de Fibonacci
│   ├── main.py            ← Script principal para 
│   ├── fibonacci.py       ← Lógica de la sucesión de 
│   └── requirements.txt   ← Dependencias (matplotlib)
|
├── taylor/                ← Proyecto de Taylor
│   ├── main.py            ← Script principal para 
│   ├── taylor.py          ← Lógica de la serie de 
│   └── requirements.txt   ← Dependencias (matplotlib)
|
├── .gitignore             ← Ignora entornos virtuales y cachés
└── README.md              ← Este archivo
```

Cada subcarpeta es un proyecto autónomo con su propio entorno virtual recomendado.

---

## Requisitos generales

- **Python 3.x** instalado en el sistema.
- (Opcional pero recomendado) **Virtualenv** para crear entornos aislados.

---

## Configuración y ejecución de los proyectos

Para **cada** proyecto (`fibonacci-grafica` y `taylor-series`), sigue estos pasos dentro de su carpeta correspondiente:

1. **Crear y activar el entorno virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el script principal**:
   ```bash
   python main.py
   ```

4. **Desactivar el entorno virtual** cuando termines:
   ```bash
   deactivate
   ```

---

## Detalles de cada proyecto

### 1. Fibonacci Gráfica (`fibonacci/`)

- **`fibonacci.py`**: clase `Fibonacci(n_terms)` que genera la lista de términos.
- **`main.py`**: pide al usuario el número de términos y grafica la serie usando matplotlib.
- **`requirements.txt`**: contiene:
  ```
  matplotlib
  ```

**Uso**:
```bash
cd fibonacci
source venv/bin/activate
pip install -r requirements.txt
env/bin/python main.py
```

### 2. Taylor Series (`taylor/`)

- **`taylor.py`**: función `taylor_exp(x, n_terms)` que aproxima \(e^x\) con la serie de Taylor.
- **`main.py`**: solicita al usuario el valor de \(x\) y número de términos, muestra la aproximación y grafica la convergencia.
- **`requirements.txt`**: contiene:
  ```
  matplotlib
  ```

**Uso**:
```bash
cd taylor
source venv/bin/activate
pip install -r requirements.txt
env/bin/python main.py
```


