import pygame
from Key_State import Key_State
from Model import Model
from Point import Point

# Variables
start = False
time_elapsed = 0
max_voltage = 12.0
voltage = 12.0
window_size = 800
model = Model(0.3, 0.0024, 0.0075)
time_increment = 0.1
time_scale_factor = 1/time_increment
rpm_scale_factor = model.get_rpm_scale_factor(800.0, max_voltage)
points = []

# Variables to manage the key states
key_up = Key_State(Key_State.states.RELEASED, time_elapsed)
key_down = Key_State(Key_State.states.RELEASED, time_elapsed)

# Window
window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Shooter Model")
window.fill((0, 0, 0))

# Window Loop
running = True
while running:

    # Preform resetting actions and delays
    window.fill((0, 0, 0))
    pygame.time.delay(10)

    # Check the event list
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key_up.update_state(Key_State.states.PRESSED, time_elapsed)
            if event.key == pygame.K_DOWN:
                key_down.update_state(Key_State.states.PRESSED, time_elapsed)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                key_up.update_state(Key_State.states.RELEASED, time_elapsed)
            if event.key == pygame.K_DOWN:
                key_down.update_state(Key_State.states.RELEASED, time_elapsed)

    if start:
        # If the points list is empty add a new point
        if len(points) == 0:
            points.append(Point(0, 0, time_scale_factor, rpm_scale_factor, window_size))

        # If the points list has more points then there are pixels then remove a point
        if len(points) >= window_size:
            points.pop(0)
            for point in points:
                point.model_time -= time_increment

        # Add a new point
        prev_point = points[-1]
        velocity = model.get_velocity(prev_point.model_rpm, voltage, time_increment)
        new_point = Point(
            prev_point.model_time + time_increment,
            velocity,
            time_scale_factor,
            rpm_scale_factor,
            window_size
        )
        points.append(new_point)

        # Draw all of the points
        for i in range(len(points) - 1):
            pygame.draw.line(
                window,
                (255, 255, 255),
                (points[i].get_draw_x(), points[i].get_draw_y()),
                (points[i + 1].get_draw_x(), points[i + 1].get_draw_y()),
                1
            )

        # Update the time elapsed
        time_elapsed += time_increment

        # Update the voltage
        priority = key_up.is_priority(key_down)
        if priority is None:
            voltage += 0
        elif priority and voltage < max_voltage:
            voltage += 0.1
        elif not priority and voltage > 0:
            voltage -= 0.1

    # Update the window
    pygame.display.flip()
