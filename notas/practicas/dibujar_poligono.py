import turtle

# ==========================================
# PRÁCTICA 1.5 A: Dibujo de un Polígono Regular
# ==========================================
# Este script demuestra cómo la repetición de instrucciones
# simples de trazo (avanzar y girar) genera formas geométricas.
# ==========================================

def dibujar_poligono(lados, longitud):
    """
    Dibuja un polígono regular.
    Parámetros:
        lados (int): Número de lados del polígono.
        longitud (int): Longitud de cada lado en píxeles.
    """
    # El ángulo de giro exterior para un polígono regular es 360 / N lados
    angulo = 360 / lados

    # Bucle para dibujar cada lado
    for _ in range(lados):
        t.forward(longitud) # Avanzar (Trazar línea)
        t.right(angulo)     # Girar

# --- Configuración Inicial ---
ventana = turtle.Screen()
ventana.bgcolor("#2b2b2b") # Fondo oscuro
ventana.title("Práctica: Polígonos")

t = turtle.Turtle()
t.shape("turtle")
t.color("#00ff9d") # Color verde neón
t.speed(3) # Velocidad media (1=lento, 10=rápido, 0=instantáneo)
t.pensize(2)

# --- Dibujar ---
# Movemos la tortuga para empezar más arriba
t.penup()
t.goto(-50, 150)
t.pendown()

# Dibujar un Cuadrado (4 lados)
t.color("#ff5e57")
dibujar_poligono(4, 100)

# Mover a otra posición
t.penup()
t.goto(-50, -50)
t.pendown()

# Dibujar un Hexágono (6 lados)
t.color("#00d2d3")
dibujar_poligono(6, 100)

# Finalizar
t.hideturtle() # Ocultar el cursor
print("Polígonos dibujados. Haz clic en la ventana para cerrar.")
ventana.exitonclick()
