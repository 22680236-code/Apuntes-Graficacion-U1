import turtle

# ==========================================
# PRÁCTICA 1.5 B: La Flor de la Vida
# ==========================================
# Este ejercicio muestra cómo patrones complejos y estéticos
# (geometría sagrada) surgen de la superposición precisa
# de formas primitivas simples (círculos).
# ==========================================

def dibujar_circulo(radio, color):
    t.color(color)
    t.circle(radio)

# --- Configuración Inicial ---
ventana = turtle.Screen()
ventana.bgcolor("black")
ventana.title("Práctica: Flor de la Vida")

t = turtle.Turtle()
t.speed(0) # Velocidad máxima (instantáneo) para dibujar rápido
t.pensize(2)
t.hideturtle()

# --- Parámetros del dibujo ---
radio_circulo = 60
color_trazo = "#f1c40f" # Color dorado

# 1. Círculo Central
t.penup()
t.goto(0, -radio_circulo) # Ajustar para que el centro del círculo sea (0,0)
t.pendown()
dibujar_circulo(radio_circulo, color_trazo)

# 2. Primera capa de 6 círculos (Semilla de la Vida)
# Los centros de estos círculos están en el borde del círculo central.
for i in range(6):
    t.penup()
    t.home() # Volver al centro (0,0)
    t.setheading(i * 60) # Girar 60 grados por cada iteración (360/6)
    t.forward(radio_circulo) # Avanzar hasta el borde del primer círculo
    
    # Ajuste de posición para dibujar el círculo desde su base
    posicion_actual = t.pos()
    t.setheading(0) # Resetear rotación para el comando circle
    t.goto(posicion_actual[0], posicion_actual[1] - radio_circulo)
    
    t.pendown()
    dibujar_circulo(radio_circulo, color_trazo)

print("Patrón base completado. Para la Flor de la Vida completa, se requieren más capas.")
print("Haz clic en la ventana para cerrar.")

ventana.exitonclick()
