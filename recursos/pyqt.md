# Ejercicios Ventana
---

### **Ejercicio 1: Ventana básica**

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class VentanaBasica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola, PyQt")  # Título de la ventana
        self.setGeometry(100, 100, 400, 300)  # Posición y tamaño de la ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaBasica()
    ventana.show()
    sys.exit(app.exec_())
```

---

### **Ejercicio 2: Botón interactivo**

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class VentanaConBoton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Botón Interactivo")
        self.setGeometry(100, 100, 300, 200)
        
        # Crear un botón
        self.boton = QPushButton("Hacer clic", self)
        self.boton.setGeometry(100, 80, 100, 30)  # Posición y tamaño
        
        # Conectar el botón con una acción
        self.boton.clicked.connect(self.mostrar_mensaje)
    
    def mostrar_mensaje(self):
        print("¡Botón presionado!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaConBoton()
    ventana.show()
    sys.exit(app.exec_())
```

---

### **Ejercicio 3: Campo de texto**

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class CampoDeTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Campo de Texto")
        self.setGeometry(100, 100, 400, 200)
        
        # Crear un campo de texto
        self.campo_texto = QLineEdit(self)
        self.campo_texto.setGeometry(50, 50, 200, 30)
        
        # Crear un botón
        self.boton = QPushButton("Mostrar texto", self)
        self.boton.setGeometry(270, 50, 100, 30)
        self.boton.clicked.connect(self.mostrar_texto)
    
    def mostrar_texto(self):
        print(self.campo_texto.text())  # Imprimir el texto ingresado

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CampoDeTexto()
    ventana.show()
    sys.exit(app.exec_())
```

---

### **Ejercicio 4: Etiqueta actualizable**

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class EtiquetaDinamica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Etiqueta Dinámica")
        self.setGeometry(100, 100, 400, 200)
        
        # Crear una etiqueta
        self.etiqueta = QLabel("Texto vacío", self)
        self.etiqueta.setGeometry(50, 50, 300, 30)
        
        # Crear un campo de texto
        self.campo_texto = QLineEdit(self)
        self.campo_texto.setGeometry(50, 100, 200, 30)
        
        # Crear un botón
        self.boton = QPushButton("Actualizar etiqueta", self)
        self.boton.setGeometry(270, 100, 100, 30)
        self.boton.clicked.connect(self.actualizar_etiqueta)
    
    def actualizar_etiqueta(self):
        texto = self.campo_texto.text()
        self.etiqueta.setText(texto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = EtiquetaDinamica()
    ventana.show()
    sys.exit(app.exec_())
```

---

### **Ejercicio 5: Diseño de widgets**

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class DisenoVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diseño de Widgets")
        
        # Diseño vertical
        layout_principal = QVBoxLayout()
        
        # Etiqueta arriba
        self.etiqueta = QLabel("Ingrese un texto:")
        layout_principal.addWidget(self.etiqueta)
        
        # Diseño horizontal para campo y botón
        layout_horizontal = QHBoxLayout()
        self.campo_texto = QLineEdit()
        self.boton_actualizar = QPushButton("Actualizar")
        layout_horizontal.addWidget(self.campo_texto)
        layout_horizontal.addWidget(self.boton_actualizar)
        layout_principal.addLayout(layout_horizontal)
        
        # Botón de salida abajo
        self.boton_salir = QPushButton("Salir")
        self.boton_salir.clicked.connect(self.close)
        layout_principal.addWidget(self.boton_salir)
        
        self.setLayout(layout_principal)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = DisenoVentana()
    ventana.show()
    sys.exit(app.exec_())
```

---



### **Ejercicio 6: Caja de selección**

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel

class CajaDeSeleccion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caja de Selección")
        self.setGeometry(100, 100, 300, 200)
        
        # Crear una lista desplegable (ComboBox)
        self.combo = QComboBox(self)
        self.combo.setGeometry(50, 50, 200, 30)
        self.combo.addItems(["Opción 1", "Opción 2", "Opción 3"])
        
        # Crear una etiqueta
        self.etiqueta = QLabel("Seleccione una opción", self)
        self.etiqueta.setGeometry(50, 100, 200, 30)
        
        # Conectar el ComboBox con la acción
        self.combo.currentTextChanged.connect(self.actualizar_etiqueta)
    
    def actualizar_etiqueta(self, texto):
        self.etiqueta.setText(f"Seleccionado: {texto}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CajaDeSeleccion()
    ventana.show()
    sys.exit(app.exec_())
```

---

### **Ejercicio 7: Barra de menús**

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

class BarraDeMenus(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barra de Menús")
        self.setGeometry(100, 100, 400, 300)
        
        # Crear la barra de menús
        barra_menu = self.menuBar()
        
        # Agregar un menú
        menu_archivo = barra_menu.addMenu("Archivo")
        
        # Crear una acción
        accion_salir = QAction("Salir", self)
        accion_salir.triggered.connect(self.close)
        
        # Agregar la acción al menú
        menu_archivo.addAction(accion_salir)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = BarraDeMenus()
    ventana.show()
    sys.exit(app.exec_())
```

---

### **Ejercicio 8: Diálogo de archivo**

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QFileDialog

class DialogoArchivo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diálogo de Archivo")
        self.setGeometry(100, 100, 600, 400)
        
        # Crear un área de texto
        self.area_texto = QTextEdit(self)
        self.area_texto.setGeometry(50, 50, 500, 250)
        
        # Crear un botón
        self.boton_abrir = QPushButton("Abrir archivo", self)
        self.boton_abrir.setGeometry(250, 320, 100, 30)
        self.boton_abrir.clicked.connect(self.abrir_archivo)
    
    def abrir_archivo(self):
        # Mostrar un diálogo para seleccionar el archivo
        ruta_archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt)")
        if ruta_archivo:
            with open(ruta_archivo, "r") as archivo:
                contenido = archivo.read()
                self.area_texto.setText(contenido)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = DialogoArchivo()
    ventana.show()
    sys.exit(app.exec_())
```

---

### **Ejercicio 9: Tablas de datos**

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class TablaDatos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tablas de Datos")
        self.setGeometry(100, 100, 400, 300)
        
        # Crear una tabla
        self.tabla = QTableWidget(self)
        self.tabla.setGeometry(50, 50, 300, 200)
        self.tabla.setRowCount(3)
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(["Nombre", "Edad"])
        
        # Agregar datos
        datos = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
        for fila, (nombre, edad) in enumerate(datos):
            self.tabla.setItem(fila, 0, QTableWidgetItem(nombre))
            self.tabla.setItem(fila, 1, QTableWidgetItem(str(edad)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TablaDatos()
    ventana.show()
    sys.exit(app.exec_())
```

---

### **Ejercicio 10: Gráficas con PyQt**

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt5.QtCore import Qt

class GraficasBarras(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráficas con PyQt")
        self.setGeometry(100, 100, 600, 400)
        
        # Crear una vista y una escena
        self.vista = QGraphicsView(self)
        self.vista.setGeometry(50, 50, 500, 300)
        self.escena = QGraphicsScene()
        self.vista.setScene(self.escena)
        
        # Dibujar barras
        valores = [50, 120, 80]
        for i, valor in enumerate(valores):
            barra = QGraphicsRectItem(i * 60, 300 - valor, 40, valor)
            barra.setBrush(Qt.blue)
            self.escena.addItem(barra)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = GraficasBarras()
    ventana.show()
    sys.exit(app.exec_())
```

---

